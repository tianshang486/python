s1 = 'python全部22期'
# 对字符串进行索引，0对应第一位也就是p
# 从左至右循序，下标，索引。
s2 = s1[0]
print(s2,type(s2))
s3 = s1[8]
print(s3)
s4 = s1[-1]
print(s4)
# 按照切片取值，-1也就是从右往左第一个，与0相反,为了体贴人心都会减去一个显示，0：6 = 1：6。
s5 = s1[0:6]
print(s5)
# 0:6 也就是0到6位的字符
# :6 也就是和 0:6 一样
s6 = s1[:6]
print(s6)
# 从第六位到最后一位
s7 = s1[6:]
print(s7)
# 也就是0:5中隔一位取一个
s8 = s1[:5:2]
print(s8)
# 倒序
s9 = s1[-1:-6:-1]
print(s9)
# 如果加的不是 -1 则会从与正数同理
s10 = s1[-1:-6:-2]
print(s10)
# 按索引：s1[index]
# 按照切片：s1[start_index:end_index+1]
# 按照切片步长：s1[start_index:end_index+1:2]
# 反向按照切片步长：s1[start_index：end_index后延一位{也就是额外在加:-1}：2]
