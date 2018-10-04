# -*- encoding:utf-8 -*-
import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
import re
import csv
import time

# 从网上把相应的网址爬下来
def put_url(month,year):
    try:
        url = 'http://www.creprice.cn/rank/citylease.html?type=11&y='+str(year)+'&m='+str(month)+'&citylevel=1'
        kv = {'user-agent': 'Mazilla/5.0'}
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        html = r.text
        return html
    except:
        return ''

# 用bs4把我们要的具体数据拿出来
def data_dict(month, year):
    html = put_url(month, year)
    data={}
    soup = BeautifulSoup(html, 'lxml')
    soup1 = soup.find('tbody', attrs={'id':'order_f'})
    td = soup1.td

    for i in range(6):
        cityname = td.find_next('td').string
        data[cityname] = [0, '--', '--']
        td=cityname.find_next('td')
        price=td.string
        td=price.find_next('td')
        price=price.strip()

        val1=re.search('(\+|\-).*%',td.string)
        if val1:
            val1=td.string
        else:val1='--'
        val1=val1.strip()

        td=td.find_next('td')
        val2=re.search('(\+|\-).*%',td.string)
        if val2:
            val2=td.string
        else:val2='--'
        val2=val2.strip()

        data[cityname]=[price,val1,val2]

        td=td.find_next('td')
        i = i + 1

    return data

if __name__=='__main__':
    print (data_dict(12, 2007))