# s1 = 'fjrhghae[shbfiojpsvp[dxbdjdk[jjkzsbjpjsbd/j;dks'
# python没有len
# count = 0
# for i in s1:
#     count += 1
# print(count)

# l1 = [1,2,3,4,5,6]
# count = 0
# for i in l1:
#     count += 1
# print(count)
# s1 = 'fjrhghae[shbfiojpsvp[dxbdjdk[jjkzsbjpjsbd/j;dks'
# def my_len(s):
#     count = 0
#     for i in s:
#         count += 1
#     print(count)
# my_len(s1)
# my_len(l1)

# 函数以功能（完成一件事）为导向。
# 减少重复性
# 正确代码可读性
# 减少代码量


#
# def meet():
#     print('代开微信')
#     print('上划一下')
#     return # 中断字符
#     print('下滑一下')
#     print('点开好友')
#     print('开始打字')
# meet()
# 函数什么时候运行
# 函数必须要函数名遇到（） 时才会运行

def meet():
    print('代开微信')
    print('上划一下')
    print('下滑一下')
    print('点开好友')
    print('开始打字')
    return '嘿嘿' # 将数据返回给函数的执行者，调用者meet（）
meet()
print('-------------')
ret = meet()
print(ret)

# return也就是还可以运行print时候在显示


# 传递参数
# def meet(sex):
#     print('代开微信')
#     print('识别男女：%s' %(sex))
#     print('上划一下')
#     print('下滑一下')
#     print('点开好友')
#     print('开始打字')
#     return '嘿嘿'
# meet('女')
# print('-------------')
#
# def meet(几个,大号,小号):
#     print('代开微信')
#     print('上划一下')
#     print('进行筛选%s：选择两个：%s ,%s' %(几个,大号,小号))
#     print('下滑一下')
#     print('点开好友')
#     print('开始打字')
#     return '嘿嘿' # 将数据返回给函数的执行者，调用者meet（）
# meet('2个',1426,1389)
#
# # 写一个函数，只接收两个int参数，并且大的在前
# # 三元运算符
# def com(a,b):
#     if a>b:
#         return a
#     else:
#         return b
#     pass
# print(com(400,200))
#

#
# def cod(a,b):
#     # c = a if a > b else b
#     # print(c)
#     print(a if a > b else b)
# cod(100,900)
# def cod(a,b):
#     c = a if a > b else b
#     return c
# #   return a if a > b else b
# print(cod(100,900))

# def meet(几个,大号,小号):
#     print('代开微信')
#     print('上划一下')
#     print('进行筛选%s：选择两个：%s ,%s' %(几个,大号,小号))
#     print('下滑一下')
#     print('点开好友')
#     print('开始打字')
#     return '嘿嘿' # 将数据返回给函数的执行者，调用者meet（）
# meet(几个='2个',小号=1389,大号=1426)

# 传入两个字符串参数，将两个参数拼接输出
# def pj(a,b):
#     print(a+b)
# pj(a='嘿嘿',b='哈哈') # 使用关键字等于不用担心循序

# def meet(几个,大号,小号):
#     print('代开微信')
#     print('上划一下')
#     print('进行筛选%s：选择两个：%s ,%s' %(几个,大号,小号))
#     print('下滑一下')
#     print('点开好友')
#     print('开始打字')
#     return '嘿嘿：大号%s,小号%s' %(大号,小号) # 将数据返回给函数的执行者，调用者meet（）
# print(meet(几个='2个',小号=1389,大号=1426))


# 写函数，检查传入列表的长度，如果大于2，那么保留前两内容，并输出
# 第一种
# def func(l):
#     if len(l) > 2:
#         return l[:2]
#     else:
#         return 1
# print(func([1,2,3,4,5,6]))
# print(func([1,]))
# 第二种
# def func(l):
#     print(l[0:2])
# func([1,2,3,4,5])
# func([1,])

# 可以直接赋值，也可以后续改值

# 形参角度：
# 1.位置参数
# 2.默认参数（经常使用的参数）