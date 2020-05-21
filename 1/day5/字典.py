# # 4950669 交流群
# # 列表查找数据速度较慢，适合较少量数据
# # 字典 （dict） 查找速度快，适合大量数据
# # dic = {'name':['太白','翟小龙'],
# # 'age':[1,2,3,4]
# # }
#
# dict
#
# # 字典的创建
# # 第一种
# dic = dict((('one',1),('two',2),('three',3)))
# print(dic)
# # 第二种
# dic = dict(one=1,two=2,three=3)
# dic1 = dict(one=[1,2,3],two=2,three=3)
# print(dic)
# print(dic1)
# # 第三种 常用
# dic = dict({'one':1,'two':2,'three':3})
# print(dic)
#
# # 验证字典合法性：
# # dic = {[1,2,3]:'alex',1:666}
# # print(dic)
#
# # 字典的增删查改
# dic = {'name':'太白','age':18}
# # 键值对：键为房间号码，值为房间里面放的东西
# # dic = {1:(2,3),1:(3,4)}
# # print(dic)
# # 键要唯一，如果出现两次，则会顶掉
#
# # 增：
# # 直接增加
# dic['sex'] = '男' # 同时为改，当已经有那个键时为改
# print(dic)
# # setdefault 有这个键这不动，没有则增加
# dic.setdefault('hobby','直男')
# print(dic)
# dic.setdefault('age',48)
# print(dic)
#
# # 删
# # pop 按照键删除
# dic.pop('age')
# print(dic)
# # 第二键值，防止没有此键而删除报错
# ret = dic.pop('hhh','没有此键')
# print(dic)
# print(ret)
#
# # clear 清空
# dic.clear()
# print(dic)
#
# # 改
# dic = {'name':'太白','age':18}
# dic['name'] = 'alex'
# print(dic)
#
# # 查
dic = {'name':'太白','age':18,'hobby':['直男','钢管','坚硬']}
# print(dic['age'])
# # 如果没有回报错，不建议使用
# # get 查找使用get
# l1 = dic.get('yayay','没有此键')
# print(l1)
#
# # 三种特殊的
# # keys 输出所有键
# print(dic.keys())
# # 可以转换为列表
# print(list(dic.keys()))
#
# for key in dic.keys():
#     print(key)
#
# # values()输出所有值
# print(dic.values())
# print(list(dic.values()))
#
# items() 以列表输出字典
for i in dic.items():
    print(i)
# 轮流输出
for key,value in dic.items():
    print(key,value)
#
# # 面试题
# a = 18
# b = 12
# a,b = b,a
# # a,b = 12,18
# print(a,b)
#
# # 字典嵌套
# dic = {
#     'name': '汪峰',
#     'age': 48,
#     'wife': [{'name': '国际章', 'age': 38},],
#     'children': {'girl_first': '小苹果','girl_second': '小怡','girl_three': '顶顶'}
# }
#
# # 1.获 取汪峰的名字。
# print(dic.get('name','my'))
# # 2.获取这个字典：{'name':'国际章','age':38}。
# print(dic.get('wife','my'))
# print(dic['wife'][0])
# # 3. 获取汪峰妻子的名字。
# dic2 = dic['wife'][0]
# print(dic2['name'])
# print(dic['wife'][0]['name'])
# # 4. 获取汪峰的第三个孩子名字。
# print(dic['children']['girl_first'])
# print(dic['children']['girl_second'])
# print(dic['children']['girl_three'])
#
# # 练习题
# dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# # 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
# l1 = dic.get('k3')
# l1.append(44)
# print(l1)
# print(dic)
# # 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
# dic['k1'] = 'alex'
# print(dic.get('k1','my'))
# print(dic)
# # 请在k3对应的值中追加一个元素 44，输出修改后的字典
#
# print(dic['k3'])
# l1 = dic.get('k3')
# print(l1)
# dic.get('k3').append(44)
# print(dic)
# # 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# dic1 = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# dic1['k3'].insert(0,18)
# print(dic1)
# # 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
# dic2 = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# dic2['k4'] = 'v4'
# print(dic2)
# # 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
# dic2['k1'] = 'alex'
# print(dic2)
# # 请在k3对应的值中追加一个元素 44，输出修改后的字典
# dic3 = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# print(dic3['k3'])
# dic3.get('k3').append(44)
# print(dic3)
# dic4 = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# dic4['k3'].append(44)
# print(dic4)
# # 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
# dic5 = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# dic5['k3'].insert(0,18)
# print(dic5)