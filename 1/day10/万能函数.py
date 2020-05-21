# 形参角度：
# def eat(a,b,c,d):
#     print('%s,%s,%s,%s' %(a,b,c,d))
# eat('zxl','zxl1','zxl2','zxl2')
# 万能参数
# def eat(*a):
#     print('%s,%s,%s,%s' %(a))
# eat('zxl','zxl1','zxl2','zxl2')

# * 号代表聚合也就是一个代表所有位置参数，也就是聚合成一个元组，并赋值给 ‘a’
# ** 号与*类似，只不过是聚合到一个字典中,利用关键字参数
# def eat(**a):
#     print('%sabc%s' %(a,a))
# eat(name='zxl',name1='zxl1')
# 混合运用
def fun(a,b,*c,sex='nan',name='zxl',**d):
    print(a,b)
    print(c)
    print(sex)
    print(d)
    print(name)
fun(1,2,3,4,5,6,4,8,sex='nv',name='zjb',age=100)

# 在调用时候用 * 可以打散
def a(*i):
    print(i)
a(*[1,23,4],*[5,6])
a(*{1,23,4},*{5,6}) # {} 可以从小到大排序
a(*(1,23,4),*(5,6))
a(*'1,23,4',*'5,6') # 对字符串使用则会拆分每一个字符
def a(**i):
    print(i)
a(**{'name':'zxl'},**{'age':18,'sex':'nan'}) # **与*效果相似但只能对字典类型有效


