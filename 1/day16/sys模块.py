# 里面存在python解释器的操作
# 获取命令行方式运行的脚本后面的参数
import sys
# print(sys.argv[0]) # 脚本名
# print(sys.argv[1]) # 第一个参数
# print(sys.argv[2]) # 第二个参数
# arg1 = int(sys.argv[1])
# arg2 = int(sys.argv[2])
# print(arg1+arg2)

# 解释器寻找模块的路径
# print(sys.path)
# 寻找已经加载的模块
print(sys.modules)