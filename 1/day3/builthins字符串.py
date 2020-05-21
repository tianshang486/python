s = 'zxlZXL'
s1 = '翟小龙zxlZXL'
# 字符串的常用操作方法
# 不会对源字符串进行任何操作，都是产生新的字符串
# upper(全部转换为大写) lower(全部小写)
s2 = s.upper()
s3 = s1.lower()
print(s2,type(s2))
print(s3,type(s3))

# 应用
username = input('用户名')
password = input('密码')
code = 'QweR'
your_code = input('请输入验证码,不区分大小写:')
if your_code.upper() == code.upper():
    if username == 'zxl' and password == '123':
        print('登陆成功')
    else:
        print('用户名或密码错误')
else:
    print('验证码错误')

# startswith(以什么什么开始) endswith(以什么什么结束)
# 判断是不是以（）开始结束，输出False,True
ss = 'zxlZXL'
print(ss.startswith('z'))
print(ss.startswith('zxl'))
# 判断3:6是不是以（）开始结束
print(ss.startswith('Z',3,6))

# replace,将' '内容替换,后面加数字，为从左至右替换数量
msg = 'alex 很nb，alex是老男孩教育的创始人之一，alex长得很帅'
msg1 = msg.replace('alex','zxl')
msg2 = msg.replace('alex','zxl',2)
print(msg1)
print(msg2)
# strip:空白：空格，\t(空格) \n(换行),只对字符串两边有效
a= 'zxl'
print(a)
a1 = '\t\n翟小\t龙\t\n'
print(a1)
print(a1)
a2 = a1.strip()
print(a2)
print(a2)
# 可以去除指定字符,从左往右从右往左同时进行，遇到没有的停止
a2 = 'zxlzhai翟z小xiaozxl'
a3 = a2.strip('zxlxiaozhai')
print(a3)

# split 非常重要
# 默认按照空格分隔，返回一个列表
# 指定分隔符
# str ---> list(字符串转列表)
# z = '小强 小王 小明'
# z1 =  z.split()
# print(z1)
# 了解：
z2 = ':小王:小明,小强'
print(z2)
print(z2.split(':'))
print(z2.split(':',1))
# 识别到指定字符串，才转换为列表。
# 后面加数字代表转换次数。

# join 与 split 相反，将列表转字符串
# 每个字符用指定号链接以字符串输出
h1 = 'alex'
h2 = '+'.join(h1)
print(h2,type(h2))
# 列表转字符串,列表内所有字符串按循序以指定字符串进行链接
# 前提列表里必须是字符串，不能是数字
h3 = ['小强','小王','小明']
h4 = ':'.join(h3)
print(h4)
h5 = '+'.join(h2)

# count(计算字符数字出现的次数)
d = 'asoifcgaefgbapfaofeig..,,,,,,[[[----+fip1351566'
print(d.count('a'),d.count('s'))

# format: 格式化输出
# 第一种：
msg = '我叫{}今年{}性别{}'.format('大壮',25,'男')
print(msg)
# 第二种
msg1 = '我叫{0}今年{1}性别{2}我还叫{0}'.format('大壮',25,'男')
print(msg1)
# 第三种
msg3 = '我叫{name}今年{age}性别{sex}我还叫{name}'.format(name='大壮',age=18,sex='男')
print(msg3)

# is 系列：
name = 'zxl123'
print(name.isalnum()) #判断字符串由字母或数字组成
print(name.isalpha()) #判断字符串只由字母组成
print(name.isdecimal()) #判断字符串只由十进制组成

f1 =input('请输入金额')
if f1.isdecimal():
    print(int(f1))
else:
    print('输入有误')

# 判断有没有该字符串
o1 = '老男孩edu'
print('老' in o1)
print('老男' in o1)
print('老ed' in o1)
print('老ed' not in o1) #not将含义改为是不是没有该字符串
b1 = '老男孩的讲师：太白'
'''
老       s1[0]
男       s2[1]
孩       s3[2]
的       s4[3]
讲       s5[4]
师       s6[5]
...
'''
# 0~12
index = 0
while index < 9:
    print(b1[index])
    index += 1
# for有限循环，用法与while类似
for i in b1:
    print(i)
    if i == '讲':
        break