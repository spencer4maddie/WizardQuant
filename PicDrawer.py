import matplotlib.pyplot as plt
class PicDrawer:

    def __init__(self, method='NN', valid_tag=[], valid_pred=[]):
        self.method = method
        self.valid_tag = valid_tag
        self.valid_pred = valid_pred

    def picDrawer(self):
            # %matplotlib inline
            plt.figure()
            plt.plot(self.valid_pred, 'g')
            plt.plot(self.valid_tag.values, 'b')
            plt.show()
