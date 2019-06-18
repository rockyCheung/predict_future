# -*- coding:utf-8 -*-
"""
地址&配置
Created on 2018/12/26
@author: TabQ
@group : gugu
@contact: 16621596@qq.com
"""

HOLIDAY_URL = 'http://timor.tech/api/holiday/info/%s'
K_LABELS = ['D', 'W', 'M']
K_MIN_LABELS = ['5', '15', '30', '60']
K_TYPE = {'D': 'akdaily', 'W': 'akweekly', 'M': 'akmonthly'}
TT_K_TYPE = {'D': 'day', 'W': 'week', 'M': 'month'}
FQ_KEY = ['qfqday', 'hfqday', 'day']
INDEX_LABELS = ['sh', 'sz', 'hs300', 'sz50', 'cyb', 'zxb', 'zx300', 'zh500']
INDEX_LIST = {'sh': 'sh000001', 'sz': 'sz399001', 'hs300': 'sz399300',
              'sz50': 'sh000016', 'zxb': 'sz399005', 'cyb': 'sz399006', 'zx300': 'sz399008', 'zh500':'sh000905'}
P_TYPE = {'http': 'http://', 'ftp': 'ftp://'}
PAGE_NUM = [40, 60, 80, 100]
FORMAT = lambda x: '%.2f' % x
FORMAT4 = lambda x: '%.4f' % x
INDEX_ETF_URL = 'https://www.jisilu.cn/jisiludata/etf.php?rp=25&page=%s'
INDEX_ETF_COLS = ['fund_id', 'fund_nm', 'index_id', 'creation_unit', 'amount', 'unit_total',
                  'unit_incr', 'price', 'volume', 'increase_rt', 'estimate_value', 'discount_rt', 
                  'fund_nav', 'nav_dt', 'index_nm', 'index_increase_rt', 'pe', 'pb']
STOCK_LOF_URL = 'https://www.jisilu.cn/data/lof/stock_lof_list/?rp=25&page=%s'
STOCK_LOF_COLS = ['fund_id', 'fund_nm', 'price', 'increase_rt', 'volume', 'amount', 
                  'fund_nav', 'nav_dt', 'estimate_value', 'discount_rt', 'stock_ratio', 
                  'stock_increase_rt', 'apply_fee', 'redeem_fee', 'apply_redeem_status']
INDEX_LOF_URL = 'https://www.jisilu.cn/data/lof/index_lof_list/?rp=25&page=%s'
INDEX_LOF_COLS = ['fund_id', 'fund_nm', 'price', 'increase_rt', 'volume', 'amount', 
                  'fund_nav', 'nav_dt', 'estimate_value', 'discount_rt', 'index_id', 'index_nm', 
                  'index_increase_rt', 'apply_fee', 'redeem_fee', 'apply_redeem_status']
RATING_FUNDA_URL = 'https://www.jisilu.cn/data/sfnew/funda_list/?page=%s'
RATING_FUNDA_COLS = ['funda_id', 'funda_name', 'funda_current_price', 'funda_increase_rt', 'funda_volume', 'funda_value',
                    'funda_discount_rt', 'funda_coupon', 'funda_coupon_next', 'funda_profit_rt_next', 'funda_index_id', 
                    'funda_index_name', 'funda_index_increase_rt', 'funda_lower_recalc_rt', 'lower_recalc_profit_rt', 
                    'fundb_upper_recalc_rt', 'funda_base_est_dis_rt_t1', 'funda_base_est_dis_rt_t2', 'funda_amount', 
                    'funda_amount_increase', 'abrate', 'next_recalc_dt']
RATING_FUNDB_URL = 'https://www.jisilu.cn/data/sfnew/fundb_list/?page=%s'
RATING_FUNDB_COLS = ['fundb_id', 'fundb_name', 'fundb_base_fund_id', 'funda_id', 'funda_name', 'coupon', 'manage_fee', 'funda_current_price', 
                     'funda_upper_price', 'funda_lower_price', 'funda_increase_rt', 'fundb_current_price', 'fundb_upper_price', 
                     'fundb_lower_price', 'fundb_increase_rt', 'fundb_volume', 'fundb_value', 'fundm_value', 'fundb_discount_rt', 
                     'fundb_price_leverage_rt', 'fundb_net_leverage_rt', 'fundb_capital_rasising_rt', 'fundb_lower_recalc_rt', 
                     'fundb_upper_recalc_rt', 'b_est_val', 'fundb_index_id', 'fundb_index_name', 'fundb_index_increase_rt', 
                     'funda_ratio', 'fundb_ratio', 'fundb_base_price', 'fundB_amount', 'fundB_amount_increase', 'abrate']
RATING_FUNDM_URL = 'https://www.jisilu.cn/data/sfnew/fundm_list/?page=%s'
RATING_FUNDM_COLS = ['base_fund_id', 'base_fund_nm', 'market', 'issue_dt', 'manage_fee', 'index_id', 'index_nm', 'lower_recalc_price',
                     'a_ratio', 'b_ratio', 'next_recalc_dt', 'fundA_id', 'fundA_nm', 'coupon', 'coupon_next', 'fundB_id', 'fundB_nm', 
                     'price', 'base_lower_recalc_rt', 'abrate']
