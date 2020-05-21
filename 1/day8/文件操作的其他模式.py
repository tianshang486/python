# 不能已读写形容，应该以读追加，追加是以光标位置，也就是每打一个子后面闪动的竖线
# f = open('文件的读写',encoding='utf-8',mode='r+')
# content = f.read()
# print(content)
# f.write('欧力给')
# f.close()

# 错误示例
# 先写后读，则先替换前面文字，然后读出后面内容
# f = open('文件的读写',encoding='utf-8',mode='r+')
# f.write('欧力给')
# content = f.read()
# print(content)
# f.close()

# flush 强制刷新
# pycharm 自动保存，其他软件不一定自动保存，所以需要自动刷新
# f = open('文件的其他功能',encoding='utf-8',mode='w')
# f.write('欧力给')
# f.flush()
# f.close()

# 打开文件的另一种方送
# with open('文件的读',encoding='utf-8') as f1:
#     print(f1.read())
# 优点1：不用手动关闭文件句柄也就是不要f1.close()
# 优点2：一个位置可以掉用多个
# yo优先使用这个
# with open ('文件的读',encoding='utf-8') as f1,\
#         open('文件的写',encoding='utf-8',mode='w') as f2:
#     print(f1.read())
#     f2.write('saoifgaoifgaefe')

# f.seek(0) 将光标调整到最开始
# f.seek(0,2) 将光标调整到结尾

# t以文本的方式进行使用

# with open('金刚葫芦娃', encoding='utf-8',mode='a+') as f:
#     f.write('老男孩教育')
#     f.seek(0)
#     # f.seek(0,2)
#     content = f.read()
#     print(content[0:-5])  #从头到尾最后少读5个字符