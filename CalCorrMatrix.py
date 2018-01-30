import os
import pandas as pd


class CalcCorrMatrix(object):
    def __init__(self):
        self.file_path = "../data/"

    def run(self):
        corr_pairs = []
        stock_panel = self.readfiles(self.filepath)

        stock_panel = self.del_empty_frame(stock_panel)

        # calculate correlations, return the correlations of stock_code
        key = ['p_change']
        for key_iter in range(len(key)):
            compare = []
            for item, value in stock_panel.iteritems():
                compare.append(value[key[key_iter]].tolist())
            compare_frame = pd.DataFrame(compare)
            compare_frame = compare_frame.transpose()
            corr = compare_frame.corr()
            corr = pd.DataFrame(corr.values, index=stock_panel.items, columns=stock_panel.items)

        return corr

    def readfiles(self):
        path = os.walk(self.filepath)
        root = ""
        files = []
        for root_path, dirs, contained_files in path:
            root = root_path
            files = contained_files

        stock_dict = {}
        for one_file in files:
            stock_data = pd.read_csv(root + '/' + one_file)
            if stock_data.empty:
                continue
            stock_code = one_file.split('.')[0]
            date = stock_data['time']
            stock_data = stock_data.drop(['time'], axis=1)
            stock_data = pd.DataFrame(stock_data.values, index=date)
            stock_dict[stock_code] = stock_data
        stock_panel = pd.Panel(stock_dict)

        return stock_panel

    def del_empty_frame(self, stock_panel):
        # delete empty data
        for item, value in stock_panel.iteritems():
            stock_frame = stock_panel[item]
            stock_frame = stock_frame.dropna(axis=1, how='all')
            if len(stock_frame.columns) == 0:
                stock_panel = stock_panel.drop([item], axis=0)

        return stock_panel