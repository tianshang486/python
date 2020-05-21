# str
str = 'taibai'
# capitalize() 首字母大写，其余变小写
print(str.capitalize())
# swapcase() 大小写翻转
print(str.swapcase())

msg = 'taibai si sb'
# title() 字符串的每个首字母大写
print(msg.title())

s1 = 'taibai'
# center 居中，并左右按照指定字符填充
print(s1.center(20,'*'))
# find 通过元素查找到第一个就返回索引
print(s1.find('a'))
# index 和find相似，但查找不到就报错
# print(s1.index('0'))

# tuple 元组
# 元组中只有一个元素并且没有单号，那么他不是元组
# 他与该元素的数据类型一致。
tu1 = (2,3,4)
print(tu1,type(tu1))
tu1 = (1)
print(tu1,type(tu1))
tu1 = (0,1,2,3,4,5,6,7,8,9)
# 计数，该字符总共在元组中有多少个
print(tu1.count(3))
# index 查找
print(tu1.index(5))
# print(tu1.index(10))

# list

# 元组有的列表一般也有
# sort 从小到大排序
l1 = [10,9,54,6,1,3,4,5]
l1.sort()
# sort.(reverse=True) 从大到小排序
# revese() 反转,将原排列循序翻转排序
l1.reverse()
print(l1)
l2 = [44,55]
# 列表可以相加
print(l1 + l2)
# 列表可以与数字相乘
print(l2*8)

l1 = [11,22,33,44,55]
# 将索引为奇数对应的元素删除，不能一个一个删除
# 做法错误，将前面删除后，后面元素索引也会发生改变
# for i in range(len(l1)):
#     if i % 2 == 1:
#         l1.pop(i)
# print(l1)
# 正确做法
del l1[1::2]
print(l1)
# 倒序法删除元素
l1 = [11,22,33,44,55]
for i in range(len(l1)-1,-1,-1):
    if i%2 == 1:
        l1.pop(i)
print(l1)
l1 = [11,22,33,44,55]
new = []
# 直接加入空列表
for i in range(len(l1)):
    if i % 2 == 0:
        new.append(l1[i])
print(new)

# 字典
# 默认删除最后一个，作用不大

# 增加键值对，也可以改
dic = {'name':'zxl' , 'age':'18'}
dic.update(hobby='云动')


# fromkeys 拆解字符串，每一个元素为一个键，共用同一个元素
dic = dic.fromkeys('abc',100)
print(dic)
dic = dict.fromkeys([1,2,3],[])
dic[1].append(666)
# 更改一个，每一个都发生改变
print(dic)