CON_BONDS_URL = 'https://www.jisilu.cn/data/cbnew/cb_list/?page=%s'
CON_BONDS_COLS = ['bond_id', 'bond_nm', 'stock_id', 'stock_nm', 'market', 'convert_price', 'convert_dt', 'issue_dt', 'maturity_dt',
                  'next_put_dt', 'put_price', 'put_count_days', 'put_total_days', 'redeem_price', 'redeem_price_ratio', 'redeem_count_days',
                  'redeem_total_days', 'orig_iss_amt', 'curr_iss_amt', 'rating_cd', 'issuer_rating_cd', 'guarantor', 'active_fl', 'ration_rt',
                  'pb', 'sprice', 'sincrease_rt', 'last_time', 'convert_value', 'premium_rt', 'year_left', 'ytm_rt', 'ytm_rt_tax', 'price',
                  'increase_rt', 'volume', 'force_redeem_price', 'put_convert_price', 'convert_amt_ratio', 'stock_cd', 'pre_bond_id']
NEW_CON_BONDS_URL = 'https://www.jisilu.cn/data/cbnew/pre_list/?page=%s'
NEW_CON_BONDS_COLS = ['bond_id', 'bond_nm', 'apply_cd', 'apply_date', 'list_date', 'amount', 'convert_price', 'pma_rt', 'stock_id',
                      'stock_nm', 'price', 'increase_rt', 'ration_rt', 'online_amount', 'lucky_draw_rt', 'individual_limit',
                      'underwriter_rt', 'rating_cd', 'progress_nm', 'apply_tips', 'valid_apply']
CLOSED_STOCK_FUND_URL = 'https://www.jisilu.cn/data/cf/cf_list/?page=%s'
CLOSED_STOCK_FUND_COLS = ['fund_id', 'fund_nm', 'issue_dt', 'duration', 'last_time', 'price', 'increase_rt', 'volume', 'net_value',
                          'nav_dt', 'realtime_estimate_value', 'discount_rt', 'left_year', 'annualize_dscnt_rt', 'quote_incr_rt',
                          'nav_incr_rt', 'spread', 'stock_ratio', 'report_dt', 'daily_nav_incr_rt', 'daily_spread']
CLOSED_BOND_FUND_URL = 'https://www.jisilu.cn/jisiludata/CloseBondFund.php?page=%s'
CLOSED_BOND_FUND_COLS = ['fund_id', 'fund_nm', 'maturity_dt', 'left_year', 'est_val', 'discount_rt', 'annual_discount_rt',
                         'trade_price', 'increase_rt', 'volume', 'last_time', 'fund_nav', 'last_chg_dt', 'price_incr_rt',
                         'stock_ratio', 'bond_ratio', 'report_dt', 'is_outdate']
AH_RATIO_URL = 'https://www.jisilu.cn/data/ha/index2list/?page=%s'
AH_RATIO_COLS = ['a_code', 'stock_name', 'a_price', 'a_increase_rt', 'h_code', 'h_price', 'h_increase_rt', 'last_time',
                 'rmb_price', 'hk_currency', 'ha_ratio', 'h_free_shares', 'a_free_shares']
DIVIDEND_RATE_URL = 'https://www.jisilu.cn/data/stock/dividend_rate_list/?page=%s'
DIVIDEND_RATE_COLS = ['stock_id', 'stock_nm', 'dividend_rate', 'dividend_rate2', 'ipo_date', 'price', 'volume', 'increase_rt', 'pe', 'pb',
                      'total_value', 'eps_growth_ttm', 'roe', 'revenue_average', 'profit_average', 'roe_average', 
                      'pb_temperature', 'pe_temperature', 'int_debt_rate', 'cashflow_average', 'dividend_rate_average', 
                      'dividend_rate5', 'industry_nm', 'active_flg', 'last_time']
HISTORY_TICK_COLUMNS = ['time', 'price', 'change', 'volume', 'amount', 'type']
TODAY_TICK_COLUMNS = ['time', 'price', 'pchange', 'change', 'volume', 'amount', 'type']
DAY_TRADING_COLUMNS = ['code', 'symbol', 'name', 'changepercent',
                       'trade', 'open', 'high', 'low', 'settlement', 'volume', 'turnoverratio',
                       'amount', 'per', 'pb', 'mktcap', 'nmc']
REPORT_COLS = ['code', 'name', 'eps', 'eps_yoy', 'bvps', 'roe',
               'epcf', 'net_profits', 'profits_yoy', 'distrib', 'report_date']
FORECAST_COLS = ['code', 'name', 'type', 'report_date', 'pre_eps', 'range']
PROFIT_COLS = ['code', 'name', 'roe', 'net_profit_ratio',
               'gross_profit_rate', 'net_profits', 'eps', 'business_income', 'bips']
OPERATION_COLS = ['code', 'name', 'arturnover', 'arturndays', 'inventory_turnover',
                  'inventory_days', 'currentasset_turnover', 'currentasset_days']
GROWTH_COLS = ['code', 'name', 'mbrg', 'nprg', 'nav', 'targ', 'epsg', 'seg']
DEBTPAYING_COLS = ['code', 'name', 'currentratio',
                   'quickratio', 'cashratio', 'icratio', 'sheqratio', 'adratio']
CASHFLOW_COLS = ['code', 'name', 'cf_sales', 'rateofreturn',
                 'cf_nm', 'cf_liabilities', 'cashflowratio']
DAY_PRICE_COLUMNS = ['date', 'open', 'high', 'close', 'low', 'volume', 'price_change', 'p_change',
                     'ma5', 'ma10', 'ma20', 'v_ma5', 'v_ma10', 'v_ma20', 'turnover']
INX_DAY_PRICE_COLUMNS = ['date', 'open', 'high', 'close', 'low', 'volume', 'price_change', 'p_change',
                         'ma5', 'ma10', 'ma20', 'v_ma5', 'v_ma10', 'v_ma20']
