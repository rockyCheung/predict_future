# -*- coding:utf-8 -*-
import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt
import os
from for_future import logger
import click
from datetime import *

class PredictFuture(Prophet):
    def __init__(self,
            growth='linear',
            changepoints=None,
            n_changepoints=25,
            changepoint_range=0.8,
            yearly_seasonality='auto',
            weekly_seasonality='auto',
            daily_seasonality='auto',
            holidays=None,
            seasonality_mode='additive',
            seasonality_prior_scale=10.0,
            holidays_prior_scale=10.0,
            changepoint_prior_scale=0.05,
            mcmc_samples=0,
            interval_width=0.80,
            uncertainty_samples=1000,file=''):

        self._file = file
        if not os.path.exists(file):
            curdir = os.path.abspath(os.path.dirname(__file__))
            self._file = os.path.join(curdir, file)
        if os.access(self._file, os.R_OK):
            self._df = pd.read_csv(self._file)
            self._df.head()
        else:
            raise Exception('Can\'t found the file %s',self._file)
        super().__init__(growth,
              changepoints,
              n_changepoints,
              changepoint_range,
              yearly_seasonality,
              weekly_seasonality,
              daily_seasonality,
              holidays,
              seasonality_mode,
              seasonality_prior_scale,
              holidays_prior_scale,
              changepoint_prior_scale,
              mcmc_samples,
              interval_width,
              uncertainty_samples)

    def seeFuture(self,periods, freq, include_history):
        # 训练模型
        self.fit(self._df)
        # 构建待预测日期数据框，periods = 365 代表除历史数据的日期外再往后推 365 天
        self._future = self.make_future_dataframe(periods, freq, include_history)
        predict_set = self._future.tail()
        logger.info(
            '\n##################################################################构建预测集-start##############################################################################')
        logger.info(predict_set)
        logger.info(
            '\n##################################################################构建预测集-end##############################################################################')
        # 进行预测
        self._forecast = self.predict(self._future)

    def getTopTail(self, top):
        forecast_set = self._forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(top)
        return forecast_set

    def drawForecast(self):
        # 展示预测结果
        self.plot(self._forecast);
        plt.show()
    def drawTrend(self):
        # 预测的成分分析绘图，展示预测中的趋势、周效应和年度效应
        self.plot_components(self._forecast);
        plt.show()
    def saveDataFrame(self,path):
        generate_file_name = lambda name:'predict_'+ name + '.csv'
        svaeFile = os.path.join(path, generate_file_name(str(datetime.now())))
        self._forecast.to_csv(svaeFile , index=False, header=False)

'''
freq :
    A number of string aliases are given to useful common time series frequencies. We will refer to these aliases as offset aliases.
                                                                                               'B	business day frequency'
                                                                                               'C	custom business day frequency'
                                                                                               'D	calendar day frequency'
                                                                                               'W	weekly frequency'
                                                                                               'M	month end frequency'
                                                                                               'SM	semi-month end frequency (15th and end of month)'
                                                                                               'BM	business month end frequency'
                                                                                               'CBM	custom business month end frequency'
                                                                                               'MS	month start frequency'
                                                                                               'SMS	semi-month start frequency (1st and 15th)'
                                                                                               'BMS	business month start frequency'
                                                                                               'CBMS	custom business month start frequency'
                                                                                               'Q	quarter end frequency'
                                                                                               'BQ	business quarter end frequency'
                                                                                               'QS	quarter start frequency'
                                                                                               'BQS	business quarter start frequency'
                                                                                               'A, Y	year end frequency'
                                                                                               'BA, BY	business year end frequency'
                                                                                               'AS, YS	year start frequency'
                                                                                               'BAS, BYS	business year start frequency'
                                                                                               'BH	business hour frequency'
                                                                                               'H	hourly frequency'
                                                                                               'T, min	minutely frequency'
                                                                                               'S	secondly frequency'
                                                                                               'L, ms	milliseconds'
                                                                                               'U, us	microseconds'
                                                                                               'N	nanoseconds'
'''
@click.command()
@click.option('--top', prompt=False,
              help='Print predict result top {top} lines.', type=int)
@click.option('--draw_forecast',type=bool, is_flag=False , prompt=False,
              help='Draw forecast line.True is draw,default False.')
@click.option('--draw_trend', type=bool , is_flag=False , prompt=False,
              help='Draw trend line.True is draw,default False.')
@click.option('--save', type=str , prompt=False,
              help='Save result path.')
@click.option('--hd', type=bool , is_flag=False , prompt=False,
              help='Show the help detail.')
def predict(top,draw_forecast,draw_trend,save,hd):
    path = click.prompt('Please enter sample CSV file path', type=str)
    freq = click.prompt('Please enter freq,freq choice [M,D,3M,5D,H...]', type=str)
    periods = click.prompt('Please enter periods', type=int)  
    include_history = click.confirm('Whether or not include history?')
    
    # if sys.argv.__len__() > 1:
    #     path = sys.argv[1]
    # if sys.argv.__len__() > 2:
    #     freq = sys.argv[2]
    # if sys.argv.__len__() > 3:
    #     periods = sys.argv[3]
    # if sys.argv.__len__() > 4:
    #     include_history = sys.argv[4]
    # 定义拟合模型
    predict_future = PredictFuture(file=path)
    # 构建待预测日期数据框，periods = 365 代表除历史数据的日期外再往后推 365 天
    predict_future.seeFuture(periods, freq, include_history)
    if top:
        forecast_set = predict_future.getTopTail(top)
        logger.info('the forecast_set %s',forecast_set)
    if draw_forecast and click.confirm('Do you want to show forecast line?'):
        predict_future.drawForecast()
    if draw_trend and click.confirm('Do you want to show trend line?'):
        predict_future.drawTrend()
    if save:
        predict_future.saveDataFrame(save)
    if hd:
        click.echo('Prediction is a time series prediction model, which can be trained according to the set sample data, and the prediction results are given according to the given frequency and period.')
        click.echo('Description of parameters:')
        click.echo('  path: The path instruction needs to specify the sample path. The sample data must be in CSV format. The sample includes DS and Y columns. DS indicates the time of data acquisition. y is the corresponding data value.')
        click.echo('  freq: Freq refers to the frequency of prediction. For example, M represents monthly prediction, D represents daily prediction, H represents hours, and 3D represents three days.')
        click.echo('  periods: Periodods are the prediction period, freq is D, which is marked by the last time point of the sample, then pushed back the periods day for prediction, and M is pushed back the periods month for prediction.')
        click.echo('  include_history: Does it include holidays?')
        click.echo('Option:')
        click.echo('  top: For any integer, the top information identifying the predicted data set is printed to the log')
        click.echo('  draw_forecast: For bool type, whether to draw predictive curve or not')
        click.echo('  draw_trend: For bool type, whether to draw the trend of key indicators')