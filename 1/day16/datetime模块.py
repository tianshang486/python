import datetime
# # date类：
# d = datetime.date(2010,10,10)
# print(d)
# # 获取date对象的各个属性
# print(d.year)
# print(d.month)
# print(d.day)
# # time类：
# t = datetime.time(10,48,15)
# print(t.hour)
# print(t.minute)
# print(t.second)
#
# # datetime
# dt = datetime.datetime(2010,11,10,9,15,20)
# print(dt)
#
# # datetime中的类，主要是用于数学计算的
# # timedelta：时间变化量
# td = datetime.timedelta(days=1)
# print(td)
# # 参与数学运算
# # 创建时间对象：
# # date，datetime，timedelta
# ddt = datetime.date(2010,10,10)
# res = td + ddt
# rse = ddt - td
# print(res)
# print(rse)
#
# # 时间变化量的计算是否会产生进位？
# t = datetime.datetime(2010,10,10,10,10,59)
# ttd = datetime.timedelta(seconds=3)
# ress = t + ttd
# print(ress)
# # 验证会产生进位

# 练习：计算某一年的二月份有多少天
# 普通算法：根据年份计算是否是闰年
# 用datetime模块
# 首先创建出指定年份的3月1号。
year = int(input('输入年份：'))
# 创建指定年份的date对象
d = datetime.date(year,3,1)
# 创建一天的时间段
td = datetime.timedelta(days=1)
res = d - td
print(res.day)

# 和时间段进行运算结果是什么类型
d1 = datetime.date(2010,10,10)
d2 = datetime.datetime(2010,10,10,10,10,10)
d3 = datetime.timedelta(seconds=20)
d3 = datetime.timedelta(seconds=20)
d4 = datetime.date(2010,10,10)
td = datetime.timedelta(days=1)
td4 = datetime.timedelta(seconds=20)
res1 = d1-td
res2 = d2-td
res3 = d3-td
res4 = d4+td4
print(type(res1))
print(type(res2))
print(type(res3))
print(type(res4))
