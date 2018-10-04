# This python file is encoding: utf-8
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from Put_csv_into_pandas_and_make_analysis import save_analysis

# 导入一张表格数据之后，再分成六个地方的表格,这个是用来处理前三个数据缺失年份的数据的
def save_analysis_2(year):
    df = pd.read_csv('data'+str(year)+'.csv', header=None, encoding='gbk')
    df[None] = range(1, 13)
    df.set_index(None, inplace=True, drop=True)
    title = ['城市名称', '平均租金（元/月/平方）', '环比上月', '同比上年']

    df_BJ = df.iloc[:, 1: 5]
    df_BJ.columns = title
    df_BJ.fillna(method='ffill', inplace=True)

    df_CQ = df.iloc[:, 6: 10]
    df_CQ.columns = title
    df_CQ.fillna(method='ffill', inplace=True)

    df_GZ = df.iloc[:, 11: 15]
    df_GZ.columns = title
    df_GZ.fillna(method='ffill', inplace=True)

    df_SH = df.iloc[:, 16: 20]
    df_SH.columns = title
    df_SH.fillna(method='ffill', inplace=True)

    df_SZ = df.iloc[:, 21: 25]
    df_SZ.columns = title
    df_SZ.fillna(method='ffill', inplace=True)

    df_TJ = df.iloc[:, 26: 30]
    df_TJ.columns = title
    df_TJ.fillna(method='ffill', inplace=True)

    # print(df_BJ, '\n',df_BJ.describe())
    # print('')
    # print(df_CQ, '\n',df_CQ.describe())
    # print('')
    # print(df_GZ, '\n', df_GZ.describe())
    # print('')
    # print(df_SH, '\n', df_SH.describe())
    # print('')
    # print(df_SZ, '\n', df_SZ.describe())
    # print('')
    # print(df_TJ, '\n', df_TJ.describe())

    # 创建新的文件夹备用存放分析后的数据文件
    root = 'C:\\Users\chenxi\Desktop\一级城市的房租问题\Save_analysis_' + str(year) + '\\'
    if not os.path.exists(root): os.mkdir(root)

    df_BJ.to_csv('Save_analysis_' + str(year) + '\df_BJ.csv')
    df_BJ.describe().to_csv('Save_analysis_' + str(year) + '\df_BJ_analysis.csv')

    df_CQ.to_csv('Save_analysis_' + str(year) + '\df_CQ.csv')
    df_CQ.describe().to_csv('Save_analysis_' + str(year) + '\df_CQ_analysis.csv')

    df_GZ.to_csv('Save_analysis_' + str(year) + '\df_GZ.csv')
    df_GZ.describe().to_csv('Save_analysis_' + str(year) + '\df_GZ_analysis.csv')

    df_SH.to_csv('Save_analysis_' + str(year) + '\df_SH.csv')
    df_SH.describe().to_csv('Save_analysis_' + str(year) + '\df_SH_analysis.csv')

    df_SZ.to_csv('Save_analysis_' + str(year) + '\df_SZ.csv')
    df_SZ.describe().to_csv('Save_analysis_' + str(year) + '\df_SZ_analysis.csv')

    df_TJ.to_csv('Save_analysis_' + str(year) + '\df_TJ.csv')
    df_TJ.describe().to_csv('Save_analysis_' + str(year) + '\df_TJ_analysis.csv')

    return df_BJ, df_CQ, df_GZ, df_SH, df_SZ, df_TJ

# 画出每年不同城市一个简单的月份房租折线走势图
def simple_monthly_plt(cityname, year, y):
    plt.style.use('ggplot')
    font= FontProperties(fname=r"C:\\WINDOWS\\Fonts\\simsun.ttc")
    x = np.arange(1, 13, 1)
    plt.plot(x, y, marker='o')
    plt.title(str(year)+''+cityname+u'每月走势', fontproperties=font, size=15)
    plt.xlabel('Month', size=10)
    plt.ylabel(u'平均租金（元/月/平方）', fontproperties=font, size=10)
    plt.savefig('C:\\Users\chenxi\Desktop\一级城市的房租问题\Save_plot\\'+str(year)+''+cityname+'.png', dpi= 600)
    plt.show()

# 画出每年六座城市租金均值
def six_bar(year):
    plt.style.use('ggplot')
    font= FontProperties(fname=r"C:\\WINDOWS\\Fonts\\simsun.ttc")
    df_BJ, df_CQ, df_GZ, df_SH, df_SZ, df_TJ = save_analysis_2(year)
    y = [df_BJ.iloc[:,1].mean(), df_CQ.iloc[:,1].mean(), df_GZ.iloc[:,1].mean(),
         df_SH.iloc[:,1].mean(), df_SZ.iloc[:,1].mean(), df_TJ.iloc[:,1].mean()]
    plt.xlabel(u'城市', fontproperties=font, size=15)
    plt.ylabel(u'平均租金（元/月/平方）', fontproperties=font, size=15)
    plt.title(str(year)+u'六个城市的租金均值', fontproperties=font, size=20)
    plt.xticks((0, 1, 2, 3, 4, 5),('BJ', 'CQ', 'GZ', 'SH', 'SZ', 'TJ'))
    plt.bar(left = (0, 1, 2, 3, 4, 5), height = y, color='b', alpha=0.7)
    plt.savefig('C:\\Users\chenxi\Desktop\一级城市的房租问题\Save_analysis_'+str(year)+'\six_bar.png', dpi= 600)
    plt.show()

# 将六条折线放在一张图上
def comparison_2(year):
    plt.style.use('ggplot')
    font= FontProperties(fname=r"C:\\WINDOWS\\Fonts\\simsun.ttc")
    x = np.arange(1, 13, 1)
    df_BJ, df_CQ, df_GZ, df_SH, df_SZ, df_TJ = save_analysis_2(year)

    plt.plot(x, df_BJ.iloc[:, 1], 'ro--', label='BJ')
    plt.plot(x, df_CQ.iloc[:, 1], 'bo--', label='CQ')
    plt.plot(x, df_GZ.iloc[:, 1], 'go--', label='GZ')
    plt.plot(x, df_SH.iloc[:, 1], 'co--', label='SH')
    plt.plot(x, df_SZ.iloc[:, 1], 'yo--', label='SZ')
    plt.plot(x, df_TJ.iloc[:, 1], 'ko--', label='TJ')
    plt.title(str(year)+u'六座城市均值折线图', fontproperties=font, size=15)
    plt.xlabel(u'月份', fontproperties=font, size=10)
    plt.ylabel(u'平均租金（元/月/平方）', fontproperties=font, size=10)
    plt.legend(loc=2)

    plt.savefig('C:\\Users\chenxi\Desktop\一级城市的房租问题\Save_analysis_' + str(year) + '\\' + 'ALL_2.png', dpi=600)
    plt.show()



if __name__=='__main__':
    # df_BJ, df_CQ, df_GZ, df_SH, df_SZ, df_TJ = save_analysis_2(2009)
    # print(simple_monthly_plt('BJ', 2009, df_BJ.iloc[:, 1]))
    # print(simple_monthly_plt('CQ', 2009, df_CQ.iloc[:, 1]))
    # print(simple_monthly_plt('GZ', 2009, df_GZ.iloc[:, 1]))
    # print(simple_monthly_plt('SH', 2009, df_SH.iloc[:, 1]))
    # print(simple_monthly_plt('SZ', 2009, df_SZ.iloc[:, 1]))
    # print(simple_monthly_plt('TJ', 2009, df_TJ.iloc[:, 1]))

    # print(six_bar(2009))

    # print(comparison_2(2009))