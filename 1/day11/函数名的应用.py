# def func():
#     print(666)
# func()

# 1. 函数名指向的是函数的内存地址
# 函数名 +（） 就可以执行一次函数
# print(func,type(func)) #<function func at 0x00BAA3D0> <class 'function'>
# func()
# func是个变量，作用只是指向内存地址

# 2. 函数名（func） 就是个变量
# def func():
#     print(666)
# def func1():
#     print(888)
# func1 = func
# func1()
# 函数名可以作为容器类数据类型元素
# def func():
#     print(666)
# def func1():
#     print(888)
# def func2():
#     print(999)
# l1 = [func,func1,func2]
# for i in l1:
#     i()
# 4. 函数名可以作为函数的参考数
# def func(a):
#     print(a)
#     print('10')
# b = 3
# func(b)

# def func():
#     print('999')
# def func1(x):
#     x()
#     print('9991')
# func1(func)

# 5. 函数名可以作为函数的返回值
def func():
    print(666)
def func1(x):
    print(888)
    return x
ret = func1(func)
ret()
