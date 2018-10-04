# This python file is encoding: utf-8
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from Put_csv_into_pandas_and_make_analysis import save_analysis

# 画出每年六座城市租金均值
def six_bar(year):
    plt.style.use('ggplot')
    font= FontProperties(fname=r"C:\\WINDOWS\\Fonts\\simsun.ttc")
    df_BJ, df_CQ, df_GZ, df_SH, df_SZ, df_TJ = save_analysis(year)
    y = [df_BJ.iloc[:,1].mean(), df_CQ.iloc[:,1].mean(), df_GZ.iloc[:,1].mean(),
         df_SH.iloc[:,1].mean(), df_SZ.iloc[:,1].mean(), df_TJ.iloc[:,1].mean()]
    plt.xlabel(u'城市', fontproperties=font, size=15)
    plt.ylabel(u'平均租金（元/月/平方）', fontproperties=font, size=15)
    plt.title(str(year)+u'六个城市的租金均值', fontproperties=font, size=20)
    plt.xticks((0, 1, 2, 3, 4, 5),('BJ', 'CQ', 'GZ', 'SH', 'SZ', 'TJ'))
    plt.bar(left = (0, 1, 2, 3, 4, 5), height = y, color='b', alpha=0.7)
    plt.savefig('C:\\Users\chenxi\Desktop\一级城市的房租问题\Save_analysis_'+str(year)+'\six_bar.png', dpi= 600)
    plt.show()

if __name__=='__main__':
    for i in range(2010, 2017):
        six_bar(i)