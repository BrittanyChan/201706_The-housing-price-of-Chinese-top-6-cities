# -*- encoding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
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
def data_list(month, year):
    data_list = []
    html = put_url(month, year)
    soup = BeautifulSoup(html, 'html.parser')
    soup1 = soup.find('tbody', attrs={'id':'order_f'})
    city = soup1.find_all('td')
    for i in city:
        city_detail = i.string.strip()
        data_list.append(city_detail)
    return data_list

# 把爬下来的每年的具体数据分别放入不同的csv中并以年份命名好
def put_into_csv(year):
    data = []
    csvFile = open('C:\\Users\chenxi\Desktop\一级城市的房租问题\data'+str(year)+'.csv', 'w+', newline='', encoding='utf-8')
    writer = csv.writer(csvFile)
    for month in range(1, 13):
        data.append(data_list(month, year))
    for each_data in data:
        writer.writerow(each_data)
    csvFile.close()

# 进行调用，以年份命名存好
if __name__=='__main__':
    for year in range(2007, 2017):
        print (put_into_csv(year))
        time.sleep(8)