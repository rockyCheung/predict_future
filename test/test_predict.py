from for_future.predict import PredictFuture
import os

def test_saveDataFrame():
    curdir = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(curdir, 'AggregateFinancingtotheRealEconomy.csv')
    predict_future = PredictFuture(file=path)
    predict_future.seeFuture(periods=20, freq='M', include_history=True)
    predict_future.saveDataFrame(curdir)

if __name__ == '__main__':
    test_saveDataFrame()