LIVE_DATA_COLS = ['name', 'open', 'pre_close', 'price', 'high', 'low', 'bid', 'ask', 'volume', 'amount',
                  'b1_v', 'b1_p', 'b2_v', 'b2_p', 'b3_v', 'b3_p', 'b4_v', 'b4_p', 'b5_v', 'b5_p',
                  'a1_v', 'a1_p', 'a2_v', 'a2_p', 'a3_v', 'a3_p', 'a4_v', 'a4_p', 'a5_v', 'a5_p', 'date', 'time', 's']
FOR_CLASSIFY_B_COLS = ['code','name']
FOR_CLASSIFY_W_COLS = ['date','code', 'weight']
FOR_CLASSIFY_W5_COLS = ['date','code', 'name', 'weight']
THE_FIELDS = ['code','symbol','name','changepercent','trade','open','high','low','settlement','volume','turnoverratio']
KLINE_TT_COLS = ['date', 'open', 'close', 'high', 'low', 'volume']
HISTORY_TICKS_URL = 'http://market.finance.sina.com.cn/transHis.php?date=%s&symbol=%s&page=%s'
TODAY_TICKS_PAGE_URL = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_Transactions.getAllPageTime?date=%s&symbol=%s'
TODAY_TICKS_URL = 'http://vip.stock.finance.sina.com.cn/quotes_service/view/vMS_tradedetail.php?symbol=%s&date=%s&page=%s'
HISTORY_URL = 'http://web.ifzq.gtimg.cn/appstock/app/%skline/get?_var=kline_day%s&param=%s,%s,%s,%s,640,%s&r=0.%s'
HISTORY_MIN_URL = 'http://ifzq.gtimg.cn/appstock/app/kline/mkline?param=%s,m%s,,640&_var=m%s_today&r=0.%s'
DAY_PRICE_URL = '%sapi.finance.%s/%s/?code=%s&type=last'
LIVE_DATA_URL = 'http://hq.sinajs.cn/rn=%s&list=%s'
DAY_PRICE_MIN_URL = '%sapi.finance.%s/akmin?scode=%s&type=%s'
LATEST_URL = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?num=80&sort=code&asc=0&node=hs_a&symbol=&_s_r_a=page&page=%s'
REPORT_URL = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/mainindex/index.phtml?s_i=&s_a=&s_c=&reportdate=%s&quarter=%s&p=%s&num=%s'
FORECAST_URL = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/performance/index.phtml?s_i=&s_a=&s_c=&s_type=&reportdate=%s&quarter=%s&p=%s&num=%s'
PROFIT_URL = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/profit/index.phtml?s_i=&s_a=&s_c=&reportdate=%s&quarter=%s&p=%s&num=%s'
OPERATION_URL = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/operation/index.phtml?s_i=&s_a=&s_c=&reportdate=%s&quarter=%s&p=%s&num=%s'
GROWTH_URL = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/grow/index.phtml?s_i=&s_a=&s_c=&reportdate=%s&quarter=%s&p=%s&num=%s'
DEBTPAYING_URL = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/debtpaying/index.phtml?s_i=&s_a=&s_c=&reportdate=%s&quarter=%s&p=%s&num=%s'
CASHFLOW_URL = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/cashflow/index.phtml?s_i=&s_a=&s_c=&reportdate=%s&quarter=%s&p=%s&num=%s'
SHIBOR_TYPE ={'Shibor': 'Shibor数据', 'Quote': '报价数据', 'Tendency': 'Shibor均值数据',
              'LPR': 'LPR数据', 'LPR_Tendency': 'LPR均值数据'}
SHIBOR_DATA_URL = 'http://www.shibor.org/shibor/web/html/downLoad.html?nameNew=Historical_%s_Data_%s.xls&downLoadPath=data&nameOld=%s%s.xls&shiborSrc=http://www.shibor.org/shibor/'
ALL_STOCK_PROFILES_URL = 'http://s.askci.com/stock/a/?reportTime=%s&pageNum=%s#QueryCondition'
ALL_STOCK_PROFILES_COLS = ['code', 'name', 'city', 'staff', 'date', 'industry', 'pro_type', 'main']
SINA_CONCEPTS_INDEX_URL = 'http://money.finance.sina.com.cn/q/view/newFLJK.php?param=class'
SINA_INDUSTRY_INDEX_URL = 'http://vip.stock.finance.sina.com.cn/q/view/%s'
SINA_DATA_DETAIL_URL = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page=1&num=1000&sort=symbol&asc=1&node=%s&symbol=&_s_r_a=page'
INDEX_C_COMM = 'sseportal/ps/zhs/hqjt/csi'
HS300_CLASSIFY_URL_FTP = '%s%s/webdata/%s'
HS300_CLASSIFY_URL_HTTP = '%s%s/%s/%s'
HIST_FQ_URL = '%s%s/corp/go.php/vMS_FuQuanMarketHistory/stockid/%s.phtml?year=%s&jidu=%s'
HIST_INDEX_URL = '%s%s/corp/go.php/vMS_MarketHistory/stockid/%s/type/S.phtml?year=%s&jidu=%s'
HIST_FQ_FACTOR_URL = '%s%s/api/json.php/BasicStockSrv.getStockFuQuanData?symbol=%s&type=hfq'
INDEX_URL = 'http://hq.sinajs.cn/rn=xppzh&list=sh000001,sh000002,sh000003,sh000008,sh000009,sh000010,sh000011,sh000012,sh000016,sh000017,sh000300,sh000905,sz399001,sz399002,sz399003,sz399004,sz399005,sz399006,sz399008,sz399100,sz399101,sz399106,sz399107,sz399108,sz399333,sz399606'
SSEQ_CQ_REF_URL = '%s%s/assortment/stock/list/name'
SINA_DD = 'http://vip.stock.finance.sina.com.cn/quotes_service/view/cn_bill_download.php?symbol=%s&num=60&page=1&sort=ticktime&asc=0&volume=%s&amount=0&type=0&day=%s'
BOX = 'boxOffice'
MOVIE_BOX = '%s%s/%s/GetHourBoxOffice?d=%s'
BOXOFFICE_DAY = '%s%s/%s/GetDayBoxOffice?num=%s&d=%s'
BOXOFFICE_MONTH = '%s%s/%s/getMonthBox?sdate=%s'
BOXOFFICE_CBD = '%s%s/%s/getCBD?pIndex=%s&dt=%s'
SHIBOR_COLS = ['date', 'ON', '1W', '2W', '1M', '3M', '6M', '9M', '1Y']
QUOTE_COLS = ['date', 'bank', 'ON', '1W', '2W', '1M', '3M', '6M', '9M', '1Y']
SHIBOR_MA_COLS = ['date', 'ON_5', 'ON_10', 'ON_20', '1W_5', '1W_10', '1W_20','2W_5', '2W_10', '2W_20',
                  '1M_5', '1M_10', '1M_20', '3M_5', '3M_10', '3M_20', '6M_5', '6M_10', '6M_20',
                  '9M_5', '9M_10', '9M_20','1Y_5', '1Y_10', '1Y_20']
