# This python file is encoding: utf-8
import pandas as pd
import os

# 导入一张表格数据之后，再分成六个地方的表格
def save_analysis(year):
    df = pd.read_csv('data'+str(year)+'.csv', header=None)
    df[None] = range(1, 13)
    df.set_index(None, inplace=True, drop=True)
    title = ['城市名称', '平均租金（元/月/平方）', '环比上月', '同比上年']

    df_BJ = df.iloc[:, 1: 5]
    df_BJ.columns = title

    df_CQ = df.iloc[:, 6: 10]
    df_CQ.columns = title

    df_GZ = df.iloc[:, 11: 15]
    df_GZ.columns = title

    df_SH = df.iloc[:, 16: 20]
    df_SH.columns = title

    df_SZ = df.iloc[:, 21: 25]
    df_SZ.columns = title

    df_TJ = df.iloc[:, 26: 30]
    df_TJ.columns = title

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
    if not os.path.exists(root):os.mkdir(root)

    df_BJ.to_csv('Save_analysis_'+ str(year) +'\df_BJ.csv')
    df_BJ.describe().to_csv('Save_analysis_'+ str(year) +'\df_BJ_analysis.csv')

    df_CQ.to_csv('Save_analysis_'+ str(year) +'\df_CQ.csv')
    df_CQ.describe().to_csv('Save_analysis_'+ str(year) +'\df_CQ_analysis.csv')

    df_GZ.to_csv('Save_analysis_'+ str(year) +'\df_GZ.csv')
    df_GZ.describe().to_csv('Save_analysis_'+ str(year) +'\df_GZ_analysis.csv')

    df_SH.to_csv('Save_analysis_' + str(year) + '\df_SH.csv')
    df_SH.describe().to_csv('Save_analysis_' + str(year) + '\df_SH_analysis.csv')

    df_SZ.to_csv('Save_analysis_' + str(year) + '\df_SZ.csv')
    df_SZ.describe().to_csv('Save_analysis_' + str(year) + '\df_SZ_analysis.csv')

    df_TJ.to_csv('Save_analysis_' + str(year) + '\df_TJ.csv')
    df_TJ.describe().to_csv('Save_analysis_' + str(year) + '\df_TJ_analysis.csv')

    return df_BJ, df_CQ, df_GZ, df_SH, df_SZ, df_TJ

if __name__=='__main__':
    for year in range(2010, 2017):
        save_analysis(year)
