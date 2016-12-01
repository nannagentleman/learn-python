# -*- coding: utf-8 -*-
"""
计算任意两个日期之间的间隔是：
a)         多少天
b)         多少周
c)         多少月
d)         多少季度
e)         多少年
"""
import datetime

def date(year, month, day):
    return datetime.datetime(year, month, day)


def interval_day(date1, date2):
    day = date1 - date2
    day = abs(day)
    return day.days

def interval_week(date1, date2):
    day = date1 - date2
    day = abs(day)
    d = day.days
    weeks = d / 7
    return weeks
    
def interval_month(date1, date2):
    day = date1 - date2
    day = abs(day)
    d = day.days
    months = d/30
    return months
    
def interval_year(date1, date2):
    day = date1 - date2
    day = abs(day)
    d = day.days
    years = d/365
    return years

def interval_quarter(date1, date2):
    #一季度按91天计算
    day = date1 - date2
    day = abs(day)
    d = day.days
    quarters = d/91
    return quarters
    
#test
date1 =  date(2016,5,1)
date2 = date(2014, 5, 1)   
print interval_day(date1, date2)
print interval_week(date1, date2)
print interval_month(date1, date2)
print interval_year(date1, date2)
print interval_quarter(date1, date2)