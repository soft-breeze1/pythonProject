# name = "itheima"
# length = len(name)
# print(length)

# str1 = "itheima"
# len()函数   内置函数
# str2 = "itcast"
# str3 = "python"

# count = 0
# for i in str1:
#     count += 1
# print(f"字符串{str1}的长度是：{count}")
#
# count = 0
# for i in str2:
#     count += 1
# print(f"字符串{str2}的长度是：{count}")
#
# count = 0
# for i in str3:
#     count += 1
# print(f"字符串{str3}的长度是：{count}")
#
# def my_len(data):
#     count = 0
#     for i in data:
#         count += 1
#     print(f"字符串{data}的长度是：{count}")
#
# my_len(str1)
# my_len(str2)
# my_len(str3)

"""
================================================== def
def 函数名(传入参数):
    函数体
    return 返回值
"""

def say_hi():
    print("Hi,我是黑马程序员，学Python来黑马")
resurt = say_hi()
print(f"{resurt},{type(resurt)}")
# ===================================================换行符 \n
# print("静安分局案发。\n大大苏打大。")
# ==========================================a,b为形式参数，传入的5和6为实际参数
# def add(a, b):
#     result = a + b
#     print(result)
# add(1, 2)
# add(3, 4)
# add(5,7)

# def caheshuan(a):
#     print("欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并配合测量体温！")
#     if a <= 37.5:
#         print(f"体温测量中，您的体温是：{a}度，体温正常请进！")
#     else:
#         print(f"体温测量中，您的体温是：{a}度,需要隔离！")
# caheshuan(37.3)
# caheshuan(39.3)

# ===========================================================return 返回值
# def add(a, b):
#     result = a + b
#     return result
# c = add(4, 6)
# print(c)

# ================================================================None

"""
if not result=====等同于如果result为假，则not result 为真,就可以进入到if中的循环中。
"""
"""
函数的说明文档
"""
# ================================================== global 关键字
# num = 100
#
# def test1():
#     print(num)
#
# def test2():
#     #======================global关键字声明a是全局变量
#     global num
#     num = 200
#     print(num)
#
# test1()
# test2()
# print(num)
# 修改了num的值
