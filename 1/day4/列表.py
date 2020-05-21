li = [100,'翟小龙',True,[1,2,3]]
# 索引
print(li[0],type(li[0]))
print(li[-1],type(li[-1]))
print(li[:2])
print(li[:-4:-1])
print(li[:4:2])
print(li[:-5:-2])
# 列表的创建
# 方式一
li = [100,'翟小龙',True,[1,2,3]]
# 方拾二
li = list()
print(li)
li = list('asbnvlabsdvk')
print(li)

# 方式三：列表推导式 后面讲

# 增删查改
l1 = ['小强','小明','小王','xiaowu','小明']
# 增
# append：追加
l1.append('xx')
print(l1)
print(l1.append('xx')) # 不能打印他
print(l1)

# 举例：
l2 = ['小强','小明','小王','xiaowu','小明']
while 1:
    name = input('请输入新员工姓名：(Q或者q退出程序)')
    if name.upper() == 'Q':break
    l2.append(name)
print(l2)

# insert 插入：直接插入指定步数内，原步数及以后都往后退一步
l3 = ['小强','小明','小王','xiaowu','小明']
l3.insert(2,'lala')
print(l3)
# extend 迭代追加
l4 = ['小强','小明','小王','xiaowu','小明']
l4.extend('ggggggg')
print(l4)
l4.extend(['alex,'])
print(l4)
print(l4)
l4.extend(['alex,1,2'])
print(l4)

# 删
# pop 按照索引删除

l5 = ['小强','小明','小王','xiaowu','小明']
print(l5.pop(-2))
print(l5)
l5.pop() #默认最后一个
print(l5)

# remove 指定元素删除
l5 = ['小强','小明','小王','xiaowu','小明']
l5.remove('xiaowu')
print(l5)
l5.remove('小明')
print(l5) # 有重名从左至右第一个删除

# clear清空
l5.clear()
print(l5)

# del:按照索引删除
l6 = ['小强','小明','小王','xiaowu','小明']
del l6[-1]
print(l6)

# 按照切片删除

l6 = ['小强','小明','小王','xiaowu','小明']
del l6[::2]
print(l6)
l6 = ['小强','小明','小王','xiaowu','小明']
del l6[:5:2]
print(l6)

# 改
# 按照索引改

l7 = ['小强','小明','小王','xiaowu','小明']
l7[0] = '小八'
print(l7)
# 按照切片改
l7[2:] = 'ifgafiagfpiagfapifgaile'
print(l7)
# 安装切片步长
l7 = ['小强','小明','小王','xiaowu','小明']
l7[::2] = 'abc' # 不能多，不能少
print(l7)
l7 = ['小强','小明','小王','xiaowu']
l7[::2] = 'ab'
print(l7)
l7 = ['小强','小明','小王','xiaowu']
for i in l7:
    print(i)


# 列表嵌套（重点）
# 将xao改为大写
l1 = [1,2,'xao',[1,'alex',3,]] # 第一种
l1[2] = 'XAO'
print(l1)
l1 = [1,2,'xao',[1,'alex',3,]] # 第二种
l1[2] = l1[2].upper()
print(l1)

# 给小列表追加一个元素：哈哈哈哈
l1 = [1,2,'xao',[1,'alex',3,]]
l1[-1].append('哈哈哈哈')
print(l1)

# 将小列表中的alex后加sb
l1 = [1,2,'xao',[1,'alex',3,]]
l1[-1][1] = l1[-1][1] + 'sb'
print(l1)

lis = [2,'k',['qwe',20,['k1',['tt',3,'1']],89],'ab','adv']
# 将lis中tt改成大写
# lis[2][2][1][0] = lis[2][2][1][0].upper()
# print(lis)
# 将数字3变成字符串'100'
# lis[2][2][1][1] = '100'
# print(lis)
# 将列表中的字符串'1'变成数字101
lis[2][2][1][2] = 101
print(lis)

# 元组
# 只读列表，与普通列表不一样就是不能增删改
tu = (100,'xia','小王',[1,2,3])
print(tu[1])
print(tu[::])

for i in tu:
    print(i)
print(len(tu))# 有多少个元素
del tu[3][0] # 元组里面的列表可以增删改
print(tu)

# 应用
# 重要数据，不让不让改的，可以用元组
# 元组的拆包
# 不能多不能少，
a,b = (1,2)
print(a,b)
# 列表也可以拆包，但一般用元组

# range ：类似列表，只能为自己可以控制的数字
# 顾头不顾尾，只能从零到指定数字的前一个
r = range(10)
print(r)
for i in r:
    print(i)

# for i in range(1,101):print(i)
# f# 打or i in range(2,101,2):print(i) # 打印偶数

# for i in range(1,100,2):print(i) 印计数

# for i in range(100,0,-1):print(i) # 反向从100到1

l1 = [1,2,3,'alex','太白']
# 利用for循环，利用range将列表的所有索引依次打印出来

for i in range(len(l1)):print(i) # len 将列表索引打印出(l11
for i in range(len(l1)):pass
print(i) # 直接打印最后一个索引得出有都是个元素

l1 = range(5)

print(l1[1:3])
print(l1[-1])
for i in range(5,1,-1):
    print(i)

content = input('请输入内容')
l1 = content.split('+')
print(l1)
# 字符串不能进行计算，所以转换为int整数格式
result = int(l1[0])+int(l1[1])
print(result)

content = input('请输入内容')
s1 = 0
l2 = content.split('+')
print(l2)
for i in l2:
    s1 += int(i)
print(s1)


content = input('请输入内容')
s1 = 0
for i in content:
    print(i,type(i))
    if i.isdecimal():
        s1 += 1
print(s1)
#

s1 = 0
while s1 < 10:
    content = input('请输入：')
    if content == content[::-1]:
        print('是回文')
    else:
        print('不是回文')
    s1 += 1
else:
    print('结束')

li = [1,3,2,'a',4,'b',5,'c']
print(li[-1])

