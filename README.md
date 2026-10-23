# chess-rating-predictor-dl

**Detecting Cheating in Online Chess: A Hybrid Approach Using CNN-LSTM and XGBoost for Identifying Computer Assistance**

Final project for CSAC 212: Introduction to Artificial Intelligence, College of Computer Studies, Camarines Sur Polytechnic Colleges (2024). The report is [`FP_Bacsain_Jave_BSCS2A.pdf`](FP_Bacsain_Jave_BSCS2A.pdf). The code and its outputs are in [`FP_Bacsain_Jave_BSCS2A.ipynb`](FP_Bacsain_Jave_BSCS2A.ipynb).

## Project

The data is the Kaggle "Spotting Cheaters: Chess cheating dataset" (`Games.csv`). Its games were played between bots, and each move came from either Stockfish (a cheat move) or Maia (a human-like move). The report frames the project as cheat detection. In the notebook, the XGBoost classifier predicts the game result (0 White win, 1 Black win, 2 draw) from predicted ratings, listed Elo ratings and the number of cheat moves by each side.

## Methodology

1. `gameprocessor.py` converts each game to UCI moves with python-chess and saves the board before each move as a 12x8x8 tensor in `games/<row>.pkl`. These files are large and are not in the repo.
2. `rating_prediction.py` loads `model_55.pth`, the pre-trained CNN-LSTM rating model from Omori & Tadepalli (2024), and predicts a rating for White and Black in each game. The model is used for prediction only and is not trained here. `Games.csv` has no clock times, so the clock input is all zeros. The output is `predictions.csv`.
3. The notebook joins `predictions.csv` and `Games.csv` by row into `combined_data.csv`, turns `Score` into the `result` label, replaces the per-move cheat flags with counts, and drops `Score`, `Game` and `Row`. This leaves 48,932 games, 6 features and no missing values.
4. 80/20 train/test split (`random_state=42`), then `XGBClassifier` with `max_depth=7`, `learning_rate=0.05`, `subsample=0.7`, `reg_alpha=1` and `reg_lambda=1`. The report lists `n_estimators=100`. Notebook cell 28 has `n_estimators=1`.

## Results

Accuracy is 0.69 on the 9,787-game test split. Draws are the weak class (recall 0.14).

| Class | Precision | Recall | F1-score | Support |
|---|---|---|---|---|
| 0 (White win) | 0.64 | 0.83 | 0.72 | 3905 |
| 1 (Black win) | 0.74 | 0.76 | 0.75 | 4205 |
| 2 (Draw) | 0.79 | 0.14 | 0.24 | 1677 |
| Weighted avg | 0.71 | 0.69 | 0.65 | 9787 |

Source: the notebook's "Training and Evaluation" section and Section 5.1 of the report.

- Of the 1677 draws, 912 were predicted as a White win and 526 as a Black win. The report puts this down to class imbalance.
- The two predicted ratings have a correlation of r = 1.00. The report says they may provide similar or redundant information.
- The notebook also prints `Validation Accuracy: 0.6824`. That cell and the model cell with `n_estimators=1` ran last (execution counts 119 and 120). The table and the confusion matrix come from cells run earlier (execution counts 93 and 92), so the two numbers come from different runs.

## How to Run

The notebook reads `predictions.csv` and `Games.csv`, which are both in this repo.

```bash
pip install pandas numpy seaborn matplotlib scikit-learn xgboost ydata-profiling AutoLogging-ML jupyter
jupyter notebook FP_Bacsain_Jave_BSCS2A.ipynb
```

Rebuilding `predictions.csv` also needs PyTorch, python-chess and `chess_rating_net.py` from [RatingNet](https://github.com/AstroBoy1/RatingNet). That file is not in this repo.

## References

- Omori, M., & Tadepalli, P. (2024). Chess Rating Estimation from Moves and Clock Times Using a CNN-LSTM. arXiv:2409.11506. Code: https://github.com/AstroBoy1/RatingNet
- Spotting Cheaters: Chess cheating dataset. (2024, April 1). Kaggle. https://www.kaggle.com/datasets/brieucdandoy/chess-cheating-dataset/data

## License

MIT. See [LICENSE](LICENSE).
