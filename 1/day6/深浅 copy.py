# 赋值运算
l1 = [1,2,3,[22,33]]
l2 = l1 # 增删改其中一个都将同时改变,因为共有一个内存
l1.append(666)
print(l1)
print(l2)
# 这种情况下并没有改变原先内存，所以改变
a = 1
b = a
a = 2
print(a,b)
print(id(a),id(b))
# 浅copy
l1 = [1,2,3,[22,33]]
l2 = l1.copy() # 将两人内存值不在相同，也就是后续整改不影响双方
l1.append(66)
print(l1)
print(l2)
# 浅copy无法对列表里的小列表产生作用
l1[3].append(666)
print(l1)
print(l2)

# 深copy,对列表内的小列表同样有效
import copy
l3 = [1,2,3,[22,33]]
l4 = copy.deepcopy(l3)
l3[3].append(66)
print(l3,id(l3))
print(l4,id(l4))
