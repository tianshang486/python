#+ - * / 不详解
# %   /后返回余数
# ** 乘方
# //  /后返回余数的整数部分
# == 是否等于
# ！= 不等于
# +=    a = a+1 可以简写为 += 其他各种运算同理同理
# 优先级： not(不) > and(和) > or(或);0为假数也就是False
# or 输入左 and 输入右
print(1 or 2)
print(0 or 2)
print(1 and 2)
#面试题
#为4
print(1 and 2 or 3 and 4)
#任何数字可以转换为字符串，纯数字的字符串才能转换为数字。
abd = '00100'
abe = 100
print(int(abd),type(int(abd)))
print(abd,type(abd))
print(abe,type(str(abe)))
print(abe,type(str(abd)))
# 1 > 2 不成立 去除 and优先取6 or 左边2被去除只剩下右边所以结果为6
print(1 > 2 or 3 and 6)
# not为相反 True 和 False 之间转换
print(not 0 or 1 and 2)
print(int(False),type(int(False)))
print(int(True),type(int(True)))
