# 制作自己介绍模板
# msg = '''------------info of 翟小龙--------------
# name:  翟小龙
# 性别：  男
# 种族：  汉
# --------------end----------------
# '''
# print(msg)
# 制作公共模板
name = input('请输入性名')
password = input('请输入身份证')
org = input('请输入性别')
# % 占位符 s >> str
msg = '''
---------- info of %s ----------
name    : %s
password: %s
org     : %s
------------- end --------------
''' % (name,name,password,org)
print(msg)