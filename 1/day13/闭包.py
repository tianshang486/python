# 封闭的东西:保证数据的安全
# l1 = []
# def make(new):
#     l1.append(new)
#     total = sum(l1)
#     return total/len(l1)
# print(make(100000))
# print(make(110000))
# print(make(120000))

# 数据安全，l1不能是全局变量

# 直接在局部设置变量，不能达到要求

# 因此使用闭包
# def make(): #
# #    l1 = [] # 产生闭包后，这个变量将成为自由变量，自由变量不会在内存中消失
# #    def averager(new): # 两个#号区域为闭包区域
# #        l1.append(new)
# #        total = sum(l1)
# #       return total/len(l1)
#     return averager
# avg = make()
# print(avg(100000))
# print(avg(110000))
# print(avg(120000))
#
# def func():
#     return 666
# ret = func() # 赋值后，及时函数结束全局也有这个数值
# print(globals()) # 返回全局所有变量

# 闭包：
# 内层函数对外层函数非全局变量的引用，就会形成闭包。
# 闭包只会存在嵌套函数中
# 被引用的非全局变量也称做自由变量，这个自由变量会与内层函数绑定关系
# 自由变量不会在内存中消失
# 闭包的作用：保证数据安全

# 如何判断一个嵌套函数是不是闭包
# 1.必须是嵌套函数
# 2.不能引用全局变量
# 3.内层函数引用外层函数变量
# 4.全局变量与其对应数值与局部相等，还是闭包，内层引用的是外层局部，不是全局

# 用代码判断闭包
# def make(): #
#     l1 = [] # 产生闭包后，这个变量将成为自由变量，自由变量不会在内存中消失
#     def averager(new): # 两个#号区域为闭包区域
#         l1.append(new)
#         total = sum(l1)
#         return total/len(l1)
#     return averager
# avg = make()
# print(avg(100000))
#
# def func():
#     pass
# avg1=func()
# print(avg.__code__.co_freevars) # 代码判断是否闭包
# 有返回变量代表产出了自由变量，就是闭包