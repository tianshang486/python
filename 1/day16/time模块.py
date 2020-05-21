import time
# 获取时间戳
# 时间戳：从时间元年（1970.1.1 00:00:00）到现在经过的秒数
print(time.time())
# 获取格式化时间对象
print(time.gmtime()) # GMT(欧洲时间):
print(time.gmtime(1)) # 时间元年过了一秒后的时间
print(time.localtime()) # 当地时间

# 格式化时间对象和字符串之间的转换
s = time.strftime('%Y年%m月%d号 %H:%M:%S')
print(s)
# 把时间字符串转换为时间对象
b = time.strptime('2010 10 10',"%Y %m %d")
print(b)
# 时间对象 -> 时间戳,只是相当于只保留小数点后一位前的数
d = time.mktime(time.localtime())
print(time.time())
print(d)
# 暂停当前程序，睡眠xxx秒
time.sleep(3)

for x in range(5):
    print(time.strftime('%Y年%m月%d号 %H:%M:%S'))
    # 休眠以一秒
    time.sleep(1)