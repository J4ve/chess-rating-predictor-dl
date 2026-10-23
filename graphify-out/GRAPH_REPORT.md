# Graph Report - chess-rating-predictor-dl  (2026-10-23)

## Corpus Check
- Large corpus: 500 files · ~680,437 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder.

## Summary
- 56 nodes · 79 edges · 6 communities
- Extraction: 95% EXTRACTED · 4% INFERRED · 1% AMBIGUOUS · INFERRED: 3 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Spotting Cheaters: Chess Cheating
- gameprocessor.py
- xgboost_model (XGBClassifier, n_estimators=1)
- Online Chess Cheat Detection
- rating_prediction.py
- game_analysis.py

## God Nodes (most connected - your core abstractions)
1. `Spotting Cheaters: Chess Cheating Dataset (Kaggle, Games.csv, ~48k bot games)` - 10 edges
2. `CNN-LSTM Rating Estimator (pre-trained, Omori & Tadepalli)` - 8 edges
3. `Online Chess Cheat Detection (computer/engine assistance)` - 7 edges
4. `parse_uci_moves_to_game()` - 6 edges
5. `XGBoost Classifier` - 6 edges
6. `xgboost_model (XGBClassifier, n_estimators=1)` - 6 edges
7. `process_csv()` - 5 edges
8. `FP_Bacsain_Jave_BSCS2A.pdf - Detecting Cheating in Online Chess: Hybrid CNN-LSTM + XGBoost (paper)` - 5 edges
9. `Board-State Pickle Files (games/ directory, ~13 GB)` - 5 edges
10. `Evaluation Results (accuracy 0.69, validation 0.6824, confusion matrix, precision/recall/F1)` - 5 edges

## Surprising Connections (you probably didn't know these)
- `result target label (0 white win, 1 black win, 2 draw)` --conceptually_related_to--> `Online Chess Cheat Detection (computer/engine assistance)`  [AMBIGUOUS]
  FP_Bacsain_Jave_BSCS2A.ipynb.md → FP_Bacsain_Jave_BSCS2A.pdf
- `FP_Bacsain_Jave_BSCS2A.ipynb (chess cheating detection notebook)` --conceptually_related_to--> `FP_Bacsain_Jave_BSCS2A.pdf - Detecting Cheating in Online Chess: Hybrid CNN-LSTM + XGBoost (paper)`  [INFERRED]
  FP_Bacsain_Jave_BSCS2A.ipynb.md → FP_Bacsain_Jave_BSCS2A.pdf
- `model_55.pth (pre-trained CNN-LSTM weights)` --implements--> `CNN-LSTM Rating Estimator (pre-trained, Omori & Tadepalli)`  [EXTRACTED]
  FP_Bacsain_Jave_BSCS2A.ipynb.md → FP_Bacsain_Jave_BSCS2A.pdf
- `xgboost_model (XGBClassifier, n_estimators=1)` --implements--> `XGBoost Hyperparameters (max_depth 7, lr 0.05, subsample 0.7, reg_alpha 1, reg_lambda 1, n_estimators 100)`  [INFERRED]
  FP_Bacsain_Jave_BSCS2A.ipynb.md → FP_Bacsain_Jave_BSCS2A.pdf
- `read_csv()` --shares_data_with--> `Spotting Cheaters: Chess Cheating Dataset (Kaggle, Games.csv, ~48k bot games)`  [EXTRACTED]
  FP_Bacsain_Jave_BSCS2A.ipynb.md → FP_Bacsain_Jave_BSCS2A.pdf

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Hybrid CNN-LSTM -> XGBoost cheat-detection data pipeline** — chess_rating_predictor_dl_fp_bacsain_jave_bscs2a_chess_cheating_dataset, chess_rating_predictor_dl_fp_bacsain_jave_bscs2a_board_state_pickle_files, chess_rating_predictor_dl_fp_bacsain_jave_bscs2a_ipynb_model_55_pth, chess_rating_predictor_dl_fp_bacsain_jave_bscs2a_ipynb_predictions_csv, chess_rating_predictor_dl_fp_bacsain_jave_bscs2a_ipynb_combined_data_csv, chess_rating_predictor_dl_fp_bacsain_jave_bscs2a_ipynb_xgboost_model [EXTRACTED 1.00]

## Communities (6 total, 0 thin omitted)

### Community 0 - "Spotting Cheaters: Chess Cheating"
Cohesion: 0.18
Nodes (14): Board-State Pickle Files (games/ directory, ~13 GB), Spotting Cheaters: Chess Cheating Dataset (Kaggle, Games.csv, ~48k bot games), CNN-LSTM Rating Estimator (pre-trained, Omori & Tadepalli), Donahue et al. (2014) Long-term Recurrent Convolutional Networks, Elo Rating System, Hochreiter & Schmidhuber (1997) Long Short-Term Memory, FP_Bacsain_Jave_BSCS2A.ipynb (chess cheating detection notebook), Lichess Open Database (+6 more)

