# 默认参数的陷阱
# def func(name,sex='男'):
#     print(name)
#     print(sex)
# func('alex') # 位置参数，所以name被替换
# 陷阱只针对默认参数能改变的参数
# def func(name,alist=[]):
#     alist.append(name)
#     return alist
# ret = func('alex')
# print(ret)
# ret2 = func('太白金星')# alist是个列表，所以加入的内容及时函数结束了，加入的值并不会消失
# print(ret2)

# def func(a,list=[]):
#     list.append(a)
#     return list
# print(func(10,))
# print(func(20,[])) # 调用这个时候将创建一个新列表，
# print(func(100,)) # 掉用这个并为使用新列表，加入的还是第一个

# def func(a,list=[]):
#     list.append(a)
#     return list
# ret1 = func(10,)
# ret2 = func(20,[])
# ret3 = func(100,)
# print(ret1)
# print(ret2)
# print(ret3)
# 1 和 3 公佣同一个同一个内存地址，所以一起改变成一样

# 局部作用域的坑

# count = 1
# def func():
#     count += 1
#     print(count)
# 只能调用不能改变，所以识别不到，所以报错
# func()
# 在函数中，如果你定义一个变量，但是定义这个变量之前引用了，那么解释器认为，语法问题。
# def i():
#     print(count)
#     count = 10
# i()

# global nonlocal

# global
# 1， 在局部作用域声明一个全局变量
# name = 'alex' # 将其注释掉，就会找不到，因为直接全局调用，找不到局部关键字。
# def func():
#     global name
#     name = '太白金星'
#     print(name)
# func()
# print(name)
# 2. 修改全局变量
# name = 1
# def func():
#     global name
#     name += 1
#     print(name)
# print(name)
# func()

# nonlocal
# 1. 不能够操作全局变量
# count = 1
# def func():
#     nonlocal count
#     count += 1
# func()
# 2. 局部作用域：内层函数对外层函数的局部变量进行修改
def wrapper():
    count = 1
    def inner():
        nonlocal count # 可以对上面的局部进行声明
        print(count)
        count += 1
        print(count)
    inner()
wrapper()