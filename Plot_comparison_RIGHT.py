# This python file is encoding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from Put_csv_into_pandas_and_make_analysis import save_analysis

# 将六条折线放在一张图上
def comparison_2(year):
    plt.style.use('ggplot')
    font= FontProperties(fname=r"C:\\WINDOWS\\Fonts\\simsun.ttc")
    x = np.arange(1, 13, 1)
    df_BJ, df_CQ, df_GZ, df_SH, df_SZ, df_TJ = save_analysis(year)

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
    for i in range(2010, 2017):
        comparison_2(i)