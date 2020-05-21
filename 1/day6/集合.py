# 集合的创建
# set1 = {1,2,3,4,5,6,'f','ds','s','a','ad'}
# print(set1)

# 空集合：
# set2 = set()
#print(set2)

# 集合不能改，也就是不能为列表和字典
# set1 = {[1,2,3],3,{'name':'al'}}
# print(set1)

# 增 add
# set = {1,23,4}
# set.add('xx')
# print(set)
# update迭代追加
# set.update('afcaf')
# print(set)

# 删,集合无序只能按元素删除和随机删除
# set.remove(23)
# print(set)
# pop 随机删除
# set1.pop()
# print(set1)

# 改，变相改，先删除在增加

set1 = {1,2,3}
set2 = {3,4,5}
# 交集
# 代码 set1.intersection(set2)
print(set1 & set2)

# 并集
# set1.union(set2)
print(set1 | set2)

# 差集
# set1.difference(set2)
print(set1 - set2)

# 反交集
# set1.symmetric_difference(set2)
print(set1 ^ set2)

# 子集
# set1 是不是set2的子集
set1 = {1,2,3,}
set2 = {1,2,3,4,5,6}
print(set1 < set2)
# 超集 set2是不是set1的超集
print(set2 > set1)

# 列表的去重
li = [1,1,2,2,3,3,4,4]
# 将列表转换为集合，集合不能重复
set1 = set(li)
li = list(set1)
print(li)

# 用处：数据之间的关系，列表去重