LPR_COLS = ['date', '1Y']
LPR_MA_COLS = ['date', '1Y_5', '1Y_10', '1Y_20']
INDEX_HEADER = 'code,name,open,preclose,close,high,low,0,0,volume,amount,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,d,c,3\n'
INDEX_COLS = ['code', 'name', 'change', 'open', 'preclose', 'close', 'high', 'low', 'volume', 'amount']
HIST_FQ_COLS = ['date', 'open', 'high', 'close', 'low', 'volume', 'amount', 'factor']
SINA_DD_COLS = ['code', 'name', 'time', 'price', 'volume', 'preprice', 'type']
GLOBAL_HQ_SYMBOL = 'sh000001,hkHSI,znb_UKX,znb_DAX,znb_INDEXCF,znb_CAC,znb_SMI,znb_FTSEMIB,znb_MADX,znb_OMX,znb_SPX,znb_HEX,znb_OSEAX,znb_ISEQ,znb_AEX,znb_ICEXI,znb_NKY,znb_TWSE,znb_FSSTI,znb_KOSPI,znb_FBMKLCI,znb_SET,znb_JCI,znb_PCOMP,znb_KSE100,znb_SENSEX,znb_VNINDEX,znb_CSEALL,znb_SASEIDX,znb_SPTSX,znb_MEXBOL,znb_IBOV,znb_MERVAL,znb_AS51,znb_NZSE50FG,znb_CASE,znb_JALSH,sz399001,znb_INDU,znb_CCMP'
GLOBAL_HQ_COLS = ['symbol', 'name', 'price', 'chga', 'chgp', 'datetime']
HIST_FQ_FACTOR_COLS = ['code','value']
GETTING_TIPS = '[Progress:]'
GETTING_FLAG = '#'
DATA_INPUT_ERROR_MSG = 'date input error.'
NETWORK_URL_ERROR_MSG = '获取失败，请检查网络和URL'
NETWORK_ERR_MSG = '获取失败，请检查网络和URL；或者您访问的过于频繁，被服务器拦截，请稍后再试'
DATE_CHK_MSG = '年度输入错误：请输入1989年以后的年份数字，格式：YYYY'
DATE_CHK_Q_MSG = '季度输入错误：请输入1、2、3或4数字'
TOP_PARAS_MSG = 'top有误，请输入整数或all.'
LHB_MSG = '周期输入有误，请输入数字5、10、30或60'
TOKEN_F_P = 'tk.csv'
BOX_INPUT_ERR_MSG = '请输入YYYY-MM格式的年月数据'
HOLIDAY_SERVE_ERR = '节假日查询服务出错'
INDEX_SYMBOL = {"399990": "sz399990", "000006": "sh000006", "399998": "sz399998", 
                "399436": "sz399436", "399678": "sz399678", "399804": "sz399804", 
                "000104": "sh000104", "000070": "sh000070", "399613": "sz399613", 
                "399690": "sz399690", "399928": "sz399928", "000928": "sh000928", 
                "000986": "sh000986", "399806": "sz399806", "000032": "sh000032", 
                "000005": "sh000005", "399381": "sz399381", "399908": "sz399908", 
                "000908": "sh000908", "399691": "sz399691", "000139": "sh000139", 
                "399427": "sz399427", "399248": "sz399248", "000832": "sh000832", 
                "399901": "sz399901", "399413": "sz399413", "000901": "sh000901", 
                "000078": "sh000078", "000944": "sh000944", "000025": "sh000025", 
                "399944": "sz399944", "399307": "sz399307", "000052": "sh000052", 
                "399680": "sz399680", "399232": "sz399232", "399993": "sz399993", 
                "000102": "sh000102", "000950": "sh000950", "399950": "sz399950", 
                "399244": "sz399244", "399925": "sz399925", "000925": "sh000925", 
                "000003": "sh000003", "000805": "sh000805", "000133": "sh000133", 
                "399677": "sz399677", "399319": "sz399319", "399397": "sz399397", 
                "399983": "sz399983", "399654": "sz399654", "399440": "sz399440", 
                "000043": "sh000043", "000012": "sh000012", "000833": "sh000833", 
                "000145": "sh000145", "000053": "sh000053", "000013": "sh000013", 
                "000022": "sh000022", "000094": "sh000094", "399299": "sz399299", 
                "000101": "sh000101", "399817": "sz399817", "399481": "sz399481", 
                "399434": "sz399434", "399301": "sz399301", "000029": "sh000029", 
                "399812": "sz399812", "399441": "sz399441", "000098": "sh000098", 
                "399557": "sz399557", "000068": "sh000068", "399298": "sz399298", 
                "399302": "sz399302", "000961": "sh000961", "000959": "sh000959", 
                "399961": "sz399961", "000126": "sh000126", "000036": "sh000036", 
                "399305": "sz399305", "000116": "sh000116", "399359": "sz399359", 
                "399810": "sz399810", "000062": "sh000062", "399618": "sz399618", 
                "399435": "sz399435", "000149": "sh000149", "000819": "sh000819", 
                "000020": "sh000020", "000061": "sh000061", "000016": "sh000016", 
                "000028": "sh000028", "399809": "sz399809", "000999": "sh000999", 
                "399238": "sz399238", "000100": "sh000100", "399979": "sz399979", 
                "000979": "sh000979", "399685": "sz399685", "000152": "sh000152", 
                "000153": "sh000153", "399318": "sz399318", "000853": "sh000853", 
                "000040": "sh000040", "399693": "sz399693", "000076": "sh000076", 
                "000017": "sh000017", "000134": "sh000134", "399989": "sz399989", 
                "000042": "sh000042", "000066": "sh000066", "000008": "sh000008", 
                "000002": "sh000002", "000001": "sh000001", "000011": "sh000011", 
                "000031": "sh000031", "399403": "sz399403", "000951": "sh000951", 
                "399951": "sz399951", "000092": "sh000092", "399234": "sz399234", 
                "000823": "sh000823", "399986": "sz399986", "399647": "sz399647", 
                "000050": "sh000050", "000073": "sh000073", "399357": "sz399357", 
                "000940": "sh000940", "000107": "sh000107", "000048": "sh000048", 
                "399411": "sz399411", "399366": "sz399366", "399373": "sz399373", 
                "000015": "sh000015", "000021": "sh000021", "000151": "sh000151", 
                "000851": "sh000851", "000058": "sh000058", "399404": "sz399404", 
                "399102": "sz399102", "399431": "sz399431", "399971": "sz399971", 
                "000125": "sh000125", "000069": "sh000069", "000063": "sh000063", 
                "399395": "sz399395", "000038": "sh000038", "399240": "sz399240", 
                "399903": "sz399903", "000989": "sh000989", "399321": "sz399321", 
                "399675": "sz399675", "399235": "sz399235", "000057": "sh000057", 
                "000056": "sh000056", "000903": "sh000903", "399310": "sz399310", 
                "000004": "sh000004", "000019": "sh000019", "399919": "sz399919", 
                "000974": "sh000974", "000919": "sh000919", "399635": "sz399635", 
                "399663": "sz399663", "399106": "sz399106", "399107": "sz399107", 
                "399555": "sz399555", "000090": "sh000090", "000155": "sh000155", 
                "000060": "sh000060", "399636": "sz399636", "000816": "sh000816", 
                "000010": "sh000010", "399671": "sz399671", "000035": "sh000035", 
                "399352": "sz399352", "399683": "sz399683", "399554": "sz399554", 
                "399409": "sz399409", "000018": "sh000018", "399101": "sz399101", 
                "000992": "sh000992", "399416": "sz399416", "399918": "sz399918", 
                "399379": "sz399379", "399674": "sz399674", "399239": "sz399239", 
                "399384": "sz399384", "399367": "sz399367", "000918": "sh000918", 
                "000914": "sh000914", "399914": "sz399914", "000054": "sh000054", 
                "000806": "sh000806", "399619": "sz399619", "399015": "sz399015", 
                "399393": "sz399393", "399313": "sz399313", "399231": "sz399231", 
                "000846": "sh000846", "000854": "sh000854", "399010": "sz399010", 
                "399666": "sz399666", "399387": "sz399387", "399399": "sz399399", 
                "000026": "sh000026", "399934": "sz399934", "000150": "sh000150", 
                "000934": "sh000934", "399317": "sz399317", "000138": "sh000138", 
                "399371": "sz399371", "399394": "sz399394", "399659": "sz399659", 
                "399665": "sz399665", "399931": "sz399931", "000161": "sh000161", 
                "399380": "sz399380", "000931": "sh000931", "399704": "sz399704", 
                "399616": "sz399616", "000817": "sh000817", "399303": "sz399303", 
                "399629": "sz399629", "399624": "sz399624", "399009": "sz399009", 
                "399233": "sz399233", "399103": "sz399103", "399242": "sz399242", 
                "399627": "sz399627", "000971": "sh000971", "399679": "sz399679", 
                "399912": "sz399912", "000982": "sh000982", "399668": "sz399668", 
                "000096": "sh000096", "399982": "sz399982", "000849": "sh000849", 
                "000148": "sh000148", "399364": "sz399364", "000912": "sh000912", 
                "000129": "sh000129", "000055": "sh000055", "000047": "sh000047", "399355": "sz399355", "399622": "sz399622", "000033": "sh000033", "399640": "sz399640", "000852": "sh000852", "399966": "sz399966", "399615": "sz399615", "399802": "sz399802", "399602": "sz399602", "000105": "sh000105", "399660": "sz399660", "399672": "sz399672", 
                "399913": "sz399913", "399420": "sz399420", "000159": "sh000159", "399314": "sz399314", "399652": "sz399652", 
                "399369": "sz399369", "000913": "sh000913", "000065": "sh000065", 
                "000808": "sh000808", "399386": "sz399386", "399100": "sz399100", 
                "000997": "sh000997", "000990": "sh000990", "000093": "sh000093", "399637": "sz399637", "399439": "sz399439", "399306": "sz399306", "000855": "sh000855", "000123": "sh000123", "399623": "sz399623", 
                "399312": "sz399312", "399249": "sz399249", "399311": "sz399311", "399975": "sz399975", "399356": "sz399356", 
                "399400": "sz399400", "399676": "sz399676", "000136": "sh000136", "399361": "sz399361", "399974": "sz399974", "399995": "sz399995", "399316": "sz399316", "399701": "sz399701", "000300": "sh000300", "000030": "sh000030", "000976": "sh000976", "399686": "sz399686", "399108": "sz399108", "399374": "sz399374", 
                "000906": "sh000906", "399707": "sz399707", "000064": "sh000064", "399633": "sz399633", "399300": "sz399300", "399628": "sz399628", "399398": "sz399398", "000034": "sh000034", 
                "399644": "sz399644", "399905": "sz399905", "399626": "sz399626", 
                "399625": "sz399625", "000978": "sh000978", "399664": "sz399664", "399682": "sz399682", "399322": "sz399322", "000158": "sh000158", "000842": "sh000842", "399550": "sz399550", "399423": "sz399423", "399978": "sz399978", "399996": "sz399996", "000905": "sh000905", 
                "000007": "sh000007", "000827": "sh000827", "399655": "sz399655", "399401": "sz399401", "399650": "sz399650", "000963": "sh000963", "399661": "sz399661", "399922": "sz399922", "000091": "sh000091", "399375": "sz399375", "000922": "sh000922", "399702": "sz399702", "399963": "sz399963", "399011": "sz399011", "399012": "sz399012", 
                "399383": "sz399383", "399657": "sz399657", "399910": "sz399910", "399351": "sz399351", "000910": "sh000910", "000051": "sh000051", "399376": "sz399376", "399639": "sz399639", "000821": "sh000821", "399360": "sz399360", "399604": "sz399604", "399315": "sz399315", "399658": "sz399658", "000135": "sh000135", 
                "000059": "sh000059", "399006": "sz399006", 
                "399320": "sz399320", "000991": "sh000991", "399606": "sz399606", 
                "399428": "sz399428", "399406": "sz399406", "399630": "sz399630", "000802": "sh000802", "399803": "sz399803", "000071": "sh000071", "399358": "sz399358", 
                "399013": "sz399013", "399385": "sz399385", "399008": "sz399008", "399649": "sz399649", 
                "399673": "sz399673", "399418": "sz399418", "399370": "sz399370", "000814": "sh000814", 
                "399002": "sz399002", "399814": "sz399814", "399641": "sz399641", "399001": "sz399001", 
                "399662": "sz399662", "399706": "sz399706", "399932": "sz399932", "000095": "sh000095", "000932": "sh000932", "399965": "sz399965", "399363": "sz399363", "399354": "sz399354", "399638": "sz399638", "399648": "sz399648", "399608": "sz399608", "000939": "sh000939", "399939": "sz399939", "399365": "sz399365", "399382": "sz399382", "399631": "sz399631", "399612": "sz399612", "399611": "sz399611", "399645": "sz399645", 
                "399324": "sz399324", "399552": "sz399552", "000858": "sh000858", "000045": "sh000045", 
                "000121": "sh000121", "399703": "sz399703", "399003": "sz399003", 
                "399348": "sz399348", "399389": "sz399389", "399007": "sz399007", "399391": "sz399391", "000973": "sh000973", 
                "000984": "sh000984", "000969": "sh000969", "000952": "sh000952", "399332": "sz399332", "399952": "sz399952", "399553": "sz399553", "000856": "sh000856", 
                "399969": "sz399969", "399643": "sz399643", "399402": "sz399402", "399372": "sz399372", "399632": "sz399632", "399344": "sz399344", "399808": "sz399808", "399620": "sz399620", "000103": "sh000103", "399911": "sz399911", "000993": "sh000993", "000983": "sh000983", "399687": "sz399687", "399933": "sz399933", "000933": "sh000933", "399437": "sz399437", "399433": "sz399433", "000046": "sh000046", "000911": "sh000911", "000114": "sh000114", "000049": "sh000049", "399392": "sz399392", "399653": "sz399653", "000975": "sh000975", "000044": "sh000044", "399378": "sz399378", "000828": "sh000828", "399634": "sz399634", 
                "399005": "sz399005", "000162": "sh000162", "399333": "sz399333", "000122": "sh000122", "399646": "sz399646", "000077": "sh000077", "000074": "sh000074", "399656": "sz399656", "399396": "sz399396", "399415": "sz399415", "399408": "sz399408", "000115": "sh000115", "000987": "sh000987", "399362": "sz399362", "000841": "sh000841", "000141": "sh000141", "000120": "sh000120", "399992": "sz399992", "000807": "sh000807", "399350": "sz399350", "000009": "sh000009", "000998": "sh000998", "399390": "sz399390", "399405": "sz399405", "000099": "sh000099", "399337": "sz399337", "000142": "sh000142", "399419": "sz399419", "399407": "sz399407", "000909": "sh000909", "000119": "sh000119", "399909": "sz399909", "399805": "sz399805", "000996": "sh000996", "000847": "sh000847", "000130": "sh000130", "399377": "sz399377", "399388": "sz399388", "399610": "sz399610", "000958": "sh000958", 
                "399958": "sz399958", "000075": "sh000075", "399346": "sz399346", "000147": "sh000147", "000132": "sh000132", "000108": "sh000108", "399642": "sz399642", "000977": "sh000977", "399689": "sz399689", "399335": "sz399335", "399977": "sz399977", "399972": "sz399972", "399970": "sz399970", "399004": "sz399004", "399341": "sz399341", "399330": "sz399330", "399917": "sz399917", "000160": "sh000160", "399432": "sz399432", "399429": "sz399429", "000917": "sh000917", 
                "000128": "sh000128", "000067": "sh000067", "000079": "sh000079", "399236": "sz399236", "399994": "sz399994", "399237": "sz399237", "000966": "sh000966", "000957": "sh000957", "399328": "sz399328", 
                "399353": "sz399353", "399957": "sz399957", "399412": "sz399412", "000904": "sh000904", "399904": "sz399904", "399410": "sz399410", "000027": "sh000027", "399667": "sz399667", "000857": "sh000857", 
                "000131": "sh000131", "000964": "sh000964", "399339": "sz399339", "399964": "sz399964", "399991": "sz399991", "399417": "sz399417", "000146": "sh000146", "399551": "sz399551", "000137": "sh000137", "000118": "sh000118", "399976": "sz399976", "000109": "sh000109", "399681": "sz399681", "399438": "sz399438", "000117": "sh000117", "399614": "sz399614", "399669": "sz399669", "000111": "sh000111", "399670": "sz399670", "000097": "sh000097", "000106": "sh000106", "000039": "sh000039", "399935": "sz399935", "000935": "sh000935", "399813": "sz399813", "000037": "sh000037", "399811": "sz399811", "399705": "sz399705", "399556": "sz399556", "000113": "sh000113", "000072": "sh000072", "399651": "sz399651", "399617": "sz399617", "399684": "sz399684", "000041": "sh000041", "399807": "sz399807", "399959": "sz399959", "399967": "sz399967", "399326": "sz399326", "399688": "sz399688", "399368": "sz399368", "399241": "sz399241", "399696": "sz399696", "000850": "sh000850", "000110": "sh000110", "399621": "sz399621", "399243": "sz399243", 
                "399973": "sz399973", "399987": "sz399987", "000112": "sh000112", "399997": "sz399997", 
                "hkHSI":"hkHSI"}
