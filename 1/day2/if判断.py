#if基本格式
if 1<2 :
    print(True)
    if 1>2 :
        print(False)
elif 1==1:
    peint('完美')
    print('yes')
#与input联合,elif等于或者。嵌套if为和全部执行，满足条件全部输出。
# 从上往下执行，一个成立，下面略过，else其他，上面条件没有一个成立。
age = input('请输入你的年龄：')
if 18<=int(age)<60:
    print('您成年了')
elif 60<int(age)<99 :
    print('老头子')
elif int(age) == 100 :
    print('您和我一样')
elif int(age)>100:
    print('寿星啊')
else:
    print('小学生')
print('完成')
#嵌套if为上面满足条件，才执行下面。
username = input('您的账号是：')
password = input('您的密码是：')
code = 'qwer'
your_code = input('输入验证码：')
if your_code == code:
    if username == 'zxl' and int(password) == 123456:
        print('登陆成功')
    else:
        print('账户或者密码错误')
else:
    print('验证码错误')