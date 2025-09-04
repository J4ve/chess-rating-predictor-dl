import csv
import torch
import pickle
import os
import numpy as np
from chess_rating_net import ChessEloPredictor
from chess_rating_net import time_to_seconds

def load_model_and_save_to_csv(model_path, data_dir, output_csv_path):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    params = {
        'train_batch_size': 32,
        'val_batch_size': 32,
        'num_workers': 16,
        'learning_rate': 0.0001,
        'weight_decay': 1e-5,
        'epochs': 100,
        'optimizer': 'Adam',
        'patience': 5,
        'lr_factor': 0.5,
        "conv_filters": 32,
        "lstm_layers": 3,
        "bidirectional": True,
        "dropout_rate": 0.5,
        "lstm_h": 64,
        "fc1_h": 32
    }
    model = ChessEloPredictor(params["conv_filters"], params["lstm_layers"], params["dropout_rate"],
                              params["lstm_h"], params["fc1_h"], params["bidirectional"]).to(device)
    
    saved_model = torch.load(model_path, map_location=torch.device('cpu'))
    model.load_state_dict(saved_model["model_state_dict"])
    model.eval()
    
    all_files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith('.pkl')]
    
    output = []
    mean_rating = 1514  # Default mean rating
    ratings_mean = 1514
    ratings_std = 366

    for file_path in all_files:
        with open(file_path, 'rb') as f:
            game_info = pickle.load(f)

        try:
            positions = torch.stack(game_info['Positions']).to(device)
            clocks = torch.zeros((positions.shape[0], 1), dtype=torch.float)
            
            with torch.no_grad():
                _, last = model(positions.unsqueeze(0), clocks.unsqueeze(0), torch.tensor([len(positions)]))
                predictions = last.squeeze().cpu().numpy()
            
            predictions = predictions * ratings_std + ratings_mean
            output.append(predictions.tolist())  # Save both white and black predictions
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")
            # Append default mean ratings if an error occurs
            output.append([mean_rating, mean_rating])
    
    # Write the output to a CSV file
    with open(output_csv_path, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Row', 'White_Prediction', 'Black_Prediction'])  # Header
        for i, row in enumerate(output):
            writer.writerow([i] + row)

    print(f"Predictions saved to {output_csv_path}")

# Example usage
model_path = 'model_55.pth'
data_dir = 'games'
output_csv_path = 'predictions.csv'
load_model_and_save_to_csv(model_path, data_dir, output_csv_path)
