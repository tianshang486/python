# python自带68个内置函数
# eval 剥去字符串的外衣，运行里面的代码
# s1 = '1+3'
# print(s1)
# print(eval(s1))
# s = "{'name':'zxl'}"
# print(s,type(s))
# print(eval(s),type(eval(s)))
# eval十分危险，项目时候不能使用。
# 网络传输str input 输入时候，sql注入等绝对不能使用

# exec与eval几乎一样，但他是处理代码流,同样也危险
#

# 哈希值
# i = '12334456'
# print(hash(i))

# help 帮助
# print(help(str))
# print(help(str.upper)) # 查找某一个
# callable 判断对象是否可调用
s1 = 'aofjhapivn'
# s1()
def func():
    pass
# func()
print(callable(s1))
print(callable(func))