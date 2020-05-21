s1 = '太白123abc'
s2 = s1[0]
s3 = s1[-1]
s4 = s1[:3]
s5 = s1[:5:2]
s6 = s1[-1:-4:-1]
s7 = s1[:8:3]
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)
print(s7)

a1 = 'zxlZXL'
a2 = 'ZXLzxl'
print(a1.upper())
print(a2.lower())

print(a1.startswith('zxl'),a2.startswith('zxl'))
print(a1.endswith('ZXL'),a2.endswith('ZXL'))

a5 = 'zxl,zxk:zxg,zxj,zxh:zxg'
print(a5)
print(a5.split())
print(a5.split(','))
print(a5.split(':'))
print(a5.split(',',1))

a1 = '\n\tzxl\n\t'
print(a1)
print(a1.strip())

a1 = 'zxl123'
print(a1.isalnum())
print(a1.isdecimal())
print(a1.isalpha())

s1 = 'anfkcn'
for i in s1:
    print(i)
    if i == 'c':
        break

s1 = '321'
for i in s1:
    print('倒计时%s秒' %(i))
print('出发')


