def login():
    pass


def register():
    pass

staus_dict={
    'username':None,
    'status':False,
}
def auth(f):
    def inner(*args,**kwargs):
        '''添加额外的功能：执行被装饰函数之前的操作'''
        if staus_dict['status']:
            ret = f(*args, **kwargs)
            '''添加额外的功能：执行被装饰函数之后的操作'''
            return ret
        else:
            username = str(input('请输入用户名：').strip())
            password = str(input('请输入密码').strip())
            if username == 'zxl' and password == '123456':
                print('登陆成功')
                staus_dict['username'] = username
                staus_dict['status'] = True
            else:
                print('登录失败')
    return inner
@auth
def article():
    print('欢迎访问文章页面')

@auth
def comment():
    print('欢迎访问评论页面')

@auth
def dariy():
    print('欢迎访问日记页面')


article()  # inner()
comment()  #inner()
dariy()