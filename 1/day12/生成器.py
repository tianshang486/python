# 生成器的本质就是迭代器，唯一的区别生成器是我们自己用Python代码构建的数据结构，迭代器都是提供的或者转化得来的
# 获取生成器的三种方式：
# 1. 生成器函数
# 2. 生成器表达式
# 3. python内部提供的一些
# 生成器函数获得一个生成器：
# def func():
#     print(111)
#     print(222)
#     yield 3
#     a = 3
#     b = 2
#     c = a + b
#     print(c)
#     yield 4
# ret = func()
# print(next(ret))
# print(next(ret))

# return yield
# return: 函数中只有一个return有用，结束函数，并且给函数的执行者返回值
# yield： 只要函数中有yield那么他就是生成器函数而不是函数了
# 生成器函数中可以存在多个yield，一个yield对应一个next。
# 自己构建一个迭代器也就是生成器
# def func(): # 不用迭代器时候
#     l1 = []
#     for i in range(1,2001):
#         l1.append(f'{i}号包子')
#     return l1
# ret = func()
# print(ret)

# 自己构建生成器
# def baoz():
#     for i in range(1,2001):
#         yield f'{i}号包子'
# ret =  baoz()
# for i in range(200):
#     print(next(ret))
# 迭代器的惰性机制，在代码结束前会保留上一次位置
# for i in range(100):
#     print(next(ret))

# yield from

# def func():
#     l1 = [1,2,3,4,5]
#     yield from l1 # from 将列表拆分，一个next对应列表中的一个元素
# ret = func()
# print(next(ret))
# print(next(ret))
# print(next(ret))
# print(next(ret))
# print(next(ret))

def func():
    l1 = [1,2,3,4,5]
    l2 = [6,7,8,9,10]
    yield from l1
    yield from l2
ret = func()
for i in ret:
    print(i)

# 生成器是自己构建，迭代器是转化，生成器就是迭代器。