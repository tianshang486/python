# 第一题
# def func1():
#     print('abc')
#     print(3)
# def func2():
#     print('def')
#     print(4)
# func1()
# print(1)
# func2()
# print(2)
# 必须要将函数执行完毕才会进行下一步


# 第二题
# def func1():
#     print('abc')
#     print(3)
# def func2():
#     print('def')
#     func1()
#     print(4)
# print(1)
# func2()
# print(2)

# 第三题
def func2():
    print(2)
    def func3():
        print(3)
    print(4)
    func3()
    print(5)

print(6)
func2()
print(7)


