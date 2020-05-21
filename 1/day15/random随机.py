# 此模块提供了和随机数获取相关的方法
# random.random():获取(0.0,1.0)范围内的随机浮点数
# random.randint(a,b)范围内的一个随机整数
# random.uniform(a,b):获取(a,b)范围内的浮点数
# random.shuffle(x):把参数指定的数据中的元素打乱。参数必须是一个可变数据
# random.sample(x,k):从x中随机抽取k个数据，组成一个列表返回
x = [1,2,'zxl','zjb']
y = '123456'
z = {'name':'zxl' ,'age':18,'user':'zjb'}
import random
print(random.sample(x,2))
print(random.sample(y,2))
# print(random.sample(z,2)) # 字典不行，其他都可以
print(random.random())
print(random.randint(1,100))
print(random.uniform(1,10))
a = [1,2,'zxl','zjb',19,1000,'taibai',("kkk","bbb")]
random.shuffle(a)
print(a)