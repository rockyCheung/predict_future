# -*- coding:utf-8 -*-
"""
公用类
Created on 2019/01/15
@author: TabQ
@group : gugu
@contact: 16621596@qq.com
"""

from __future__ import division
import datetime
import json
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import for_future.stock.config as cf

class Utility():
    @staticmethod    
    def str2Dict(string):
        string = eval(string, type('Dummy', (dict,), dict(__getitem__ = lambda s, n:n))())
        string = json.dumps(string)
        
        return json.loads(string)
    
    
    @staticmethod
    def fceil(number, ndigits=2):
        if number == 0:
            return number
        
        tail_number = 1 / pow(10, ndigits)
        ndigits_number = round(number, ndigits)
        
        result = number - ndigits_number
        if result == 0:
            return number
        elif result > 0:
            return ndigits_number + tail_number
        else:
            return ndigits_number
    
    
    @staticmethod
    def checkQuarter(year, quarter):
        if isinstance(year, str) or year < 1989 :
            raise TypeError(cf.DATE_CHK_MSG)
        elif quarter is None or isinstance(quarter, str) or quarter not in [1, 2, 3, 4]:
            raise TypeError(cf.DATE_CHK_Q_MSG)
        else:
            return True
        
        
    @staticmethod
    def checkLhbInput(last):
        if last not in [5, 10, 30, 60]:
            raise TypeError(cf.LHB_MSG)
        else:
            return True
        
    
    @staticmethod
    def symbol(code):
        """
                            生成symbol代码标志
        """
        if code in cf.INDEX_LABELS:
            return cf.INDEX_LIST[code]
        elif len(code) != 6 :
            return ''
        else:
            return 'sh%s' % code if code[:1] in ['5', '6', '9'] else 'sz%s' % code 
        
        
    @staticmethod
    def random(n=13):
        from random import randint
        
        start = 10**(n-1)
        end = (10**n)-1
        
        return str(randint(start, end))
    
    
    @staticmethod
    def getToday():
        return str(datetime.datetime.today().date())
    
    
    @staticmethod
    def getHour():
        return datetime.datetime.today().hour
        
    
    @staticmethod
    def getMonth():
        return datetime.datetime.today().month
        
    
    @staticmethod
    def getYear():
        return datetime.datetime.today().year
        
    
    @staticmethod
    def getTodayLastYear():
        return str(Utility.getDateInterval(days=-365))

    
    @staticmethod
    def getTodayLastMonth():
        return str(Utility.getDateInterval(days=-30))
        
    
    @staticmethod
    def getTodayLastWeek():
        return str(Utility.getDateInterval(days=-7))
        
        
    @staticmethod
    def getDateInterval(date=str(datetime.datetime.today().date()), days=-1):
        return datetime.datetime.strptime(date, '%Y-%m-%d').date() + datetime.timedelta(days)
    
    
    @staticmethod
    def diffDays(start=None, end=None):
        d1 = datetime.datetime.strptime(end, '%Y-%m-%d')
        d2 = datetime.datetime.strptime(start, '%Y-%m-%d')
        delta = d1 - d2
        
        return delta.days
    
    
    @staticmethod
    def ttDates(start='', end=''):
        startyear = int(start[0:4])
        endyear = int(end[0:4])
        dates = [d for d in range(startyear, endyear+1, 2)]
        
        return dates
    
    
    @staticmethod
    def lastTradeDate(date=str(datetime.datetime.today().date())):
        lastdate = str(Utility.getDateInterval(date, -1))
        
        if Utility.isTradeDay(lastdate):
            return lastdate
        else:
            return Utility.lastTradeDate(lastdate)
        
        
    @staticmethod
    def nextTradeDate(date=str(datetime.datetime.today().date())):
        nextdate = str(Utility.getDateInterval(date, 1))
        
        if Utility.isTradeDay(nextdate):
            return nextdate
        else:
            return Utility.nextTradeDate(nextdate)
        
        
    @staticmethod
    def isHoliday(date=str(datetime.datetime.today().date())):
        """
                            节假日判断
        Parameters
        ------
            date: string
                                                        查询日期 format：YYYY-MM-DD 为空时取当前日期
        return
        ------
            True or False
        """
        session = requests.Session()
        retry = Retry(connect=5, backoff_factor=1)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.keep_alive = False
        
        try:
            request = session.get( cf.HOLIDAY_URL % date, timeout=10 )
            dataDict = json.loads(request.text)
            if dataDict['code'] != 0:
                raise IOError(cf.HOLIDAY_SERVE_ERR)
            elif dataDict['holiday'] is None:
                return False
            else:
                return True
        except Exception as e:
                print(e)
    
    
    @staticmethod
    def isTradeDay(date=str(datetime.datetime.today().date())):
        """
                            交易日判断
        Parameters
        ------
            date: string
                                                        查询日期 format：YYYY-MM-DD 为空时取当前日期
        return
        ------
            True or False
        """
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        w = int(date.strftime('%w'))
        
        if w in [6, 0]:
            return False
        else: 
            return not Utility.isHoliday(date)
        
