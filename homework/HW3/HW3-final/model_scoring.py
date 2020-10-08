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

alpha = 0.1
linreg = LinearRegression()
ridreg = RidgeRegression()
ridreg.set_params(alpha=alpha)
models = [linreg, ridreg]

model_scores = []
for model in models:
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    model_scores.append(score)
    print(str(type(model).__name__)+" has R^2 score of: " + str(score))

best_model = models[model_scores.index(max(model_scores))]
print("The best model is " + str(type(best_model).__name__))
print("And params for the best model are: ")
print(best_model.get_params())