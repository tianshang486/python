# 装饰器：
# 开放封闭原则
# 开放：对代码的拓展开放的。比如游戏：更新地图，加入枪或者角色
# 封闭：对源码的修改是封闭的。比如吃鸡，游戏是枪战游戏是不会改变

# 装饰器：完全遵循开放封闭原则。
# 装饰器：在不改变原函数的代码以及调用方式的前提下，为其增加新功能

# 版本1：写一些代码测试一下index函数的执行效率。
# def index():
#     '''
#     有很多代码
#     '''
#     print('欢迎登陆博客园')
#
# def dariy():
#     '''有很多代码'''
#     time.sleep(3)
#     print('欢迎登陆日记')
# 版本1有问题：如果测试别人代码，必须重新复制粘贴，改一些代码
import time
# print(time.time()) # 格林威治时间
#
# start_time = time.time()
# index()
# end_time = time.time()
# print(end_time-start_time)

# start_time = time.time()
# dariy()
# end_time = time.time()
# print(end_time-start_time)

# 版本2：利用函数解决代码重复使用问题
# def index():
#     '''有很多代码'''
#     time.sleep(2)
#     print('欢迎登陆博客园')
# index()
# def dariy():
#     '''有很多代码'''
#     time.sleep(3)
#     print('欢迎登陆日记')
#
# def timmer(f):
#     start_time = time.time()
#     f()
#     end_time = time.time()
#     print(f'测试本函数的执行效率{end_time-start_time}')
# timmer(index)

# 版本2还是有问题：原来index函数源码没有变化，给原函数添加一个新的功能测试原函数的执行效率功能
# 满足开放封闭原则么?原函数的调用方式改变了.

# 版本三：不能改变原函数调用方式。

# def timmer(f):
#     def inner():
#         start_time = time.time()
#         f()
#         end_time = time.time()
#         print(f'测试本函数的执行效率{end_time-start_time}')
#     return inner
# @timmer # index = timmer(index)等于这个，与5对应
#
# def index():
#     '''有很多代码'''
#     time.sleep(2)
#     print('欢迎登陆博客园')
#
# def dariy():
#     '''有很多代码'''
#     time.sleep(3)
#     print('欢迎登陆日记')
# 1
# # timmer(index)
# 2
# # ret = timmer(index)
# # ret()
# 3
# # index = timmer(index)
# # index()
# 4
# # dariy = timmer(dariy)
# # dariy()
# 5
# index()# 最终优化

# 增加功能
# def timmer(f):
#     def inner():
#         start_time = time.time()
#         r = f()
#         end_time = time.time()
#         print(f'测试本函数的执行效率{end_time-start_time}')
#         return r
#     return inner
# @timmer # index = timmer(index)等于这个，与5对应

# def index():
#     '''有很多代码'''
#     time.sleep(2)
#     print('欢迎登陆博客园')
#     return 666
#
# def dariy():
#     '''有很多代码'''
#     time.sleep(3)
#     print('欢迎登陆日记')
# ret = index()
# print(ret)
# index()

# 增加:参数
# def timmer(f):
#     def inner(n):
#         start_time = time.time()
#         r = f(n)
#         end_time = time.time()
#         print(f'测试本函数的执行效率{end_time-start_time}')
#         return r
#     return inner
# @timmer # index = timmer(index)等于这个，与5对应
#
# def index(name):
#     '''有很多代码'''
#     time.sleep(1)
#     print(f'欢迎{name}登陆博客园')
#     return 666

# def dariy():
#     '''有很多代码'''
#     time.sleep(3)
#     print('欢迎登陆日记')
# index('sb')

# 使用多个参数
# def timmer(f):
#     def inner(*args,**kra):
#         start_time = time.time()
#         r = f(*args,**kra)
#         end_time = time.time()
#         print(f'测试本函数的执行效率{end_time-start_time}')
#         return r
#     return inner
# @timmer # index = timmer(index)等于这个，与5对应
#
# def index(name):
#     '''有很多代码'''
#     time.sleep(1)
#     print(f'欢迎{name}登陆博客园')
#     return 666
#
# def dariy(name,age):
#     '''有很多代码'''
#     time.sleep(1)
#     print(f'欢迎{name}登陆日记,{age}岁')
# dariy('sb',18)
# index('sb')

# 万能参数
# 最终版本

# timmer装饰器
# def timmer(f):
#     # f = index
#     def inner(*args,**kwargs):
#         #  函数的定义：* 聚合  args = ('李舒淇',18)
#         start_time = time.time()
#         # print(f'这是个f():{f()}!!!') # index()
#         r = f(*args,**kwargs)
#         # 函数的执行：* 打散：f(*args) --> f(*('李舒淇',18))  --> f('李舒淇',18)
#         end_time = time.time()
#         print(f'测试本函数的执行效率{end_time-start_time}')
#         return r
#     return inner
#
# @timmer # index = timmer(index)
# def index(name):
#     '''有很多代码.....'''
#     time.sleep(0.6) # 模拟的网络延迟或者代码效率
#     print(f'欢迎{name}登录博客园首页')
#     return 666
# index('纳钦')  # inner('纳钦')

# @timmer
# def dariy(name,age):
#     '''有很多代码.....'''
#     time.sleep(0.5) # 模拟的网络延迟或者代码效率
#     print(f'欢迎{age}岁{name}登录日记页面')
# dariy('李舒淇',18)  # inner('李舒淇',18)


# 标准版的装饰器；

def wrapper(f):
    def inner(*args,**kwargs):
        '''添加额外的功能：执行被装饰函数之前的操作'''
        ret = f(*args,**kwargs)
        ''''添加额外的功能：执行被装饰函数之后的操作'''
        return ret
    return inner
# 后面为自己添加
@wrapper

def index(name,age):
    '''有很多代码'''
    time.sleep(1)
    print(f'欢迎{name,age}登陆博客园')
    return 666
index('zxl',18)
# 装饰器类似一个模板。


