# %s format
# name = '太白'
# age = 18
# msg = '我叫%s，今年%s' %(name,age)
# msg1 = '我叫{}，今年{}' .format(name,age)
# 新特性：格式化输出
# name = 'taibai'
# age = 18
# msg = f'我叫{name}，今年{age}'
# print(msg)
# 可以加表达式
# dic = {'name':'zxl','age':18}
# msg = f'我叫{dic["name"]},今年{dic["age"]}'
# print(msg)
#
# count = 6
# print(f'最终结果：{count**2}')
# name = 'zxl'
# print(f'名字叫：{name.upper()}')

# 结合函数写
def _sum(a,b):
    return a+b
msg = f'最终结果是：{_sum(10,20)}'
print(msg)
# 优点：
# 1.结构更加简化
# 2.可以结合表达式
# 3.效率提升很多
# 3.6版本后，上面两种被这回这个新方法替换