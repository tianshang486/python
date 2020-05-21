'''
世界所有软件的模式
1.以读的模式打开源文件
2.以写的模式创建一个新文件
3.将源文件的内容读出来修改成新内容，写入新文件
4.将源文件删除
5.将原文件命名成源文件
'''
# low版，处理少量数据
import os#导入模块
with open('文件的改',encoding='utf-8') as f1,\
    open('作业10-1', encoding='utf-8', mode='w') as f2:
    f3 = f1.read()
    f4 = f3.replace('alex,sb')#改
    f2.write(f4)
os.remove('文件的改')#删除
os.rename('作业10-1', '文件的改')#重命名

# 进阶版
import os#导入模块
with open('文件的改',encoding='utf-8') as f1,\
    open('作业10-1', encoding='utf-8', mode='w') as f2:
    for line in f1:
        line1 = line.replace('sb','alex')
        f2.write(line1)
os.remove('文件的改')#删除
os.rename('作业10-1', '文件的改')#重命名