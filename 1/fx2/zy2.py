# 判断下列逻辑语句的True,False.
# print(1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
# 1>1 or 3<4# 为True
# True or 4 > 5 and 2 > 1 and 1 > 8 # 取左 True
# True or 7 < 6 # 取左
# 2）not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
# print(not 2 > 1 and 3 )# False
# 求出下列逻辑语句的值。
# 1),8 or 3 and 4 or 2 and 0 or 9 and 7
# print(8 or 3 and 4 or 2 and 0 or 9 and 7)
# print(8)
# 优先级： not(不) > and(和) > or(或);0为假数也就是False *****
# or 输入左 and 输入右

# 2),0 or 2 and 3 and 4 or 6 and 0 or 3
# 下列结果是什么？
# 1)、6 or 2 > 1
# print(6 or 2 > 1) # 2>1为Ture，成立，所以式子不   为False，or取左
# 6
# 2)、3 or 2 > 1
# print(3 or 2 > 1)
# 3)、0 or 5 < 4
# print(0 or 5 < 4)# or  取左0 因为左边为False 所以取Fasle
# 当 0 or False 时候 ，默认判断0为False
# 4)、5 < 4 or 3
# print(5 < 4 or 3)# False or 3 ，因为False为错误，所以或者3，因此取3
# 5)、2 > 1 or 6
# print(2 > 1 or 6)# 取左为True
# 6)、3 and 2 > 1
# print(3 and 2 > 1) # and 取右
# 7)、0 and 3 > 1 # 0为False为假，and假时，取假值
# print(0 and 3)
# 8)、2 > 1 and 3
# print(2 > 1 and 3)
# 9)、3 > 1 and 0
# print(3 > 1 and 0)
# 10)、3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2
# print(3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2)
# print(2 or 2 < 3 and 3 and 4 or 3 > 2)
# print(2 or 3>2)
# while循环语句基本结构？
# while True:
# 利用while语句写出猜大小的游戏：
# 设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果正确，然后退出循环。
# while True:
#     a = input('请输入数字：')
#     if a > 16:print('猜大了')
#     elif a < 16 :print('猜小了')
#     else:print('猜对了')
# 在5题的基础上进行升级：
# 给用户三次猜测机会，如果三次之内猜测对了，则显示猜测正确，退出循环，如果三次之内没有猜测正确，则自动退出循环，并显示‘太笨了你....’。
# chare = 1
# while chare < 4:
#     a = int(input('请输入数字：'))
#     chare += 1
#     if a > 66:print('猜大了')
#     elif a < 66 :print('猜小了')
#     else:print('猜对了')
#     break
# else:
#     print('次数超过')
# 使用while循环输出 1 2 3 4 5 6 8 9 10
# chare = 1
# while chare < 11:
#     print(chare)
#     chare += 1
# 求1-100的所有数的和
# chare = 1
# sum = 0
# while chare < 101:
#     sum += chare
#     chare += 1
# else:
#     print(sum)

# # 输出 1-100 内的所有奇数
# chare  = 1
# sum = 0
# while chare < 101:
#     if chare % 2 == 0:chare += 1
#     else:
#         sum += chare
#         chare += 1
# print(sum)
#
# # 输出 1-100 内的所有偶数
# chare  = 1
# sum = 0
# while chare < 101:
#     if chare % 2 == 0:
#         sum += chare
#         chare += 1
#     else:chare += 1
#
# print(sum)
# # 求1-2+3-4+5 ... 99的所有数的和
# chare = 1
# sum = 0
# while chare < 100:
#     if chare % 2 == 0:
#         sum -=  chare
#         chare += 1
#     else:
#         sum += chare
#         chare += 1
# print(sum)

# 用户登录（三次输错机会）且每次输错误时显示剩余错误次数（提示：使用字符串格式化）
chare = 1
while chare < 4:
    user = input('请输入用户名：')
    passwd = input('请输入密码：')
    if user == 'zxl' and passwd == '123456':print('登陆成功')
    else:print(f'用户名或者密码错误，还剩余{3-chare}次机会')
    chare += 1
else:print('机会用完，登录失败')
# 简述ASCII、Unicode、utf-8编码
# 简述位和字节的关系？