import pandas as pd
import cntalib
from sklearn.preprocessing import StandardScaler


class IndicatorGallery(object):

    def __init__(self, stock_data):
        self.stock_data = stock_data
        self.indicator_dic = {}

    def load_indicator(self, indicator_type, indicated_data):
        if indicator_type not in self.indicator_dic.keys():
            self.indicator_dic[indicator_type] = indicated_data
        else:
            pd.concat([self.indicator_dic[indicator_type], indicated_data])

    def cal_std(self):

        stdsc = StandardScaler()
        stdsc.fit(self.stock_data)
        std = stdsc.var_
        self.load_indicator(indicator_type='std', indicated_data=std)

    def cal_avg_prc(self):
        indicator_type = 'AvgPrc'
        data_price = self.stock_data['price']

        data_mean = data_price.mean()
        data_avg_prc = data_mean['price']
        self.load_indicator(indicator_type, data_avg_prc)

    def cal_ema(self):
        # ema close short 与 ema close long 两种
        # ema(short) = ema[i-1] * 11/13 + close * 2/13
        # ema(long) = ema[i-1] *25/27 + close * 2/27
        cntalib.df_EMA()
        

    def cal_macd(self):
        # macd = 2 * (dif - dea)
        macd = 2 * (self.indicator_dic['dif']-self.indicator_dic['dea'])
        self.load_indicator(indicator_type='macd', indicated_data=macd)

    def cal_dif(self):
        # dif = short ema - long ema
        dif = self.indicator_dic['shortEMA'] - self.indicator_dic['longEMA']
        self.load_indicator(indicator_type='dif', indicated_data=dif)

    def cal_boll(self):
        pass

    def cal_sar(self):
        pass

    def cal_macd(self):
        pass

    def cal_kdj(self):
        pass

    def cal_dmi(self):
        pass

    def cal_rsi(self):
        pass

    def cal_cci(self):
        pass

    def cal_cr(self):
        pass

    def cal_mtm(self):
        pass

    def cal_mtm(self):
        pass

    def arbr(self):
        pass

    def get_indicator(self, indicator_index):
        return self.indicator_dic[indicator_index]

    def run(self):
        pass

