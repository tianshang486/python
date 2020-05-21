# 与json相似，不过是完全序列化，而且是转换为字节串
import pickle
bys = pickle.dumps([1,2,3])
print(bys,type(bys))
bys1 = pickle.dumps((1,2,3))
print(bys1,type(bys1))
# 反序列回来会保留属性
res = pickle.loads(bys)
print(res,type(res))
res1 = pickle.loads(bys)
print(res1,type(res1))
# 集合也可以转换
bys3 = pickle.dumps(set('abc'))
print(bys3)

# 把pickle序列化运用到文本中
with open('c.txt',mode='wb') as f:
    pickle.dump([1,2,3],f)
# 从文件中反序列化pickle数据
with open('c.txt',mode='rb') as f1:
    res = pickle.load(f1)
    print(res,type(res))

# 多次实验
with open('d.txt',mode='ab') as f2:
    pickle.dump([1,2,3,4],f2)
    pickle.dump([1,2,3,4],f2)
    pickle.dump([1,2,3,4],f2)
with open('d.txt',mode='rb') as f3:
    for i in range(0,3):
        res  = pickle.load(f3)
        print(res,type(res))
# 多次很少使用，一般使用单次

# pcckle 功能完全领先但是不能跨语言，json能跨语言