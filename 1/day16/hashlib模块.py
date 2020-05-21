# hashlib：加密模块，封装一些用于加密的类

# dir(hashlib) # 用cmd命令行使用才能显示
# 加密的目的：用于判断和验证，而并非解密
# 特点：
    # 把一个大的数据，切成不同快，分别对不同的块进行加密，
    # 在汇总的结果的，和直接对整体数据加密的结果是一致的。
    # 单向加密不可逆，不是绝对(可能被破解)
    # 原始数据的一点小变化，将导致结果的非常大的差异，'雪崩'

# md5加密算法：
import hashlib
# m = hashlib.md5()
# 使用加密对象的update，进行加密
# m.update('abc中文'.encode('utf-8'))
# # 通过hexddiggest获取加密结果
# res = m.hexdigest()
# print(res)

# 给一个数据加密：
# 验证：用另一个数据加密的结果和第一次加密的结果对比
# 如果结果相同，说明原文相同

# 不同加密算法：实际上就是加密结果的长度不同
# s = hashlib.sha224()
# s.update(b'abc')
# print(len(s.hexdigest()),s.hexdigest())
# s = hashlib.sha256()
# s.update(b'abc')
# print(len(s.hexdigest()),s.hexdigest())

# 注册登录程序：

def get_md5(username,password):
    m = hashlib.md5()
    m.update(username.encode('utf-8'))
    m.update(password.encode('utf-8'))
    return m.hexdigest()

def reg(username,password):
    # 加密
    res = get_md5(username, password)
    # 写入文件
    with open('login.txt',mode='at',encoding='utf-8') as f:
        f.write(res)
        f.write('\n')

def login(username,password):
    # 获取当前登录信息的加密结果
    res = get_md5(username,password)
    # 读文件，和其中数据进行对比
    with open('login.txt',mode='rt',encoding='utf-8') as f:
        for line in f:
            if res == line.strip():
                return True
        else:
            return False
while True:
    op = int(input('1.注册 2.登录 3.退出'))
    if op == 3:
        break
    elif op == 1:
        username = input('请输入用户名：')
        password = input('请输入密码：')
        reg(username,password)
    elif op == 2:
        username = input('请输入用户名：')
        password = input('请输入密码：')
        res = login(username,password)
        if res:
            print('登录成功')
        else:
            print('登录失败')