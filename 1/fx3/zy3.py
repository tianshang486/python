# 有变量name = "aleX leNb" 完成如下操作：
# 移除 name 变量对应的值两边的空格,并输出处理结果
name = "aleX leNb"
a = name.strip().split(' ')
print(a)
b = ''.join(a).strip()
print(b)
# 判断 name 变量是否以 "al" 开头,并输出结果
print(name.startswith('al'))
# 判断name变量是否以"Nb"结尾,并输出结果
print(name.endswith('Nb'))
# 将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结果
name1 = name.replace('l','p')
print(name1)
# 将name变量对应的值中的第一个"l"替换成"p",并输出结果
name2 = name.replace('l','p',1)
print(name2)
# 将 name 变量对应的值根据 所有的"l" 分割,并输出结果。
print(name.split('l'))
# 将name变量对应的值根据第一个"l"分割,并输出结果。
print(name.split('l',1))
# 将 name 变量对应的值变大写,并输出结果
print(name.upper())
# 将 name 变量对应的值变小写,并输出结果
print(name.lower())
# 判断name变量对应的值字母"l"出现几次，并输出结果
print(name.count('l'))
# 如果判断name变量对应的值前四位"l"出现几次,并输出结果
print(name.count('l',4))
# 请输出 name 变量对应的值的第 2 个字符?
print(name[2])
# 请输出 name 变量对应的值的前 3 个字符?
print(name[:3])
# 请输出 name 变量对应的值的后 2 个字符?
name = "aleX leNb"
print(name[-1:-3:-1])
# 2.有字符串s = "123a4b5c"
# 通过对s切片形成新的字符串s1,s1 = "123"
s = "123a4b5c"
print(s[:3])
# 通过对s切片形成新的字符串s2,s2 = "a4b"
print(s[3:6])
# 通过对s切片形成新的字符串s3,s3 = "1345"
print(s[::2])
# 通过对s切片形成字符串s4,s4 = "2ab"
print(s[1:-2:2])
# 通过对s切片形成字符串s5,s5 = "c"
s5 = s[-1]
print(s5)
# 通过对s切片形成字符串s6,s6 = "ba2"
s6 = s[-3:0:-2]
print(s6)
# 使用while和for循环分别打印字符串s="asdfer"中每个元素。
s="asdfer"
while True:
    for i in s:
        print(i)
    break
# 使用for循环对s="asdfer"进行循环，但是每次打印的内容都是"asdfer"。
for i in range(0,10):
    print(s)
# 使用for循环对s="abcdefg"进行循环，每次打印的内容是每个字符加上sb， 例如：asb, bsb，csb,...gsb。
for i in s:
    i = i+'sb'
    print(i)
# 使用for循环对s="321"进行循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"。
s="321"
for i in s:
    print(f'倒计时{i}秒')
# 实现一个整数加法计算器(两个数相加)：
# while True:
#     d = input('输入a或A为开始计算，q或Q为退出').upper()
#     if  d == 'Q':
#         print('退出成功')
#         break
#     elif d == 'A':
#         a = int(input('输入第一个：'))
#         b = int(input('输入第二个：'))
#         c = a + b
#         print(c)
#     else:print('指令错误')
# 如：content = input("请输入内容:") 用户输入：5+9或5+ 9或5 + 9，然后进行分割再进行计算。
# content = input("请输入内容:").strip().split('+')
# content2 = int(content[0]) + int(content[1])
# print(content2)
# 选做题：实现一个整数加法计算器（多个数相加）：
# 如：content = input("请输入内容:") 用户输入：5+9+6 +12+ 13，然后进行分割再进行计算。
# content2 = 0
# content1 = input("请输入内容:").strip().split('+')
# print(content1)
# for i in range(0,len(content1)):
#     content2 += int(content1[i].strip())
# print(content2)
# 计算用户输入的内容中有几个整数（以个位数为单位）。
# ​ 如：content = input("请输入内容：") # 如fhdal234slfh98769fjdla
# chare = 0
# content = input("请输入内容：")
# for i in content:
#     if i.isdecimal():
#         chare += 1
# print(chare)

# 选做题：写代码，完成下列需求：
# 用户可持续输入（用while循环），用户使用的情况：
# 输入A，则显示走大路回家，然后在让用户进一步选择：
# 是选择公交车，还是步行？
# 选择公交车，显示10分钟到家，并退出整个程序。
# 选择步行，显示20分钟到家，并退出整个程序。
# 输入B，则显示走小路回家，并退出整个程序。
# 输入C，则显示绕道回家，然后在让用户进一步选择：
# 是选择游戏厅玩会，还是网吧？
# 选择游戏厅，则显示 ‘一个半小时到家，爸爸在家，拿棍等你。’并让其重新输入A，B,C选项。
# 选择网吧，则显示‘两个小时到家，妈妈已做好了战斗准备。’并让其重新输入A，B,C选项。
# while True:
#     a = input('输入A or B or C:').upper()
#     if a == 'A':
#         print('走大路回家')
#         break
#     elif a == 'B':
#         print('走小路回家')
#         break
#     elif a == 'C':
#         print('绕道回家')
#         d = input('选择游戏厅或网吧：')
#         if d == '游戏厅':print('一个半小时到家，爸爸在家，拿棍等你。')
#         else:print('两个小时到家，妈妈已做好了战斗准备。')



# 写代码：计算 1 - 2 + 3 ... + 99 中除了88以外所有数的总和？
i = 1
k = 0
while i<100:
    if i == 88:
        pass
    elif i%2 == 0:
        k -= i
    else:
        k += i
    i += 1
print(k)
# **选做题：**判断⼀句话是否是回⽂. 回⽂: 正着念和反着念是⼀样的. 例如, 上海 ⾃来⽔来⾃海上

# while True:
#     a = input('输入：')
#     a1 = a[::-1]
#     if a == a1:print('回文')
#     else:print('不是回文')
# 制作趣味模板程序需求：等待⽤户输⼊名字、地点、爱好，根据⽤户的名字和爱好进行任意现实 如：敬爱可亲的xxx，最喜欢在xxx地⽅⼲xxx
a = input('输入名字：')
b = input('输入地点：')
c = input('输入爱好：')
print(f'敬爱可亲的{a}，最喜欢在{b}{c}')