DP_163_URL = 'http://quotes.money.163.com/data/caibao/fpyg.html?reportdate=%s&sort=declaredate&order=desc&page=%s'
DP_163_COLS = ['code', 'name', 'year', 'plan', 'report_date']
RL_URL = 'http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=FD&sty=BST&st=3&sr=true&fd=%s&stat=%s'
RL_COLS = ['code', 'name', 'date', 'count', 'ratio']
QUARTS_DIC = {'1':('%s-12-31', '%s-03-31'), '2':('%s-03-31', '%s-06-30'), '3':('%s-06-30', '%s-09-30'), '4':('%s-9-30', '%s-12-31')}
FUND_HOLDS_URL = 'http://quotes.money.163.com/hs/marketdata/service/jjcgph.php?host=/hs/marketdata/service/jjcgph.php&page=%s&query=start:%s;end:%s&order=desc&count=60&type=query&req=%s'
FUND_HOLDS_COLS = ['count', 'clast', 'date', 'ratio', 'amount', 'nums','nlast', 'name', 'code']
NEW_STOCKS_URL = 'http://vip.stock.finance.sina.com.cn/corp/view/vRPD_NewStockIssue.php?page=%s&cngem=0&orderBy=NetDate&orderType=desc'
NEW_STOCKS_COLS = ['code', 'xcode', 'name', 'ipo_date', 'issue_date', 'amount', 'markets', 'price', 'pe', 'limit', 'funds', 'ballot']

