a = 1
b = a
a = 13
print(a)
print(b)
a = 13
print(a,b)
# 请用代码验证name"是否在字典的键中？
# in 判断是否字典列表中有无这个键
info = {'name': '王刚蛋', 'hobby': '铁锤', 'age': '18','s':'alex'}
# print('name' in info)
# print('name' in info.keys())
#
#
# 请用代码验证
# "alex"
# 是否在字典的值中？
# print('alex' in info.values())
# info = {'name': '王刚蛋', 'hobby': '铁锤', 'age': '18',..
# .100
# 个键值对}
# 有如下
#
# v1 = {'武沛齐', '李杰', '太白', '景女神'}
# v2 = {'李杰', '景女神}
#       请得到 v1 和 v2 的交集并输出
#       请得到 v1 和 v2 的并集并输出
#       请得到 v1 和 v2 的 差集并输出
#       请得到 v2 和 v1 的 差集并输出
#  循环提示用户输入，并将输入内容追加到列表中（如果输入N或n则停止循环）
# l1 = []
# while 1:
#     content = input('>>>')
#     if content.upper() == 'N': break
#     l1.append(content)
# print(l1)
# 循环提示用户输入，并将输入内容添加到集合中（如果输入N或n则停止循环）
#
# 写代码实现
#
# v1 = {'alex', '武sir', '肖大'}
# v2 = []
#
# # 循环提示用户输入，如果输入值在v1中存在，则追加到v2中，如果v1中不存在，则添加到v1中。（如果输入N或n则停止循环）
# 判断以下值那个能做字典的key ？那个能做集合的元素？
#
# 1
# - 1
# ""
# None
# [1, 2]
# (1, )
# {11, 22, 33, 4}
# {'name': 'wupeiq', 'age': 18}
# is 和 == 的区别？
#
# type使用方式及作用？
#
# id的使用方式及作用？
#
# 看代码写结果并解释原因
#
# v1 = {'k1': 'v1', 'k2': [1, 2, 3]}
# v2 = {'k1': 'v1', 'k2': [1, 2, 3]}
#
# result1 = v1 == v2
# result2 = v1 is v2
# print(result1)
# print(result2)
# 看代码写结果并解释原因
#
# v1 = {'k1': 'v1', 'k2': [1, 2, 3]}
# v2 = v1
#
# result1 = v1 == v2
# result2 = v1 is v2
# print(result1)
# print(result2)
# 看代码写结果并解释原因
#
# v1 = {'k1': 'v1', 'k2': [1, 2, 3]}
# v2 = v1
#
# v1['k1'] = 'wupeiqi'
# print(v2)
# 看代码写结果并解释原因
#  变量指向的是真真实实的数据。
# v1 = '好嗨哟'
# v2 = [1, 2, 3, 4, v1]  # v2[-1] = v1
# v1 = "人生已经到达了巅峰"
# print(v2)
# age1 = 12
# age2 = age1
# age3 = age2
# age2 = 18
# print(age1,age2,age3)


# 看代码写结果并解释原因
#
# info = [1, 2, 3]
# userinfo = {'account': info, 'num': info, 'money': info}
# #
# # info.append(9)
# # print(userinfo)
# #
# info = "题怎么这么多"
# print(userinfo)
# 看代码写结果并解释原因
#
# info = [1, 2, 3]
# userinfo = [info, info, info, info, info]
#
# info[0] = '不仅多，还特么难呢'
# print(info, userinfo)
# 看代码写结果并解释原因
# #
# info = [1, 2, 3]
# userinfo = [info, info, info, info, info]
#
# userinfo[2][0] = '闭嘴'
# print(info, userinfo)
# 看代码写结果并解释原因
#
# info = [1, 2, 3]
# user_list = []
# for item in range(10):
#     user_list.append(info)
# #user_list = [info, info, info, info, info,info, info, info, info, info]
# info[1] = "是谁说Python好学的？"
# print(user_list)

# 看代码写结果并解释原因
#
# data = {}
# for i in range(10):
#     data['user'] = i
# print(data)
# 看代码写结果并解释原因
#
# data_list = []
# for i in range(10):
#     data = {}
#     data['user'] = i
#     data_list.append(data)
#     '''
#     第一次： data = {'user': 0}
#     data_list = [{'user': 0},]
#     第二次： data = {'user': 1}
#     data_list = [{'user': 0},{'user': 1}]
#     '''
# print(data_list)


# data_list = []
# data = {}
# for i in range(10):
#     data['user'] = i
#     data_list.append(data)
#     '''
#     第一次： data = {'user': 0}
#     data_list = [{'user': 0},]
#     第二次： data = {'user': 1}
#     data_list = [{'user': 0},{'user': 1}]
#     '''
# print(data_list)



# 看代码写结果并解释原因
#
data_list = []
data = {}
for i in range(10):
    data['user'] = i
    data_list.append(data)
print(data_list)
# 使用循环打印出一下效果：
#
# *
# **
# ** *
# ** **
# ** ** *

# for i in range(0,10):
#     a = ''
#     a = ('*' * i)
#     print(a)

# for d in range(9,-1,-1):
#     b = ''
#     b = ('*' * d)
#     print(b)

# ** **
# ** *
# **
# *
# *
# ** *
# ** ** *
# ** ** ** *
# ** ** ** ** *
# 敲七游戏.从1开始数数.遇到7或者7的倍数（不包含17, 27, 这种数）要在桌上敲⼀下.编程来完成敲七.给出⼀个任意的数字n.从1开始数.数到n结束.把每个数字都放在列表中, 在数的过程中出现7或
# 者7的倍数（不包含17, 27, 这种数）.则向列表中添加⼀个
# '咣'
#
# 例如, 输⼊10.
# lst = [1, 2, 3, 4, 5, 6, '咣', 8, 9, 10]
a = int(input('输入'))
lst = []
for i in range(1,a+1):
    if i%7 == 0:
        lst.append('啊')
    else:
        lst.append(i)
print(lst)