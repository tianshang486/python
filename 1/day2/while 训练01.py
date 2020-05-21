# 1.猜大小游戏，自己优化版
# count = 1
# while count < 4:
#     a = int(input('输入数字'))
#     if a<50:
#         d = '%s' % (count)
#         n = 3 - int(d)
#         print('猜小了,还剩%s次' % (n))
#         count += 1
#     elif a>50:
#         d = '%s' % (count)
#         n = 3 - int(d)
#         print('猜大了,还剩%s次' % (n))
#         count += 1
#     else:
#         print('恭喜你猜中了')
#         break
# else:
#     print('你不行啊')
# 设置n函数没必要，在第6题又解决办法
# 2.循环输出1-10
# conut = 1
# while conut < 11:
#     print(conut)
#     conut += 1
# 3.不输出7
# conut = 1
# while conut < 11:#第一种
#     if conut == 7:
#         conut += 1
#     else:
#         print(conut)
#     conut += 1
# conut = 1
# while conut < 11:#第二种
#     if conut == 7:
#         pass
#     else:
#         print(conut)
#     conut += 1
# conut = 1
# while conut < 11:#第三种
#     if conut == 7:
#         print('')
#     else:
#         print(conut)
#     conut += 1
# conut = 1
# while conut < 10:#第四种
#     conut += 1
#     if conut == 7:
#         continue
#     else:
#         print(conut)

# 4.输出1-100总数和。
# conut = 1
# a = 0
# while conut < 101:
#     a += conut
#     conut += 1
# else:
#     print(a)
# 5.输出1-2+3-4+5......+99总和
# conut = 1
# a = 0
# while conut < 100:
#     if a % 2 == 0:
#         a -= conut
#     else:
#         a += conut
#     conut += 1
# else:
#     print(a)
# 6.设计账户登录
conut = 1
while conut < 4:
    name = input('输入账号：')
    passwd = input('输入密码：')
    code = 'qwer'
    you_code = input('输入验证码：')
    if you_code == code:
        if name == 'zxl' and passwd == '123':
            print('登陆成功')
        else:
            print('账号或密码错误,还剩余 %s 次' % (3-conut))
            conut += 1
    else:
        print('验证码错误')
else:
    print('超过3次输入错误')
