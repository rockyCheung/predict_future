from for_future.predict import PredictFuture
import os
from for_future.stock.stockdata import StockData
from datetime import *
import pandas as pd

def test_saveDataFrame():
    curdir = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(curdir, 'sample/predict_2019-06-18 13:21:44.369742.csv')
    predict_future = PredictFuture(file=path)
    predict_future.seeFuture(periods=20, freq='D', include_history=True)
    predict_future.saveDataFrame(curdir)

def test_stock_predict():
    stock_code = '002792'
    obj = StockData(stock_code)  # 创建股票交易类对象
    data = obj.history(start='2016-03-28', end='2019-06-19')  # 获取浦发银行2019年1月份的历史数据
    ds = {'ds':data['date'],'y':data['close'] ,'cap':data['high'] , 'floor':data['low'], 'low':data['low']}
    predict_data = pd.DataFrame(ds)
    #保存查询数据到csv文件
    curdir = os.path.abspath(os.path.dirname(__file__))
    generate_file_name = lambda name: 'predict_' + name + '(' +stock_code+ ')' + '.csv'
    svaeFile = os.path.join(curdir, generate_file_name(str(datetime.now())))
    predict_data.to_csv(svaeFile, index=False, header=False)
    #预测数据
    predict_future = PredictFuture(growth='logistic',data_frame=predict_data)
    predict_future.seeFuture(periods=200, freq='D', include_history=True)
    predict_future.drawForecast()
    predict_future.drawTrend()

    #
    # predict_future.saveDataFrame(curdir)
    # print(data)
    # obj.output()  # 输出结果
def test_money_supply():
    curdir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(curdir,'sample/money_supply.csv')
    data = pd.read_csv(file_path)
    ds = {'ds':data['time'],'y':data['M2']}
    predict_data = pd.DataFrame(ds)
    # 预测数据
    predict_future = PredictFuture(data_frame=predict_data)
    predict_future.seeFuture(periods=18, freq='M', include_history=True)
    predict_future.drawForecast()
    predict_future.drawTrend()

def checkCapFloor(a, b):
    if a<=b:
        return 0
    else:
        return b
if __name__ == '__main__':
    # test_saveDataFrame()
    test_stock_predict()
    # test_money_supply()
