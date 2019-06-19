# 时间序列模型

predict 是一个时间序列预测模型，可以根据设定的样本数据进行训练，并根据给定的频度和周期给出预测结果

## 参数说明

* path 运行指令需要指定样本路径，样本数据必须是CSV格式，样本包括ds,y两列，ds标识数据采集时间，y为对应数据值

* freq 是指预测的频度，例如M代表以月为单位进行预测，D代表以日为单位进行预测，H代表小时，3D代表3天为单位，更为详细的说明请参见下表：

|标识|含义|
|:---|:---:|
|B	|business day frequency|
|C	|custom business day frequency|
|D	|calendar day frequency|
|W	|weekly frequency|
|M	|month end frequency|
|SM	|semi-month end frequency (15th and end of month)|
|BM	|business month end frequency|
|CBM|	custom business month end frequency|
|MS	|month start frequency|
|SMS|	semi-month start frequency (1st and 15th)|
|BMS|	business month start frequency|
|CBMS|	custom business month start frequency|
|Q	|quarter end frequency|
|BQ	|business quarter end frequency|
|QS	|quarter start frequency|
|BQS|	business quarter start frequency|
|A, Y|	year end frequency|
|BA, BY|	business year end frequency|
|AS, YS|	year start frequency|
|BAS, BYS|	business year start frequency|
|BH|	business hour frequency|
|H	|hourly frequency|
|T, min|	minutely frequency|
|S	|secondly frequency|
|L, ms|	milliseconds|
|U, us|	microseconds|
|N  |nanoseconds|

* periods 是预测周期，freq为D则标识以样本最后一个时点为始，再往后推periods天进行预测，为M则往后推periods月进行预测

* include_history 是否包括节假日

* growth 可以选择输入logistic或linear

## option

* top

为任意整数，标识预测数据集的前top条信息打印到日志中
* draw_forecast

为bool型，是否绘画预测曲线
* draw_trend

为bool型，是否绘画关键指标趋势

## 运行样本集
以社会融资规模增量样本AggregateFinancingtotheRealEconomy.csv为例
```
$ predict --draw_forecast True

Please enter sample CSV file path:data/AggregateFinancingtotheRealEconomy.csv
Please enter freq,freq choice [M,D,3M,5D,H...]: M
Please enter periods: 10
Whether or not include history? [y/N]: y
Do you want to show forecast line? [y/N]: y
```
## 预测结果

### 社会融资规模增量趋势预测

* 预测结果图示

![预测结果](static/Figure_1.png)

* 预测结果趋势以及周期效应

![预测结果](static/Figure_2.png)

### 托邦股份未来200天股票走势

* 上市到2019年6月17日股价变动数据

sample/predict_2019-06-18 14:10:14.090169(002139).csv

* 预测结果图示

![预测结果](static/Figure_3.png)

* 预测结果趋势以及周期效应

![预测结果](static/Figure_4.png)

### 红宝丽未来200天股票走势

* Linear Regression预测结果图示

![预测结果](static/Figure_5.png)

* Logistic Regression预测结果图示

![预测结果](static/Figure_21.png)

* Linear Regression预测结果趋势以及周期效应

![预测结果](static/Figure_6.png)

* Logistic Regression预测结果趋势以及周期效应

![预测结果](static/Figure_22.png)

### 贵州茅台未来200天股票走势

* Linear Regression预测结果图示

![预测结果](static/Figure_7.png)

* Logistic Regression预测结果图示

![预测结果](static/Figure_19.png)

* Linear Regression预测结果趋势以及周期效应

![预测结果](static/Figure_8.png)

* Logistic Regression预测结果趋势以及周期效应

![预测结果](static/Figure_20.png)

### 三一重工未来200天股票走势

* Linear Regression预测结果图示

![预测结果](static/Figure_9.png)

* Logistic Regression预测结果图示

![预测结果](static/Figure_17.png)

* Linear Regression预测结果趋势以及周期效应

![预测结果](static/Figure_10.png)

* Logistic Regression预测结果趋势以及周期效应

![预测结果](static/Figure_18.png)




### 国家货币供给情况分析

#### M0未来18个月的走势预测

* 预测结果图示

![预测结果](static/Figure_11.png)

* 预测结果趋势以及周期效应

![预测结果](static/Figure_12.png)

* 结果分析

通常如果按照目前微信支付、支付宝支付等多种移动非现金支付发展情况来看，理论上M0应该有明显的减少，而数据显示一直在稳定增长，我觉得至少说明了一个问题：央行对非现金支付这一现象还没有给予足够的重视～

#### M1未来18个月的走势预测

* 预测结果图示

![预测结果](static/Figure_13.png)

* 预测结果趋势以及周期效应

![预测结果](static/Figure_14.png)

#### M2未来18个月的走势预测

* 预测结果图示

![预测结果](static/Figure_15.png)

* 预测结果趋势以及周期效应

![预测结果](static/Figure_16.png)

