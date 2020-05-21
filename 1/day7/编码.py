# python3x str为例，模拟将一句话通过网络发送给对方
# bytes
b = b'hello'
print(b,type(b))
print(b.upper())

# 英文与中文不同
# s1 = '中国'
# b = b'\xe4\xb8\xad\xe5\x9b\xbd'
# print(b)

# str ---> bytes
# s1 = '中国'
# b1 = s1.encode('utf-8')# 编码
# b2 = s1.encode('gbk')
# print(b1,type(b1))
# print(b2)
# s2 = b1.decode('utf-8')# 解码
# print(s2)

# gbk ---> utf-8
i1 = '中国' # 无法直接传输中文
i2 = i1.encode('gbk')# 编码成gbk传输
print(i2)
b1 = b'\xd6\xd0\xb9\xfa' # 传输网络bytes
print(b1)
s = b1.decode('gbk')# 解码gbk
print(s)
b2 = s.encode('utf-8')# 编码utf-8
print(b2)

# 所有编码本 (除开Unicode) 不能直接互相识别
# Unicode是英文的编码本，其他语言可以通过转换Unicode识别
# 英文和数字的字符串可以在‘’前加b转换wei1Unicode
# 中文通过encode编码，decode解码