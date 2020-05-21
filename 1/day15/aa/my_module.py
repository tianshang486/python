'''
自定义模块
'''
# a = 1
# age = 10
#
# def f1():
#     print('hello,world')
# # 测试函数，在开发阶段，对模块的功能进行测试
# def main():
#     print(age)
#     f1()
# if __name__ == '__main__':
#     main()
# # import xxx:导入一个模块的所有成员，在使用时需要使用模块作为模块前缀，不容易产生命名冲突
# # import aaa,bbb:一次性导入多个模块，，不推荐使用
# # from xxx import a:从每个模块中导入指定成员。a后面加，号可以添加多个
# # from xxx import *：从模块中导入所有成员。不需要前缀，可以直接使用，容易产生命名冲突
#
# # 怎么解决名称冲突的问题：
# # 直接用import xxx
# # 使用别名解决冲突：alias
# from my_module import age as a
# age = 1000
# print(age)
# print(a)
# # 给模块起别名，省事
# import my_module as m
# print(m.age)
#
# # from xxx import *
# # 默认情况下，所有成员都会导入
# # __all__是一个列表，用于表示本模块可以被外界使用的成员，元素是成员名组成的字符串
# from my_module import *
# __all__ = ['age'] # 只对这种方式有限制作用
# 重新开始，上面全注释
import os
import sys
sys.path.append(os.path.dirname(__file__))
from day15.bb import b
print(b.b)

