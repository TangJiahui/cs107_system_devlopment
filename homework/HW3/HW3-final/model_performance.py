import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
#import regression classes
from Regression import Regression
from Regression import LinearRegression
from Regression import RidgeRegression

dataset = datasets.load_boston()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'], 
                                                    dataset['target'], 
                                                    test_size=0.2, 
                                                    random_state=42)


linreg_score = []
ridreg_score = []
alphas = np.arange(0.01, 10.11, 0.1)

for i in alphas:
    linreg = LinearRegression()
    ridreg = RidgeRegression()
    ridreg.set_params(alpha=i)
    models = [linreg, ridreg]
    for model in models:
        model.fit(X_train, y_train)
        if model.__class__.__name__ == "LinearRegression":
            linreg_score.append(model.score(X_test, y_test))
        else:
            ridreg_score.append(model.score(X_test, y_test))


## plotting 
plt.figure(figsize=(10,7))
plt.plot(alphas,linreg_score)
plt.plot(alphas,ridreg_score)
plt.xlabel("alpha")
plt.ylabel("model $R^2$ scores")
plt.legend(["Linear Regression", "Ridge Regression"])
plt.title("Model Performance w.r.t to various Alpha Value")
plt.savefig('P2F.png')