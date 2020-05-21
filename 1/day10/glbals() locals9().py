# 内置函数：glbals() locals9()
a = 1
b = 2
def func():
    name = 'zxl'
    age = 20
    print(locals()) # 返回的是字典，字典里面的键值对是当前作用域
print(globals()) # 返回的是字典，字典里面的键值对是全局作用域
print(locals())
func()