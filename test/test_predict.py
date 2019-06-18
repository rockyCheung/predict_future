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
    stock_code = '600519'
    obj = StockData(stock_code)  # 创建股票交易类对象
    data = obj.history(start='2001-08-27', end='2019-06-17')  # 获取浦发银行2019年1月份的历史数据
    ds = {'ds':data['date'],'y':data['close']}
    predict_data = pd.DataFrame(ds)
    #保存查询数据到csv文件
    curdir = os.path.abspath(os.path.dirname(__file__))
    generate_file_name = lambda name: 'predict_' + name + '(' +stock_code+ ')' + '.csv'
    svaeFile = os.path.join(curdir, generate_file_name(str(datetime.now())))
    predict_data.to_csv(svaeFile, index=False, header=False)
    #预测数据
    predict_future = PredictFuture(data_frame=predict_data)
    predict_future.seeFuture(periods=200, freq='D', include_history=True)
    predict_future.drawForecast()
    predict_future.drawTrend()
    #
    # predict_future.saveDataFrame(curdir)
    # print(data)
    # obj.output()  # 输出结果

if __name__ == '__main__':
    # test_saveDataFrame()
    test_stock_predict()
