# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

stockcodeslist = ['000001']
filenameslist = ["5min/000001.csv"]
decision_attribute = "price_change"
frData = FastResearchData()
frData.loadFromCSV(stockcodeslist, filenameslist)
stock = frData.run()

dataset = DatasetPreProcessing(stock)
dataset.correctDataset(decision_attribute)


Class read(self):

        
 def loadFromDataFrame(self, data):
        '''
            直接读取df
        '''


def loadFromCSV(self, stockcodes_list, filenames_list):
        """
            加载csv:使用pandas
        """
        for (stockcode, filename) in zip(stockcodes_list, filenames_list):
            data = pd.read_csv(filename)  
            data = DataFrame(data)
            self.loadFromDataFrame(stockcode, data)
            
 def getStock(self):
        """
            返回某只股票
        """
        return self.stock_dict[self.stock_code]
def run (self,stock_code):
    self.loadFromCSV(stockcodes_list, filenames_list)
    return self.getStock(stock_code)

class CreateDataSet:
def __init__(self, stock_data,tag_name):
        self.stock_data = stock_data
        self.attribute_dict = {}
        self.tag_name = tag_name
    
def loadAttribute(self, attriname, df):
        if attriname not in self.attributedict.keys():
            self.attribute_dict[attriname] = df
        else:
            pd.concat([self.attribute_dict[attriname], df])
            
 def buildDataset(self, tag_name):
       
     dataset = Dataframe([])
        data_label = self.stock_data[tag_name]
        for i in range (0: his_num-1)
            data_frag = stock_data[i+1:len(data_label)]    
            data_frag = data_frag.reset_index(drop=True)
            data_attr = dataset.join(data_frag)
                  
        data_attr = data_set.join(data_label)
        data_attr = data_attr [0:len(data_label)-his_num]
        self.loadAttribute(tag_name, dataset)
        return dataset
def getDataset(self, tag_name):
        return self.attributedict[tag_name]
    

