from sklearn.preprocessing import StandardScaler
import pandas as pd
from IndicatorGallery import *


class PreProcessor(object):
    def __init__(self, stock_data, expect_day, expect_tag, his_num):
        self.stock_data = stock_data
        self.origin_data = pd.DataFrame([])
        self.expect_day = expect_day
        self.expect_tag = expect_tag
        self.tag_dic = {}
        self.his_num = his_num

    def reindex_data(self):
        if not self.stock_data.empty:
            time_split = pd.DataFrame((x.split(' ') for x in self.stock_data.date), columns=['day', 'time'])
            code_data = self.stock_data.drop(['date'], axis=1)
            code_data = pd.concat([time_split, code_data], axis=1)

            self.stock_data = code_data
            # print (self.stock_data)

    def build_vector_data(self):

        data_day = self.stock_data.loc[:, 'day']
        data_label = self.stock_data[self.expect_tag]

        for i in range(self.his_num):
            data_frag = self.stock_data.loc[i + 1:len(data_label), [self.expect_tag]]
            # print (data_frag)
            data_frag = data_frag.reset_index(drop=True)
            self.origin_data[i] = data_frag

        self.origin_data[self.expect_tag] = data_label
        self.origin_data['day'] = data_day
        self.origin_data = self.origin_data[0:len(data_label) - self.his_num]

        self.load_attribute_data()

    '''
        shift for one part 
        data_label = self.stock_data[self.expect_tag]
        self.origin_data = self.stock_data.loc[1:len(data_label)]
         
        self.origin_data['label'] = data_label    
    '''
    # delete X
    def select_attr(self, attr_array):

        attr_array = attr_array.split(',')
        self.origin_data = self.origin_data.drop(columns=attr_array)
        self.origin_data = self.origin_data.drop(columns=self.expect_tag)

    # add X
    def add_attr(self, attr_array):

        attr_array = attr_array.split(',')
        indicator = IndicatorGallery()
        indicator.run()
        for item in attr_array:
            self.origin_data[item] = indicator.get_indicator(item)

    def get_attribute_data(self):

        return self.tag_dic[self.expect_tag]

    def load_attribute_data(self):

        if self.expect_tag not in self.tag_dic.keys():
            self.tag_dic[self.expect_tag] = self.origin_data
        else:
            pd.concat([self.tag_dic[self.expect_tag], self.origin_data])

    def set_divider(self):

        self.origin_data = self.origin_data.set_index(['day'])
        grouped = self.origin_data.groupby('day')

        valid_raw = []
        train_raw = []
        # print (self.origin_data)
        for index, group in grouped:
            if index == self.expect_day:
                valid_raw.append(group)
            elif index < self.expect_day:
                train_raw.append(group)

        valid_raw_new = pd.concat(valid_raw)
        train_raw_new = pd.concat(train_raw)
        valid_tag = valid_raw_new[self.expect_tag]  # label
        valid_tag = valid_tag.to_frame()
        train_tag = train_raw_new[self.expect_tag]  # label
        train_tag = train_tag.to_frame()

        train_set = train_raw_new.drop([self.expect_tag], axis=1)
        valid_set = valid_raw_new.drop([self.expect_tag], axis=1)

        stdsc = StandardScaler()
        valid_set_std = stdsc.fit_transform(valid_set)
        train_set_std = stdsc.fit_transform(train_set)
        train_set_std = pd.DataFrame(data=train_set_std, index=train_set.index)
        valid_set_std = pd.DataFrame(data=valid_set_std, index=valid_set.index)
        return valid_set_std, train_set_std, valid_tag, train_tag

    def run(self):
        self.reindex_data()
        self.build_vector_data()
        # self.select_attribute()
        valid_set, train_set, valid_tag, train_tag = self.set_divider()
        return valid_set, train_set, valid_tag, train_tag


if __name__ == '__main__':
    expect_day = '2018-01-18'
    expect_tag = 'p_change'
    his_num = 5
    data_preparer = PreProcessor(Data, expect_day, expect_tag, his_num)
    valid_set, train_set, valid_tag, train_tag = data_preparer.run()
    print(valid_set)
    print(valid_tag)
    print(train_set)
    print(train_tag)