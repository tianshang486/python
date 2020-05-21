# 1. 请将列表中的每个元素通过 "_" 链接起来。
# 第一种
# users = ['李少奇','李启航','渣渣辉']
# # 请将列表中的每个元素通过 "_" 链接起来。
# users1 = '_'.join(users)
# print(users1)

# 第二种
# users = ['李少奇','李启航','渣渣辉']
# a = ''
# for i in users:
#     a = a + str(i) + '_'
# print(a[:-1])
# # 请将元组 v1 = (11,22,33) 中的所有元素追加到列表 v2 = [44,55,66] 中。
# v1 = (11,22,33)
# v2 = [44,55,66]
# for i in v1:
#     v2.append(i)
# print(v2)

# 请将元组 v1 = (11,22,33,44,55,66,77,88,99) 中的所有偶数索引位置的元素 追加到列表 v2 = [44,55,66] 中。
# v1 = (11,22,33,44,55,66,77,88,99)
# v2 = [44,55,66]
# for i in v1:
#     if i%2 == 0:
#         v2.append(i)
#     else:
#         pass
# print(v2)
# 将字典的键和值分别追加到 key_list 和 value_list 两个列表中，如：
key_list = []
value_list = []
info = {'k1':'v1','k2':'v2','k3':'v3'}
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
for key in info.keys():key_list.append(key)
for key in dic.keys():key_list.append(key)
print(key_list)
for value in info.values():value_list.append(value)
for value in dic.values():value_list.append(value)
print(value_list)
# # a. 请循环输出所有的key
# for key in key_list:
#     print(key)
# # b. 请循环输出所有的value
# for value in value_list:
#     print(value)
# c. 请循环输出所有的key和value
# for key,value in info.items():
#     print(key,value)
# for key,value in dic.items():
#     print(key,value)
# d. 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典

# e. 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
# f. 请在k3对应的值中追加一个元素 44，输出修改后的字典
# g. 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
# av_catalog = {
#     "欧美":{
#         "www.太白.com": ["很多免费的,世界最大的","质量一般"],
#         "www.alex.com": ["很多免费的,也很大","质量挺好"],
#         "oldboy.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
#         "hao222.com":["质量很高,真的很高","全部收费,屌丝请绕过"]
#     },
#     "日韩":{
#         "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]
#     },
#     "大陆":{
#         "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
#     }
# }
# 给此 ["很多免费的,世界最大的","质量一般"]列表第二个位置插入一个 元素：'量很大'。
# av_catalog['欧美']['www.太白.com'].insert(1,'量很大')
# print(av_catalog)
# 将此 ["质量很高,真的很高","全部收费,屌丝请绕过"]列表的 "全部收费,屌丝请绕过" 删除。
# av_catalog["欧美"].pop('hao222.com','my')
# print(av_catalog)
# 将此["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]列表的 "verygood"全部变成大写。
# av_catalog["日韩"]["tokyo-hot"][1] = av_catalog["日韩"]["tokyo-hot"][1].upper()
# print(av_catalog)
# 给 '大陆' 对应的字典添加一个键值对 '1048' :['一天就封了']
# av_catalog["大陆"]['1048'] = '一天就封了'
# print(av_catalog)
# 删除这个键值对："oldboy.com": ["多是自拍,高质量图片很多","资源不多,更新慢"]
# av_catalog["欧美"].pop("oldboy.com")
# print(av_catalog)
# 给此["全部免费,真好,好人一生平安","服务器在国外,慢"]列表的第一个元素，加上一句话：'可以爬下来'
# av_catalog['大陆']["1024"].append('可以爬下来')
# print(av_catalog)
#
#
# info = {
#    'k1':'v1',
#      'k2':[('alex'),('wupeiqi'),('oldboy')],
#  }
# 请循环打印k2对应的值中的每个元素。
# for i in info['k2']:print(i)
# 有字符串"k: 1|k1:2|k2:3 |k3 :4" 处理成字典 {'k':1,'k1':2....}
# msg = "k: 1|k1:2|k2:3 |k3 :4"
# dic = {}
# i1 = msg.strip().split('|')
# print(i1)
# for i in i1:
#     key,value = i.split(':')
#     dic[key.strip()] = int(value)
# print(dic)
#


# 写代码
#
# """
# 有如下值 li= [11,22,33,44,55,66,77,88,99,90] ,将所有大于 66 的值保存至字典的第一个key对应的列表中，将小于 66 的值保存至第二个key对应的列表中。
#
# result = {'k1':[],'k2':[]}
# li= [11,22,33,44,55,66,77,88,99,90]
# for i in li:
#     if i > 66:
#         result['k1'].append(i)
#     else:
#         result['k2'].append(i)
# print(result)
# 输出商品列表，用户输入序号，显示用户选中的商品
#
# """
# 商品列表：
goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998}
]
# for i in goods:print(i)
# 要求:
# 1：页面显示 序号 + 商品名称 + 商品价格，如：
#       1 电脑 1999
#       2 鼠标 10
# 	  ...
x = 0
more = ''
for i in goods:
    for key,value in i.items():
        print(x,key,value)
        x += 1
# 2：用户输入选择的商品序号，然后打印商品名称及商品价格
# you = input('请输入序号')
# print(goods[int(you)])
# 3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
# while 1:
#     you = int(input('请输入序号'))
#     if you > len(goods):
#         print('输入有误，并重新输入')
#     else:
#         print(goods[int(you)])
# 4：用户输入Q或者q，退出程序。
# 单次
# you = input('请输入序号')
# while you.upper() == 'Q':
#     break
# else:
#     if int(you)  > len(goods):
#         print('输入有误，并重新输入')
#     else:
#         print(goods[int(you)])

# 无限循环
# while 1 :
#     you = input('请输入序号')
#     if you.upper() == 'Q':
#         break
#     else:
#         if int(you) > len(goods):
#             print('输入有误，并重新输入')
#         else:
#             print(goods[int(you)])


# 看代码写结果
#
# v = {}
# for index in range(10):
#     print(index)
#     v['users'] = index
# print(v)