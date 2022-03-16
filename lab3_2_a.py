import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\灵耀S2\\大三实验资料\\鸢尾花数据\\data/某门课程平时成绩和期末考试成绩.csv")
# print('打印读取到的成绩：\n',df.head())

df_list = []
df_ps = []
df_qm = []
for i in range(len(df)):
    df_list.append({'姓名':df['姓名'][i],'平时成绩':df['平时成绩'][i],'期末成绩':df['期末成绩'][i]})
    df_ps.append(df_list[i]['平时成绩'])
    df_qm.append(df_list[i]['期末成绩'])
print(df_list)
# print(df_ps)
# print(df_qm)

print('平时成绩的均值：',np.std(df_ps))
print('平时成绩的标准差：',np.std(df_ps))
print('平时成绩的方差：',np.var(df_ps))
print('平时成绩的最小值：',np.min(df_ps))
print('平时成绩的最大值：',np.max((df_ps)))

print('期末成绩的均值：',np.std(df_qm))
print('期末成绩的标准差：',np.std(df_qm))
print('期末成绩的方差：',np.var(df_qm))
print('期末成绩的最小值：',np.min(df_qm))
print('期末成绩的最大值：',np.max((df_qm)))

df_qm_ps = []
for j in range(len(df)):
    if df_list[j]['期末成绩'] > df_list[j]['平时成绩']:
        df_qm_ps.append(df_list[j]['姓名'])
# print('期末考试比平时成绩高的学生名单:\n',df_qm_ps)

df_qm_ten = []
df_qm_ten_zan_qm = []
df_qm_ten_zan_ps = []
df_qm_argsort = np.argsort(df_qm)[-10:]
print(df_qm_argsort)

for i in df_qm_argsort:
    # print(i)
    df_qm_ten_zan_qm.append(df_list[i]['期末成绩'])
    df_qm_ten_zan_ps.append(df_list[i]['平时成绩'])
    ind = np.lexsort((df_qm_ten_zan_ps, df_qm_ten_zan_qm))
for i in df_qm_argsort[ind]:
    # print(i)
    df_qm_ten.append(df_list[i]['姓名'])
print('期末考试排名前10名的学生:',df_qm_ten[::-1])
