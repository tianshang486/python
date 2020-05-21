# f1 = open('f:\少男.txt',encoding='utf-8',mode='r')
# content = f1.read()
# print(content)
# f1.close()
'''
open 内置函数，open底层用的是操作系统的接口，也就是调用操作系统的功能。
f1,变量，一般使用f1，fh，file_handler,f_h,文件句柄。
    对文件的任何操作都要通过文件句柄，也就是变量
encoding:可以不写，不写参数，默认编码本：操作系统的默认编码
windows：gbk
linux：utf-8
mac：utf-8
mode = 'r' 读的方式输出
content = f1.read() 全部读出
f1.close() 关闭句柄。
'''

# read 全部读出
# f = open('文件的读',encoding='utf-8',mode="r")#mode 默认为读
# content = f.read()
# print(content)
# f.close()

# read(n) 安照字符读，n=多少，就从第一个开始读5个
# f = open('文件的读',encoding='utf-8',mode="r")#mode 默认为读
# content = f.read(5)
# print(content)
# f.close()

#readline() 读取第一行
# f = open('文件的读',encoding='utf-8',mode="r")#mode 默认为读
# content = f.readline()
# print(content)
# f.close()

# readlines() 每行返回一个列表并且每一行后加\n
# f = open('文件的读',encoding='utf-8',mode="r")#mode 默认为读
# content = f.readlines()
# print(content)
# f.close()

# for 循环读取
# f = open('文件的读',encoding='utf-8',mode="r")#mode 默认为读
# for line in f:
#     print(line)
# f.close()

# 前四种都是直接将文件内容全部读出，在文件内容不大是可以使用
# 当内容过多时使用for更加适用，因为是每行以此读取，读出后面前面就消失。

# rb 是读取非文本文件mode
# f = open('江南烧酒.jpg',mode='rb')
# content = f.read()
# print(content)
# f.close()

# 文件的写，创建一个新文件并写入内容
# f = open('文件的写',encoding='utf-8',mode='w')
# f.write('随便写一点')
# f.close()

# 如果文件存在，则先清空文件内容，在写入新内容
# f = open('文件的写',encoding='utf-8',mode='w')
# f.write('我又回来了')
# f.close()

# wb 写入新的非文本文件mode
# f = open('江南烧酒.jpg',mode='rb')
# content = f.read()
# print(content)
# f.close()
# f1 = open('江南烧酒2.jpg',mode='wb')
# f1.write(content)
# f1.close()

# 文件的追加 a
# 如果不存在则创建文件并写入
# f = open('文件的追加',encoding='utf-8',mode='a')
# f.write('哈哈哈哈')
# f.close()
# 有文件时，在原文件最后面追加内容
# f = open('文件的追加',encoding='utf-8',mode='a')
# f.write('呀呀哎呀呀')
# f.close()

