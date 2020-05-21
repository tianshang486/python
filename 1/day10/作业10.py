#
# def func(x,y):
#     return x + y
# func(1,6)
#
#
# l = [1,2,3,4,5]
# print(len(l))

# 9.写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。
# 用户通过输入这四个内容，然后将这四个内容传入到函数中，此函数接收到这四个内容，将内容追加到一个student_msg文件中。
#
# 10.对第9题升级：支持用户持续输入，Q或者q退出，性别默认为男，如果遇到女学生，则把性别输入女。
# 用户持续输入： while input
# # 函数：接收四个参数。将四个参数追加到文件中。
# def register(n,s,a,e):
#     with open('student_msg',encoding='utf-8', mode='a') as f1:
#         f1.write('{}，{}，{}，{}'/n.format(n,s,a,e)) # 追加多个数值方法
#
# while 1:
#     name = input('请输入姓名(Q或者q退出)：')
#     if name.upper() == 'Q': break
#     sex = input('请输入性别：')
#     age = input('请输入年龄：')
#     edu = input('请输入学历：')
#     register(name,sex,age,edu) # 函数输出
#

# 写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作（选做题）。
import os#导入模块
def li(path,old,new):
    with open(path,encoding='utf-8') as f1,\
        open(path + '.bak', encoding='utf-8', mode='w') as f2:
        for line in f1:
            line1 = line.replace(old,new)
            f2.write(line1)
    os.remove(path)#删除
    os.rename(path + '.bak', path)#重命名
li('作业10','alex','sb')
li('作业10-1','垃圾','laji')