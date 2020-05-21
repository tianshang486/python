# os：和操作系统相关的操作被封装到这个模块中
import os
# 和文件操作相关，重命名，删除
# os.remove('a.txt') # 删除
# os.rename('b.txt','a.txt')
# 改名不会影响里面内容

# 删除目录，必须是空目录
# os.removedirs('aa')

# 如果非空还想删除
# 使用shutil模块，可以删除带内容的目录
# import shutil
# shutil.rmtree('aa')

# 和路径相关的操作，被封装到另一个模块中：
# 取出路径
res = os.path.dirname(r'd:/aaa/bbb/ccc/a.txt')
print(res)
# 取出文件名
res1 = os.path.basename(r'd:/aaa/bbb/ccc/a.txt')
print(res1)
# 取出全部,放于元组中路径与文件名，号隔开，
res2 = os.path.split(r'd:/aaa/bbb/ccc/a.txt')
print(res2)
# 拼接路径
path = os.path.join('d:\\',"aaa","bbb","ccc",'a.txt')
print(path)

# 如果是/开头路径，默认是在当前盘符下
res = os.path.abspath(r'/a/b/c')
print(res)
# 如果不是/开头，默认路径
res = os.path.abspath(r'a/b/c')
print(res)

# 判断
# 是不是绝对路径
print(os.path.isabs('a.txt'))
# 存不存在这个目录
print(os.path.isdir('d:/aaa'),bool(1))
# 存不存这个文件或目录
print(os.path.exists('d:/aaa'))
# 存不存在这个文件
print(os.path.isfile('d:/aaa'))