### Community 1 - "gameprocessor.py"
Cohesion: 0.24
Nodes (12): algebraic_to_uci(), board_to_array(), clean_uci_moves(), parse_game(), parse_uci_moves_to_game(), process_csv(), Parses game object to extract evaluations, clocks, and positions., Converts a chess board into a 12-layer 8x8 tensor representing the piece… (+4 more)

### Community 2 - "xgboost_model (XGBClassifier, n_estimators=1)"
Cohesion: 0.21
Nodes (10): Chen & Guestrin (2016) XGBoost: A Scalable Tree Boosting System, Class Imbalance (draw class: recall 0.14), Evaluation Results (accuracy 0.69, validation 0.6824, confusion matrix, precision/recall/F1), Cheat-count features (Liste cheat white/black -> number of flagged moves), combined_data.csv (predictions + Games.csv row-aligned), result target label (0 white win, 1 black win, 2 draw), xgboost_model (XGBClassifier, n_estimators=1), Supervised Learning (+2 more)

### Community 3 - "Online Chess Cheat Detection"
Cohesion: 0.29
Nodes (7): FP_Bacsain_Jave_BSCS2A.pdf - Detecting Cheating in Online Chess: Hybrid CNN-LSTM + XGBoost (paper), Barnes & Hernandez-Castro (2014) On the Limits of Engine Analysis for Cheating Detection in Chess, Chess.com (2022) Hans Niemann Report, CSAC 212 - Introduction to Artificial Intelligence (course), Online Chess Cheat Detection (computer/engine assistance), Prajapati (2024) Data Cleaning + Auto-EDA + XGBoost Kaggle notebook (~70%), Regan - Fraught Issues in Statistical Chess Cheating Detection (ROI, z-scores)

### Community 4 - "rating_prediction.py"
Cohesion: 0.33
Nodes (4): Feature Correlation Analysis (White/Black Prediction r=1.00 redundancy), model_55.pth (pre-trained CNN-LSTM weights), predictions.csv (CNN-LSTM Elo predictions: White/Black Prediction), read_csv()

### Community 5 - "game_analysis.py"
Cohesion: 0.83
Nodes (3): calculate_mae(), load_model_and_sample_games_to_txt(), save_game_to_txt()

## Ambiguous Edges - Review These
- `Online Chess Cheat Detection (computer/engine assistance)` → `result target label (0 white win, 1 black win, 2 draw)`  [AMBIGUOUS]
  FP_Bacsain_Jave_BSCS2A.ipynb.md · relation: conceptually_related_to

## Knowledge Gaps
- **11 isolated node(s):** `UCI (Universal Chess Interface) notation/protocol`, `Stockfish Chess Engine (alpha-beta minimax)`, `CSAC 212 - Introduction to Artificial Intelligence (course)`, `Chen & Guestrin (2016) XGBoost: A Scalable Tree Boosting System`, `Hochreiter & Schmidhuber (1997) Long Short-Term Memory` (+6 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 20 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Online Chess Cheat Detection (computer/engine assistance)` and `result target label (0 white win, 1 black win, 2 draw)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `Online Chess Cheat Detection (computer/engine assistance)` connect `Online Chess Cheat Detection` to `Spotting Cheaters: Chess Cheating`, `xgboost_model (XGBClassifier, n_estimators=1)`?**
  _High betweenness centrality (0.263) - this node is a cross-community bridge._
- **Why does `Spotting Cheaters: Chess Cheating Dataset (Kaggle, Games.csv, ~48k bot games)` connect `Spotting Cheaters: Chess Cheating` to `gameprocessor.py`, `Online Chess Cheat Detection`, `rating_prediction.py`?**
  _High betweenness centrality (0.258) - this node is a cross-community bridge._
- **Why does `FP_Bacsain_Jave_BSCS2A.pdf - Detecting Cheating in Online Chess: Hybrid CNN-LSTM + XGBoost (paper)` connect `Online Chess Cheat Detection` to `Spotting Cheaters: Chess Cheating`?**
  _High betweenness centrality (0.221) - this node is a cross-community bridge._
- **What connects `UCI (Universal Chess Interface) notation/protocol`, `Stockfish Chess Engine (alpha-beta minimax)`, `CSAC 212 - Introduction to Artificial Intelligence (course)` to the rest of the system?**
  _11 weakly-connected nodes found - possible documentation gaps or missing edges._