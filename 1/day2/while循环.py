'''                            1. 判断是否是True
while 条件:                     2. 如果是True，就进入循环体
    循环体                      3. 每次都会进行判断条件
'''
# 最基础的循环
while True:
    print('爱你一万年')
    print('野狼')
    print('浮夸')
    print('红玫瑰')
    print('红玫瑰')
# 如何终止循环？
#   1.改变条件
#   2.break
#   3.系统命令
flag = True
while flag:
    print('爱你一万年')
    print('野狼')
    print('浮夸')
    print('红玫瑰')
    flag = False # 改变条件终止循环
    print('白玫瑰')
# 第二种例子，通过‘标志位’
count = 1
fal1 = True
while fal1:
    print(count)
    count = count + 1
    if count >= 10:
        fal1 = False
# 简单的一种
count = 1
while count < 100:
    count = count + 1
    print(count)

# break停止循环，立即停止。
while True:
    print('爱你一万年')
    print('野狼')
    print('浮夸')
    break
    print('红玫瑰')
    print('红玫瑰')
print('不听了')# 循环结束才会输出
# 输出0-100所有偶数
# 方法一
o = 2
n = True
while n:
    print(o)
    o = o+2
    if o > 100:
        break
print('结束')
# 方法二
n = 2
while n <= 100:
    if n % 2 == 0:
        print(n)
    n = n + 1
# continue,出现该命令结束本次循环，但不停止循环，相当于循环底部，直接回到顶部。
a = 1
while True:
    print(111)
    print(222)
    a = a+1
    if a > 10:
        break
    continue
    print(333)
# while else:
com = 1
while com < 5:
    print(com)
    com = com + 1
else:
    print('yes')

# 登录系统实际运用
# 第一种
count = 1
name = input('输入您的姓名')
password = input('输入您的密码')
while name != 'zxl' and password != 123:
    print('账号或密码错误')
    name = input('输入您的姓名')
    password = input('输入您的密码')
    count = count + 1
    if count > 3:
        print('超过3次')
        break
else:
    print('登录成功')
# 第二种
count = 1
while count <= 3:
    username = input('输入您的账号：')
    password = input('输入您的密码')
    code = 'qwer'
    your_code = input('输入验证码')
    if your_code == code:
        if username == 'zxl' and password == '123':
            print('登录成功')
        else:
            print('账号或者密码错误')
            count = count + 1
    else:
        print('验证码输入错误')
else:
    print('输错账号或密码3次')