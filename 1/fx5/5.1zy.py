# 如何实现字符串的反转？如： C请反转为 name ="iqiepuw"
name = "iqiepuw"
name = name[::-1]
print(name)
# 如何实现 “1,2,3” 变成 [‘1’,’2’,’3’]
int1 = '1,2,3'
int2 = int1.split(',')
print(int2)
# 如何实现[‘1’,’2’,’3’]变成[1,2,3]
list1 = []
for i in int2:
    list1.append(int(i))
print(list1)
# 以下代码输出是什么? list=['a','b','c','d','e'] print list[10:]
list=['a','b','c','d','e']
print(list[10:])

# 输出空
# 现有一列表 alist, 请写出两种去除 alist 中重复元素的方法, 其中：（难）
# – 要求保持原有列表中元素的排列顺序。
alist = [5,2,3,3,5,4,1,2,1,3]
blist = []
for i in alist:
    if i not in  blist:
        blist.append(i)
print(blist)

# – 无需考虑原有列表中元素的排列顺序（超纲）。
alist = [5,2,3,3,5,4,1,2,1,3]
print(set(alist))
# 用 Python 实现 99 乘法表（难）
# 乘法计算器
while True:
    cont1 = input('输入A或a进入计算，输入Q或q退出计算：').upper()
    if cont1 == 'A':
        int1 = int(input('输入第1个数字：'))
        int2 = int(input('输入第2个数字：'))
        cont2 = f'结果等于{int1 * int2}'
        print(cont2)
    else:break
# 99乘法表
for x in range(1,10):
    for y in range(1,x+1):
        print(f'{x}*{y}={x*y}',end=' ')
    print('')



