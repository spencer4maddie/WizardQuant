from sklearn import neural_network as nn
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import *
from sklearn.linear_model import *
from sklearn.svm import *


class Regression:

    def __init__(self, valid_set, train_set, valid_tag, train_tag, method='NN'):
        self.method = method
        self.valid_set = valid_set
        self.train_set = train_set
        self.valid_tag = valid_tag
        self.train_tag = train_tag

    def get_method(self):
        if self.method == 'NN':
            regressor = nn.MLPRegressor()
        elif self.method == 'KNN':
            regressor = KNeighborsRegressor()
        elif self.method == 'SVM':
            regressor = SVR()
        elif self.method == 'LR':
            regressor = LinearRegression()
        elif self.method == 'DT':
            regressor = DecisionTreeRegressor()
        elif self.method == 'GBDT':
            regressor = ExtraTreeRegressor()

        return regressor

    def train_and_predict(self):
            regressor = self.get_method()
            train_tag_val = self.train_tag.values.reshape(self.train_tag.values.shape[0], )
            train_tag_val.shape
            regressor.fit(self.train_set.values, train_tag_val)
            valid_pred = regressor.predict(self.valid_set.values)
            print('Score of nn regressor on valid set:{:2f}'.format(
                regressor.score(self.valid_set.values, self.valid_tag.values.reshape(self.valid_tag.shape[0], ))))
            return valid_pred

    def run(self):
        return self.train_and_predict()