MAR_URL = "http://dcfm.eastmoney.com//EM_MutiSvcExpandInterface/api/js/get?token=70f12f2f4f091e459a279469fe49eca5&st=tdate&sr=-1&p=%s&ps=50&js=var UYirVWSV={pages:(tp),data: (x)}&type=RZRQ_HSTOTAL_NJ&filter=(market='%s')&mk_time=1&rt=%s"
MAR_COLS = ['tdate', 'close', 'zdf', 'rzye', 'rzyezb', 'rzmre', 'rzche', 'rzjmre', 'rqye', 'rqyl', 'rqmcl', 'rqchl', 'rqjmcl', 'rzrqye', 'rzrqyecz']
MAR_BOTH_DETAIL = "http://dcfm.eastmoney.com/em_mutisvcexpandinterface/api/js/get?type=RZRQ_DETAIL_NJ&token=70f12f2f4f091e459a279469fe49eca5&filter=(tdate='%sT00:00:00')&st=rzjmre&sr=-1&p=%s&ps=50&js=var nZxTWeXw={pages:(tp),data:(x)}&type=RZRQ_DETAIL_NJ&time=1&rt=%s"
MAR_DET_All_COLS = ['scode', 'sname', 'rzye', 'rzyezb', 'rzmre', 'rzche', 'rzjmre', 'rqye', 'rqyl', 'rqmcl', 'rqchl', 'rqjmcl', 'rzrqye', 'rzrqyecz']
MAR_TOTAL_URL = 'http://dcfm.eastmoney.com//EM_MutiSvcExpandInterface/api/js/get?token=70f12f2f4f091e459a279469fe49eca5&st=tdate&sr=-1&p=%s&ps=50&js=var BKNgVufZ={pages:(tp),data:(x)}&type=RZRQ_LSTOTAL_NJ&mk_time=1&rt=%s'
MAR_TOTAL_COLS = ['tdate', 'close', 'zdf', 'rzye', 'rzyezb', 'rzmre', 'rzche', 'rzjmre', 'rqye', 'rqyl', 'rqmcl', 'rqchl', 'rqjmcl', 'rzrqye', 'rzrqyecz']

