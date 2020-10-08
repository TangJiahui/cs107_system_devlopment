import numpy as np

class Regression(): 
    def __init__(self):
        self.param = {}

    def get_params(self):
        return self.param

    def set_params(self, **kwargs):
        for i in kwargs:
            self.param[i] = kwargs[i]

    def fit(self, X, y):
        raise NotImplementedError

    def predict(self, X):
        return np.dot(X, self.param["coefficient"]) + self.param["intercept"]

    def score(self, X, y):
        SSE = np.sum((y - self.predict(X))**2)
        SST = np.sum((y - np.mean(y))**2)
        return 1-SSE/SST


class LinearRegression(Regression):
    def fit(self, X, y):
        new_col = np.array([[1]* X.shape[0]]).T
        new_X =  np.append(X, new_col, axis=1)
        best_fit = np.dot(np.dot(np.linalg.pinv(np.dot(new_X.T,new_X)),new_X.T),y)
        self.param["coefficient"] = best_fit[:X.shape[1]]
        self.param["intercept"] = best_fit[X.shape[1]:]


class RidgeRegression(LinearRegression):
    def fit(self, X, y):
        new_col = np.array([[1]* X.shape[0]]).T
        new_X =  np.append(X, new_col, axis=1)
        tao = self.param['alpha'] * np.identity(new_X.shape[1])
        best_fit = np.dot(np.dot(np.linalg.pinv(np.dot(new_X.T, new_X)+np.dot(tao.T, tao)), new_X.T),y)
        self.param["coefficient"] = best_fit[:X.shape[1],]
        self.param["intercept"] = best_fit[X.shape[1]:,]
