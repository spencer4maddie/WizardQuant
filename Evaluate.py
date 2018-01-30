import pandas as pd


class Evaluate:

    def __init__(self, valid_set, valid_tag, pred_result, expect_tag, method='NN'):
        self.method = method
        self.valid_set = valid_set
        self.valid_tag = valid_tag
        self.pred_result = pred_result
        self.expect_tag = expect_tag

    def get_score(self):

        if self.method == 'NN':
            # regressor = nn.MLPRegressor()

            self.valid_pred = pd.DataFrame(self.pred_result)
            self.valid_pred.columns = [self.expect_tag]
            self.valid_tag = self.valid_tag.reset_index(drop=True)
            erro = self.valid_tag - self.valid_pred
            erro = erro * erro
            s = erro.sum()
            mse = s / erro.size
            print('MSE of nn regressor on valid set : ', mse)

    def run(self):
        self.get_score()
