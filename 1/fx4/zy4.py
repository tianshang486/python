# 1.写代码，有如下列表，按照要求实现每一个功能
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# 计算列表的长度并输出
print(len(li))
# 列表中追加元素"seven",并输出添加后的列表
li.append('seven')
print(li)
# 请在列表的第1个位置插入元素"Tony",并输出添加后的列表
li.insert(0,'Tony')
print(li)
# 请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
li[1] = 'kelly'
print(li)
# 请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
l2 = [1,"a",3,4,"heart"]
li = li + l2
print(li)
# 请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
s = "qwert"
# li.extend(s)
# print(li)

li = li + list(s)
print(li)
# 请删除列表中的元素"ritian",并输出添加后的列表
li.remove('ritian')
print(li)
# 请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
li.pop(1)
print(li)
# 请删除列表中的第2至4个元素，并输出删除元素后的列表
del li[1:4]
print(li)
# 删除最后两个
del li[-1:-3:-1]
print(li)
# 2.写代码，有如下列表，利用切片实现每一个功能
li = [1, 3, 2, "a", 4, "b", 5,"c"]
# 通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
l1 = li[0:3]
print(l1)
# 通过对li列表的切片形成新的列表l2,l2 = ["a",4,"b"]
l2 = li[3:6]
print(l2)
# 通过对li列表的切片形成新的列表l3,l3 = ["1,2,4,5]
l3 = li[::2]
print(l3)
# 通过对li列表的切片形成新的列表l4,l4 = [3,"a","b"]
l4 = li[1:-2:2]
print(l4)
# 通过对li列表的切片形成新的列表l5,l5 = ["c"]
l5 = li[-1:-2:-1]
print(l5)
# 通过对li列表的切片形成新的列表l6,l6 = ["b","a",3]
l6 = li[-3:0:-2]
print(l6)
# 3.写代码，有如下列表，按照要求实现每一个功能。
lis = [2, 30, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# 将列表lis中的"tt"变成大写（用两种方式）。
# 第一种
lis[3][2][1][0].upper()
print(lis)
# 第二种
lis[3][2][1][0] = 'TT'
print(lis)
# 将列表中的数字3变成字符串"100"（用两种方式）。
# 第一种
# lis[3][2][1][1] = '100'
# print(lis)
# 第二种
lis[3][2][1].pop(1)
lis[3][2][1].insert(1,'100')
print(lis)
# 将列表中的字符串"1"变成数字101（用两种方式）。
# 第一种
lis[3][2][1][2] = '101'
print(lis)
# 第二种
lis[3][2][1].pop(2)
lis[3][2][1].insert(2,'101')
print(lis)
# 4.请用代码实现：
li = ["alex", "wusir", "taibai"]
# 利用下划线将列表的每一个元素拼接成字符串"alex_wusir_taibai"
# 第一种
# li = '_'.join(li)
# print(li)
# 第二种
# l1 = ''
# for i in li:
#     l1 = l1 + "_" + i
# print(l1[1:])
# 5.利用for循环和range打印出下面列表的索引。
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
for i in range(0,len(li)):
    print(i)
# 6.利用for循环和range找出100以内所有的偶数并将这些偶数插入到一个新列表中。
li = []
for i in range(1,101):
    if i % 2 == 0:
        li.append(i)
print(li)
# 7.利用for循环和range 找出50以内能被3整除的数，并将这些数插入到一个新列表中。
li = []
for i in range(1,51):
    if i % 3 == 0:
        li.append(i)
print(li)
# 8.利用for循环和range从100~1，倒序打印。
for i in range(100,0,-1):
    print(i)
# 9.利用for循环和range从100~10，倒序将所有的偶数添加到一个新列表中，然后对列表的元素进行筛选，将能被4整除的数留下来。
li = []
for i in range(100,9,-1):
    li.append(i)
    for i1 in li:
        if i1 % 4 == 0:pass
        else:
            li.remove(i1)
print(li)
# 10.利用for循环和range，将1-30的数字一次添加到一个列表中，并循环这个列表，将能被3整除的数改成*。
#
# 11.查找列表li中的元素，移除每个元素的空格，并找出以"A"或者"a"开头，并以"c"结尾的所有元素，并添加到一个新列表中,最后循环打印这个新列表。
l1 = []
li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", " aqc"]
for i in li:
    if i.strip().startswith('A'and'a') and  i.strip().endswith('c'):
        l1.append(i.strip())
print(l1)

# 12.开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符：
# 敏感词列表 i = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# 则将用户输入的内容中的敏感词汇替换成等长度的*（苍老师就替换***），并添加到一个列表中；如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。
# i = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# a = input('请输入评论：')
# for index in i:
#     if index in a:
#         a = a.replace(index,('*' * len(index)))
# print(a)
# 13.有如下列表（选做题）
li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
# 循环打印列表中的每个元素，遇到列表则再循环打印出它里面的元素。
# 我想要的结果是：
# 1
# 3
# 4
# "alex"
# 3
# 7,
# 8
# "taibai"
# 5
# ritian
for i1 in li:
    if type(i1) == list:
        for i2 in i1:
            print(i2)
    else:print(i1)

# 明日默写内容
# 将列表的增删改查不同的方法全部写出来，
li= [4,5,6]
li.append(1)
li.insert(1,9)
li.extend('abcdef')
li.pop(0)
li.remove(9)
del li[-1:-4]
li[2] = 'zxl'
li[5:-1] = 'afhpao'
print(li)
li[::2] = 'abcdef'
print(li)
# 例如：增：有三种，append：在后面添加。Insert按照索引添加，
# expend：迭代着添加。