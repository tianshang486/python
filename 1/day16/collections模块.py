from collections import namedtuple as na
Re = na('Rectangle',['length','width'])
r = Re(10,5)
print(r.length)
print(r.width)
print(r[1])

# defautldict:
from collections import defaultdict as de
d = de(int,name='zxl',age=18)
print(d['name'])
print(d)

# Counter:计算器
from collections import Counter
c = Counter('aascmsfcaccafpm')
print(c)
print(c.most_common(3))# 前三名