MACRO_URL = 'http://money.finance.sina.com.cn/mac/api/jsonp.php/SINAREMOTECALLCALLBACK%s/MacPage_Service.get_pagedata?cate=%s&event=%s&from=0&num=%s&condition=&_=%s'
GDP_YEAR_COLS = ['year','gdp','pc_gdp','gnp','pi','si','industry','cons_industry','ti','trans_industry','lbdy']
GDP_QUARTER_COLS = ['quarter','gdp','gdp_yoy','pi','pi_yoy','si','si_yoy','ti','ti_yoy']
GDP_FOR_COLS = ['year','cons_to','cons_rate','asset_to','asset_rate','goods_to','goods_rate']
GDP_PULL_COLS = ['year','gdp_yoy','pi','si','industry','ti']
GDP_CONTRIB_COLS = ['year','gdp_yoy','pi','si','industry','ti']
CPI_COLS = ['month','cpi']
PPI_COLS = ['month','ppiip','ppi','qm','rmi','pi','cg','food','clothing','roeu','dcg']
DEPOSIT_COLS = ['date','deposit_type','rate']
LOAN_COLS = ['date','loan_type','rate']
RRR_COLS = ['date','before','now','changed']
MONEY_SUPPLY_COLS = ['month','m2','m2_yoy','m1','m1_yoy','m0','m0_yoy','cd','cd_yoy','qm','qm_yoy','ftd','ftd_yoy','sd','sd_yoy','rests','rests_yoy']
MONEY_SUPPLY_BLA_COLS = ['year','m2','m1','m0','cd','qm','ftd','sd','rests']

