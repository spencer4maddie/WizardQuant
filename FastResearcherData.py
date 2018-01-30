import pandas as pd


class FastResearchData:

    def __init__(self, stock_code, stockcodes_list, filenames_list):
        self.stock_dict = {}
        self.stock_code = stock_code
        self.stockcodes_list = stockcodes_list
        self.filenames_list = filenames_list

    def load_from_data_frame(self, stock_code, stock_data):
        if self.stock_code not in self.stock_dict.keys():
            self.stock_dict[stock_code] = stock_data
        else:  # 可以更新原本有的数据
            pd.concat([self.stock_dict[stock_code], stock_data])

    def load_from_csv(self):

        for (stock_code, filename) in zip(self.stockcodes_list, self.filenames_list):
            stock_data = pd.read_csv(filename)
            data = pd.DataFrame(stock_data)
            self.load_from_data_frame(stock_code, data)

    def get_stock(self):
        if self.stock_code not in self.stockcodes_list:
            print("cannot find!")

        else:
            return self.stock_dict[self.stock_code]

    def run(self):
        self.load_from_csv()
        return self.get_stock()


if __name__ == '__main__':

    stockcodes_list = ['000001']
    filenames_list = ["5min/000001.csv"]
    stockcode = '000001'
    fast_data_sercher = FastResearchData(stockcode, stockcodes_list, filenames_list)
    Data = fast_data_sercher.run()
