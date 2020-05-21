# 获取所有迭代对象的方法
# s1 ='abc123'
# print(dir(s1))
# l1 = [1,2,3]
# print(dir(l1))
# 判断是不是一个对象
# print('__iter__' in dir(s1))# in 的作用就是判断前面字符串在后面的数值里面
# next 用于显示结果，迭代器与生成器都需要
# 利用while循环模拟for循环对可迭代对象进行取值的机制
l1 = [1,2,3,4,5,6,7,8,9,10,11,12]
# 将可迭代对象转化为迭代器
obj = iter(l1)# 转换
while 1:
    try:
        print(next(obj))
    except StopIteration:
        break