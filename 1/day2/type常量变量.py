#整数，浮点数，字段，布尔，(False错，Ture对)字典，列表等常量。
# 变量可以随便更改，但需要遵守规则，变量储存到根据常量开括在计算机储存的空间内。
#以下为各种规则：
#变量全部由数字，字母，下划线（——）组成。不能数字开头，不能用关键字。
#要有描述性，见名知意。
#不能用中文等其他国家语言。
#不能过长。
#变量只能指向数据，不能指向变量。
mone = 99
fudn = 0.99
user = '小明'
a = 1+2*3/4
print(mone)
print(fudn)
print(user)
#重新 = 将会取代
user = '小强'
a=2
b=3
a=a-2
b=a+3
a=b-1
print(user)
print(user,a,fudn,mone)
print(a,b)
#where指数据长而复制的数据
#age指年龄
#name指姓名
#可以这样使用name1，name2，age1，age2.
#why等这些只是讲解过程无其他意义。
#why：指生活中一直不变的，指性别，身份证号码，历史发生的时间
#what：指常量，python中没有真正常量，可以改变。
# Java，c不能，全部大写的称为常量，就按照规则不能在 = 取代。
NAME = 1
#不可以改变
name =1
name = 2
#可以改变
#how：将变量全部调为大写，放到最上面。
#where:设置一些不变常量，id，身份证 。
#注释：
#单行注释：#，多行注释："""债辛苦"""
'''
amfponafpbapbfapbf
print(a)
'''
"""
asfihsaoigfaif
print(b)
"""
#int指整形数字+-*/
#float指浮点数
#str指字符串，由''和""包括起来的。单双引号无区别但可以配合使用。如"I'm zxl, 18 year old."
#''' ''' 可以换行如
#
fore = '''fnaihfa
afpajfaj
fjapjf  a'''
print(fore)
#字符也可以使用+*，但也有一定限制，如一下案例
str1 = 'abc'
str2 = 'cba'
print(str2+str1)
print(str1*8)
str1 = 'abccba'
#bool指布尔值Ture,False.
print( 2>1)
print(1>2)
#type可以调出该常量属于那种
print(1,type(1))
print(0.11,type(0.11))
print('user',type('user'))
print(False,type(False))
print('False',type('False'))
#input用户交互
#input输出都为字符串
username = input('请输入你的用户名:')
password = input('请输入你的密码:')
print(username,type(username))
print(password,type(password))
#可以通过+链接各个变量
name = input('您的名字是：')
password = input('您的密码是：')
passwd = input ('您的验证码是：')
msg = '姓名：'+name+',密码：'+password+',验证码：'+passwd
print(msg)