TERMINATED_URL = '%s%s/%s?jsonCallBack=jsonpCallback%s&isPagination=true&sqlId=COMMON_SSE_ZQPZ_GPLB_MCJS_ZZSSGGJBXX_L&pageHelp.pageSize=50&_=%s'
TERMINATED_T_COLS = ['COMPANY_CODE', 'COMPANY_ABBR', 'LISTING_DATE', 'CHANGE_DATE']
TERMINATED_COLS = ['code', 'name', 'oDate', 'tDate']

LHB_URL = 'http://data.eastmoney.com/DataCenter_V3/stock2016/TradeDetail/pagesize=200,page=1,sortRule=-1,sortType=,startDate=%s,endDate=%s,gpfw=0,js=vardata_tab_1.html'
LHB_TMP_COLS = ['SCode', 'SName', 'Chgradio', 'ZeMoney', 'Bmoney', 'Smoney', 'Ctypedes', 'Turnover', 'JD']
LHB_COLS = ['code', 'name', 'pchange', 'amount', 'buy', 'sell', 'reason', 'Turnover', 'unscramble']
LHB_SINA_URL = 'http://vip.stock.finance.sina.com.cn/q/go.php/vLHBData/kind/%s/index.phtml?last=%s&p=%s'
LHB_KINDS = ['ggtj', 'yytj', 'jgzz', 'jgmx']
LHB_GGTJ_COLS = ['code', 'name', 'count', 'bamount', 'samount', 'net', 'bcount', 'scount']
LHB_YYTJ_COLS = ['broker', 'count', 'bamount', 'bcount', 'samount', 'scount', 'top3']
LHB_JGZZ_COLS = ['code', 'name', 'bamount', 'bcount', 'samount', 'scount', 'net']
LHB_JGMX_COLS = ['code', 'name', 'date', 'bamount', 'samount', 'type']

XQ_TOPICS_URL = 'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=%d&count=15&category=-1'
XQ_TOPICS_COLS = ['title', 'description', 'target', 'screen_name', 'followers_count', 'source', 'reply_count', 'retweet_count', 'view_count', 'created_at', 'column']
XQ_NEWS_URL = 'https://xueqiu.com/v4/statuses/user_timeline.json?page=%d&user_id=5124430882'
XQ_NEWS_COLS = ['description', 'text', 'source', 'created_at', 'retweet_count', 'reply_count', 'fav_count', 'view_count',
                'reward_count', 'reward_amount', 'reward_user_count', 'talk_count', 'like_count', 'type', 'target', 'timeBefore']
XQ_HOT_COMMENTS_URL = 'https://xueqiu.com/statuses/search.json?count=10&comment=0&symbol=%s&hl=0&source=all&sort=alpha&page=%d&q='
XQ_HOT_COMMENTS_COLS = ['user_id', 'text', 'created_at', 'retweet_count', 'reply_count', 'fav_count', 'description',
                        'screen_name', 'friends_count', 'followers_count', 'target', 'view_count', 'reward_count', 'reward_user_count',
                        'like_count', 'source']

