# 用一行代码构建一个比较复杂有规律的列表
# l1 = []
# for i in range(1,11):
#     l1.append(i)
# print(l1)
# 列表推导式
l1 = [i for i in range(1,11)]
print(l1)
# 列表推导式分两类
#循环模式：
# 将10以内所有整数的平方写入列表。
# ret = [i**2 for i in range(1,11)]
# print(ret)
# # 100以内所有的偶数写入列表.
# print([i for i in range(2, 101, 2)])

# 从python1期到python100期写入列表lst
# print([f'python{i}期' for i in range(1,101)])

# 筛选模式
# 筛选模式：[变量(加工后的变量) for  变量  in  iterable if 条件]
# 30以内能被3整除的数
# l1 = [i for i in range(1,31) if i%3 == 0]
# print(l1)
# 过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
# l1 = ['barry', 'ab', 'alex', 'wusir', 'xo']
# print([i.upper() for i in l1 if len(i) >= 3 ])

# 含有两个'e'的所有人民留下来
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
l1 = []
for i in names:
    for name in i:
        if name.count('e') == 2: #.count计算字符出现次数
            l1.append(name)
print(l1)
# 第二种
print([name.upper() for i in names for name in i if name.count('e') == 2])


# 生成器表达式与列表推导式的写法几乎一样,将中括号换成小括号
print((i for i in range(1,11)))
# 使用方法
obj = (i for i in range(1,11))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# 全部打印
# for i in obj:
#     print(i)
# 总结：
# 列表推导式：
#   1. 有毒。列表推导式只能构建比较复杂并且比较有规律。
#   2. 超过三层循环才能构建成功的，就不推荐使用。
#   3. 查找排错不行，debug模式。
#   优点：
#       一行构建，简单方便。
print([i for i in range(2,11)] + list('JQKA'))# list将字符串拆分列表

# 字典推导式（了解）
# lst1 = ['jay', 'jj', 'meet']
# lst2 = ['周杰伦','林俊杰','元宝']
# dic = { lst2[i]: lst1[i] for i in range(len(lst1))}
# print(dic)
# 集合推导式（了解）
# print({i for i in range(1,11)})
