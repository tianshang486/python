# JavaScript Object Notation:java脚本兑现标记语言
# 已经成为了一种简单的数据交换格式
# 序列化和反序列化:
    # 将内存中的数据,转换为字节串,用以保存在文件或通过网络传输,称为序列化过程,反序列化也就是相反在转换回去.
    # 序列化:serialization,反序列化:deserialization

# # json 将数据转换为字符串,用于储存或网络传输
import json
# a = json.dumps([1,2,3,])
# print(a,type(a))
# # 元组序列化后，变成列表，但也是字符串
# b = json.dumps((4,5,6))
# print(b,type(b))
# # 字典效果与列表一样
# c = json.dumps({'name':'zxl','age':18})
# print(c,type(c))
# # 除开集合，其他任何格式都可以
#
# # at以文本的方式进行追加
#
# # 序列化
# # 将json结果写到文件中
# with open('b.txt',mode='at',encoding='utf-8') as f1:
#     s = json.dump([1,2,3,4],f1)
#     print(s,type(s))
# # 反序列化
# res = json.dumps([1,2,3])
# lst = json.loads(res)
# print(lst,type(lst))
# # 元组反序列化后依然是列表属性
# res1 = json.dumps((1,2,3))
# lst1 = json.loads(res1)
# print(lst,type(lst1))
#
# # 在文件中反序列化
# with open('b.txt',encoding='utf-8') as f1:
#     res = json.load(f1)
#     print(res,type(res))
'''----------------------------------------------'''

# json文件通常是一次性写一次性读
# 使用另一种方式，可以实现多次写，多次读

# 把需要序列化的对象，通过多次序列化的方式，用文件的write方法，
# 把多次序列化后的json字符串写到文件

with open('json.txt',mode='at',encoding='utf-8') as f2:
    f2.write(json.dumps([1,2,3,4,5,6]) + '\n')
    f2.write(json.dumps([1,2,3,4,5,6]) + '\n')

# 多次序列化后，反序列化回来
with open('json.txt',mode='rt',encoding='utf-8') as f3:
    # res = json.loads(f3.readline().strip())
    # print(res,type(res))
    # res1 = json.loads(f3.readline().strip())
    # print(res1,type(res1))
    for i in f3:
        print(json.loads(i.strip()))

# json 是一种不完全的序列化，序列化成字符串