import numpy as np
import pandas as pd

class MultipleRegression:

    def __init__(self):
        self.parameters = np.ones((1, 5), dtype=np.float32)

    def fit(self, train_X, train_Y):
        self.parameters = np.matmul(np.matmul(np.linalg.inv(np.matmul(train_X.T, train_X)), train_X.T), train_Y)

if __name__ == "__main__":
    model = MultipleRegression()
    df = pd.read_csv("allfourfactors.csv")
    train_X = df[["EFG_PCT", "FTA_RATE", "TM_TOV_PCT", "OREB_PCT"]]
    train_X = np.concatenate((train_X.to_numpy(), np.ones((89, 1), dtype=np.float32)), axis=1)
    train_Y = df["W_PCT"]
    train_Y = train_Y.to_numpy().reshape((89, 1))
    model.fit(train_X, train_Y)
    print(model.parameters)