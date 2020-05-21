'''
测试自定义模块的导入
'''
import test
print(test.b)
# 自定义模块被其他模块导入时会立刻执行

# python中提供一种可以判断自定义模块是属于开发阶段还是使用阶段

# __name__:脚本方式运行时，固定的字符串：__main__
print(__name__)
# 以导入方送运行时候 --> test.py f()

# 定义一个函数，包含测试语句 --> test.py main

# __name__属性使用：
# 在脚本运行时，__name__是固定字符串__main__
# 在以模块方送被导入时候，__name__就是本模块的名字
print(test.__name__)

# 内存中：如果之前成功导入过某个模块，直接使用已经存在的模块
# 内置路径：安装目录下：lib
#sys.path：是一个路径的列表
import sys
print(sys.path)
# 添加test所在的路径到sys.path中
sys.path.append(r'F:\python\1\day15')
print(test.a)
# 使用os模块获取一个路径的父路径
import os
sys.path.append(os.path.dirname(__file__)+'/aa')
print(test.a)
# 使用相对位置找到day15文件夹
print(__file__)

# 三种都找不到就报错了
