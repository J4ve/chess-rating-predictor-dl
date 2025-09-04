import pandas as pd
import chess
import chess.pgn
import torch
import re
from datetime import timedelta
from io import StringIO
import pickle

def board_to_array(board):
    """Converts a chess board into a 12-layer 8x8 tensor representing the piece positions."""
    board_array = torch.zeros((12, 8, 8), dtype=torch.float32)
    piece_map = board.piece_map()
    for square, piece in piece_map.items():
        index = piece.piece_type - 1 + (6 if piece.color == chess.BLACK else 0)
        row, col = divmod(square, 8)
        board_array[index, 7 - row, col] = 1
    return board_array


def algebraic_to_uci(game_moves):
    """
    Convert a sequence of algebraic notation moves to UCI format.
    
    Parameters:
        game_moves (list): A list of moves in algebraic notation.
        
    Returns:
        list: A list of moves in UCI format, or None if the moves are invalid.
    """
    board = chess.Board()
    uci_moves = []
    
    for move in game_moves:
        try:
            uci_move = board.push_san(move).uci()  # Convert algebraic move to UCI
            uci_moves.append(uci_move)
        except ValueError as e:
            print(f"Invalid move '{move}': {e}")
            return None  # Return None if the moves are invalid
    return uci_moves

def clean_uci_moves(uci_moves):
    """
    Cleans the UCI moves string by removing unwanted characters like move numbers and results.

    Args:
        uci_moves (str | list): UCI moves as a string or list.

    Returns:
        list: A list of valid UCI moves.
    """
    if isinstance(uci_moves, list):
        # If already a list, return it as is
        return [move for move in uci_moves if not any(x in move for x in ['.', '1-0', '0-1', '1/2-1/2'])]

    if isinstance(uci_moves, str):
        # If it's a string, split it and clean the moves
        return [move for move in uci_moves.split() if not any(x in move for x in ['.', '1-0', '0-1', '1/2-1/2'])]

    # Return an empty list for invalid types
    return []

def parse_uci_moves_to_game(uci_moves):
    """Parses UCI moves into a PGN game."""
    
    # Ensure moves are cleaned first
    if isinstance(uci_moves, str):
        filtered_moves = clean_uci_moves(uci_moves)  # Use cleaner function
    elif isinstance(uci_moves, list):
        filtered_moves = clean_uci_moves(" ".join(uci_moves))
    else:
        return None  # Invalid input type

    uci = algebraic_to_uci(filtered_moves)
    if uci is None:
        return None  # Invalid UCI moves

    game = chess.pgn.Game()
    node = game
    board = chess.Board()

    array_list = []
    for move in uci:
        array = board_to_array(board)
        array_list.append(array)

        try:
            uci_move = chess.Move.from_uci(move)
            if uci_move not in board.legal_moves:
                return None
            node = node.add_variation(uci_move)
            board.push(uci_move)
        except ValueError:
            return None

    return array_list


def parse_game(game):
    """Parses game object to extract evaluations, clocks, and positions."""
    board = game.board()
    moves = []
    clocks = []
    positions = []
    node = game

    # Count the number of moves in the game
    move_count = 0
    temp_node = node
    while temp_node.variations:
        move_count += 1
        temp_node = temp_node.variation(0)

    # Parse moves and positions
    while node.variations:
        next_node = node.variation(0)
        move = next_node.move
        board.push(move)
        positions.append(board_to_array(board))
        moves.append(move.uci())
        node = next_node

    return {
        "Result": game.headers.get("Result", None),
        "Positions": positions,
        "Moves": moves,
        "Clocks": clocks,  # Include the generated times
    }


def process_csv(file_path):
    """Processes the CSV file and extracts chess data."""
    # Load the CSV
    df = pd.read_csv(file_path)

    #results = []
    #breakpoint()
    for i, row in df.iterrows():
        try:
            # Ensure the 'Game' column is treated as a string
            raw_moves = str(row['Game']) if not pd.isna(row['Game']) else ""
            if raw_moves.strip() == "":
                print(f"Skipping row with missing or empty 'Game' column at index {i}")
                continue

            # Clean the UCI moves
            notuci_moves = clean_uci_moves(raw_moves)
            #heres the problem lmao i fixed it (its not converting the things)
            uci_moves = algebraic_to_uci(notuci_moves)
            

            if not uci_moves:
                print(f"Skipping row with invalid 'Game' data at index {i}")
                continue
            
            white_elo = row.get('Elo White', None)
            black_elo = row.get('Elo Black', None)
            result = row.get('Score', None)

            # Validate ELOs
            if not isinstance(white_elo, (int, float)) or not isinstance(black_elo, (int, float)):
                print(f"Skipping row with invalid ELO values at index {i}")
                continue

            # Parse UCI moves into board positions
            positions = parse_uci_moves_to_game(uci_moves)
            if positions is None:
                print(f"Skipping invalid game at index {i}: {raw_moves}")
                continue
            
            game_info = {"Positions": positions}
            filename = "games/" + str(i) + ".pkl"

            with open(filename, 'wb') as file:
                pickle.dump(game_info, file)


            # Prepare result for output
            # results.append({
            #     "Row": i,
            #     "Positions": positions,
            # })
            # Row, White Rating, Black Rating

            # add the columns for White Rating and Black Rating to the rows in the original csv

            #progress l og
            if i % 1000 == 0 and i > 0:
                print(f"Processed {i} rows...")
                #return pd.DataFrame(results)

        except KeyError as e:
            print(f"Missing expected column at index {i}: {row} - {e}")
        except Exception as e:
            print(f"Unexpected error at index {i}: {e}")

    # Convert results to a DataFrame for analysis
    #return pd.DataFrame(results)

# Example Usage
file_path = "Games.csv"  # CSV file path
processed_data = process_csv(file_path)

# Save the processed data to a new CSV
#processed_data.to_csv("processed_data.csv", index=False)
