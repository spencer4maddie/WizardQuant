import argparse

from FastResearcherData import *
from PicDrawer import *
from PreProcessor import *
from Regression import *
from Evaluate import *

if __name__ == '__main__':

    '''

        python run -f [filepath] -s [filepath] -c [stock code]

    output:
        evaluate : implement by evaluator.run()
        picture : implement by drawer.run()

    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("code", type=str, help="the stock code you want to predict")
    parser.add_argument("label", type=str, help="the attribute you want to predict")
    #  parser.add_argument("expect day", type=str, help="the day you want to predict")
    #   parser.add_argument("his_num", type=int, help="the basis of day you want to predict on")
    # parse.add_argument("-a",type = str,help = "the attribute you want to add"
    # parse.add_argument("-d",type = str,help = "the attribute you want to delete"
    parser.add_argument("method", type=str, help="choose a method for regression prediction",
                        default="NN")
    args = parser.parse_args()
    stock_code = args.code
    expect_tag = args.label
    method = args.method

    stockcodes_list = ['000001']
    filenames_list = ["5min/000001.csv"]

    expect_day = '2018-01-18'
    his_num = 5
    # print(stock_code)

    fast_data_searcher = FastResearchData(stock_code, stockcodes_list, filenames_list)
    stock_data = fast_data_searcher.run()

    # calculator = CalCorrMatrix()
    data_preparer = PreProcessor(stock_data, expect_day, expect_tag, his_num)
    valid_set, train_set, valid_tag, train_tag = data_preparer.run()

    regress = Regression(valid_set, train_set, valid_tag, train_tag, method)
    pred_result = regress.run()

    print(pred_result)

    evaluator = Evaluate( valid_set, valid_tag, pred_result, expect_tag, method)
    evaluator.run()

    drawer = PicDrawer(method, valid_tag, pred_result)
    drawer.picDrawer()
