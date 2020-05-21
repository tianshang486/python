# int 将字符串或数字转换为整数

# float 将字符串或整数转换为浮点数
# i = float(3)
# print(i)
# print(type(3.2))
# complex 转换为复数

# bin：将十进制转换成二进制并返回。  **
# print(bin(100))
# # oct：将十进制转化成八进制字符串并返回。  **
# print(oct(100))
# # hex：将十进制转化成十六进制字符串并返回。  **
# print(hex(100))
# print(hex(10))
# print(hex(13))

# divmod: 计算出整数结果与其余数结果
# print(divmod(10,3))
# round:保留浮点数的小数位
# print(round(3.141592653,2))
# pow：求x**y次函数
# print(pow(2,3))
# print(pow(2,3,4))# 2**3%4

# bytes
# s1 = '翟小龙'
# b = s1.encode('utf-8')
# print(b)
# b = bytes(s1,encoding='utf-8')
# print(b)
# ord:输入字符找该字符编码的位置
# 优先ascii 没有就 Unicode
# print(ord(('a')))
# print(ord('中'))
# chr:输入位置数字找到其对应的字符
# print(chr(97))
# print(chr(10000))

# repr ：返回一个对象的string形式（原形毕露）
# s1 = '太白'
# print(repr(s1))
# a = '翟小龙'
# msg = '翟小龙%r' %(a)
# print(msg)

# all：可迭代对象中，全都是True()才是True,否则就是False(假)
# l1 = [1, 2, '太白', True, [1,2,3], '']
# print(all(l1))
# any：可迭代对象中，有一个True 就是True，否则就是False(假)
# l2 = [ 0, '太白', False, [], '',()]
# print(any(l2))
# print(bool(0))

# print
# print(1,2,3,4,sep='@',end='/') # sep决定输出时候的分隔号，默认为，end决定换行符，默认是换行，改为其他下面的print不会换行将会在一行显示
# print('zxl')
# print(123)
# list 字符串转列表
# print(list('asfihgasof'))

# dict 创建字典的三种方式
# 直接创建
# 元组的结构
# dic = dict([(1,'one'),(2,'two')])
# dic1 = dict(one=1,two=2)
# print(dic,dic1)
# fromkeys
# update
# 字典推导式

# abs() 转换为绝对值，也就是正转负
# print(abs(-6))

# sum求和
# l1 = [i for i in range(10)]
# l2 = [1,2,3,4,5]
# l3 = ['1','2'] # 字符串类型不行
# # l2 = '123456' # 这种不行
# print(sum(l1))
# print(sum(l2))
# print(sum(l3))
# print(sum(l1,100))# ，号后将会在加上

# reversed 翻转返回的是一个新的迭代器，与原列表没关系。
# l1 = [i for i in range(10)]
# l1.reverse()
# print(l1)
# zip 拉链方法,python提供的转换为迭代器方法
# l1 = [1,2]
# l2 = [3,4]
# print(dict(zip(l1,l2)))
# print(list(zip(l1,l2)))
# 对应为相互对应，重新组合按定义类型输出

# min最小 max最大
l1 = [33,4546,546,31.13,4,-2525,54,-3,5,64,13,46,4,31]
# print('最大'+str(max(l1)),'最小'+str(min(l1)))
# l2 = []
# func = lambda a:abs(a)
# for i in l1:
#     l2.append(func(i))
# print(min(l2),max(l2))

# 凡是可以加key的：它会自动的将可迭代对象中的每个元素安装顺序传入key对应的函数中
# def abss(a):
#     return abs(a)
# print(min(l1))
# print(min(l1,key=abss)) # 一定要等于的是函数名
# 上下效果相当
# print(min(l1,key=lambda a:abs(a)))
# 以返回值进行比较
# min和max默认对比字典的键
# 求出字典中值最小的键
# dic = {'a':3,'b':2,'c':1}
# def func(a):
#     return dic[a]
# print(min(dic,key=func))
# 上下效果一样
# print(min(dic,key=lambda a:dic[a]))

# 元组
# l2 = [('太白',18),('alex',73),('wusir',34)]
# print(min(l2,key=lambda x:x[1]))

# sorted 从小到大排序，输出新的列表，可以加key
# l1 = [22,33,1,2,8,7,6,5]
# l2 = sorted(l1)
# print(l1)
# print(l2)
# 字典和元组需要加入条件来进行使用
# l2 = [('dazhuang',76),('xuefei',70),('zhangchen',100)]
# print(sorted(l2,key=lambda x:x[1]))
# print(sorted(l2,key=lambda x:x[1],reverse=True)) # 增加这个参数居就是从高到低

# filter 列表推导式的筛选模式
# l1 = [2,3,4,1,6,7,8]
# print([i for i in l1 if i > 3]) # 返回列表
# 上下效果一样，那个方便用那个
# ret = filter(lambda x:x > 3,l1) # 返回迭代器
# print(ret)
# print(list(ret))

# map 列表推导式的循环模式
# l1 = [1,4,9,16,25] # 得出这个
# print([i**2 for i in range(1,6)])
# # 上下区别与filter一样
# ret = map(lambda x:x**2,range(1,6))
# print(ret)
# print(list(ret))

# reduce
# from functools import reduce
# def func(x,y):
#     # return x + y # 相对于先 1+2=x 在 x+3=y  在 y+4=最后结果
#     return x*10 + y # 相对于先1*10+2=x 在 x*10+3=y 在y*10+4=最后结果
# l = reduce(func,[1,2,3,4])
# print(l)