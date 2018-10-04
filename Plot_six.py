# This python file is encoding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from Put_csv_into_pandas_and_make_analysis import save_analysis

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

if __name__=='__main__':
    for i in range(2010, 2017):
        df_BJ, df_CQ, df_GZ, df_SH, df_SZ, df_TJ = save_analysis(i)
        print(simple_monthly_plt('BJ', i, df_BJ.iloc[:, 1]))
        print(simple_monthly_plt('CQ', i, df_CQ.iloc[:, 1]))
        print(simple_monthly_plt('GZ', i, df_GZ.iloc[:, 1]))
        print(simple_monthly_plt('SH', i, df_SH.iloc[:, 1]))
        print(simple_monthly_plt('SZ', i, df_SZ.iloc[:, 1]))
        print(simple_monthly_plt('TJ', i, df_TJ.iloc[:, 1]))