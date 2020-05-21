# 请将列表中的每个元素通过 "_" 链接起来。
# users = ['李少奇','李启航','渣渣辉']
# users1 = '_'.join(users)
# print(users1)
# 请将列表中的每个元素通过 "_" 链接起来。
users = ['李少奇','李启航',666,'渣渣辉']
users1 = ''
for i in users:
        users1 = users1 + '-' + str(i)
print(users1[1::])
# 请将元组 v1 = (11,22,33) 中的所有元素追加到列表 v2 = [44,55,66] 中。
# 第一种
v1 = (11,22,33)
v2 = [44,55,66]
# v2 = v2 + list(v1)
# print(v2)
# 第二种
# for i in v1:v2.append(i)
# print(v2)


# 请将元组 v1 = (11,22,33,44,55,66,77,88,99) 中的所有偶数索引位置的元素 追加到列表 v2 = [44,55,66] 中。
v1 = (11,22,33,44,55,66,77,88,99)
v2 = [44,55,66]
for i in range(1,len(v1)):
        in1 = v1[i]
        if i % 2 == 0 and i :
                v2.append(in1)
print(v2)
# 将字典的键和值分别追加到 key_list 和 value_list 两个列表中，如：
key_list = []
value_list = []
info = {'k1':'v1','k2':'v2','k3':'v3'}
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
for key,value in info.items():
        key_list.append(key)
        value_list.append(value)
for key1,value1 in dic.items():
        key_list.append(key1)
        value_list.append(value1)
# print(key_list,value_list)
# a. 请循环输出所有的key
# for i in key_list:
#         print(i)
# b. 请循环输出所有的value
# for i in value_list:
#         print(i)
# c. 请循环输出所有的key和value
# for key,value in info.items():
#         print(key,value)
#         for key1,value1 in dic.items():
#                 print(key1,value1)
# # d. 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
# dic['k4'] = 'v4'
# print(dic)
# # e. 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
# dic['k1'] = 'alex'
# print(dic)
# # f. 请在k3对应的值中追加一个元素 44，
# dic['k3'].append(44)
# print(dic)
# # g. 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
# dic['k3'].insert(0,18)
# print(dic)
av_catalog = {
    "欧美":{
        "www.太白.com": ["很多免费的,世界最大的","质量一般"],
        "www.alex.com": ["很多免费的,也很大","质量挺好"],
        "oldboy.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "hao222.com":["质量很高,真的很高","全部收费,屌丝请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}
# 给此 ["很多免费的,世界最大的","质量一般"]列表第二个位置插入一个 元素：'量很大'。
# av_catalog['欧美']["www.太白.com"].insert(1,'量很大')
# print(av_catalog)
# 将此 ["质量很高,真的很高","全部收费,屌丝请绕过"]列表的 "全部收费,屌丝请绕过" 删除。
# av_catalog['欧美']['hao222.com'].remove("全部收费,屌丝请绕过")
# print(av_catalog)
# 将此["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]列表的 "verygood"全部变成大写。
# av_catalog["日韩"]["tokyo-hot"][1] = av_catalog["日韩"]["tokyo-hot"][1].upper()
# print(av_catalog)
# 给 '大陆' 对应的字典添加一个键值对 '1048' :['一天就封了']
# av_catalog["大陆"]['1048'] = ['一天就封了']
# print(av_catalog)
# 删除这个键值对："oldboy.com": ["多是自拍,高质量图片很多","资源不多,更新慢"]
# av_catalog["欧美"].pop("oldboy.com")
# print(av_catalog)
# 给此["全部免费,真好,好人一生平安","服务器在国外,慢"]列表的第一个元素，加上一句话：'可以爬下来'
# av_catalog["大陆"]["1024"][0] = av_catalog["大陆"]["1024"][0] + ',可以爬下来'
# print(av_catalog)

# 请循环打印k2对应的值中的每个元素。
#
info = {
    'k1':'v1',
    'k2':[('alex'),('wupeiqi'),('oldboy')],
}
for i,value in info.items():
    if type(value) == str:print(value)
    else:
        for i1 in info[i]:print(i1)

# 有字符串"k: 1|k1:2|k2:3 |k3 :4" 处理成字典 {'k':1,'k1':2....}
k = "k: 1|k1:2|k2:3 |k3 :4"
k1 = k.strip().split('|')
k2 = {}
for i in k1:
    key,value = i.split(':')
#    print(i.split(':'))
    k2[key] = value
print(k2)
# 列表可以赋予等量的变量值
a,b = [1,2]
print(a,b)
# 写代码
#
# """
# 有如下值 li= [11,22,33,44,55,66,77,88,99,90] ,将所有大于 66 的值保存至字典的第一个key对应的列表中，将小于 66 的值保存至第二个key对应的列表中。
li= [11,22,33,44,55,66,77,88,99,90]
result = {'k1':[],'k2':[]}
for i in li:
    if i > 66:
        result['k1'].append(i)
    elif i < 66:
        result['k2'].append(i)
print(result)
# result = {'k1':[],'k2':[]}
# """
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
# 要求:
# 1：页面显示 序号 + 商品名称 + 商品价格，如：
#       1 电脑 1999
#       2 鼠标 10
# 	  ...
cont = 0
st = ''
for i in goods:
    st = str(cont) + ' ' + i['name'] + ' ' + str(i['price'])
    print(st)
    cont += 1

# 2：用户输入选择的商品序号，然后打印商品名称及商品价格
# x = int(input('输入序号：'))
# li = []
# for i in goods:
#         li.append([i['name'],i["price"]])
# print(li[x])

# 3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
# li = []
# cont = 0
# for i in goods:
#         li.append([i['name'],i["price"]])
#         cont += 1
# while True:
#     x = int(input('输入序号：'))
#     if x < cont:
#         print(li[x])
#         break
#     else:print('输入有误，重新输入：')
# 4：用户输入Q或者q，退出程序。
li = []
cont = 0
for i in goods:
        li.append([i['name'],i["price"]])
        cont += 1
while True:
    x = input('输入序号：').upper()
    if x == 'Q':break
    elif int(x) < cont:
        print(li[int(x)])
        break
    else:print('输入有误，重新输入：')

# """
# 看代码写结果
#
v = {}
for index in range(10):
    v['users'] = index
print(v)
{'users':9}
