# print("111")
"""
捕获异常
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码
"""
try:
    f = open("c:/111/abc.txt","r",encoding="utf-8")
except:
    print("出现异常了，因为文件不存在，我将open的模式，改为w模式去打开")
    f = open("c:/111/abc.txt","w",encoding="utf-8")

# 捕获指定的异常
try:
    print(name)
except NameError as e:
    print("出现了变量未定义的异常")
    print(e)

try:
    1 / 0
except(NameError,ZeroDivisionError) as e:
    print("出现了变量未定义  或者  除以0的异常错误")

try:
    f = open("c:/111/fgg.txt","r",encoding="utf-8")
except Exception as e:
    print("出现异常了")

"""
try:
    ...
except NameError as e:
    ...
else:
    ...
finally:
    ...
"""
try:
    f = open("c:/111/fgg.txt","r",encoding="utf-8")
except Exception as e:    # 有异常执行
    print("出现异常了")
    f = open("c:/111/fgg.txt","w",encoding="utf-8")
else:                     # 没异常执行
    print("好高兴，没有异常")
finally:
    print("我是finally，有没有异常我都要执行")
    f.close()

"""
模块 Module
[from 模块名] import [模块|类|变量|函数|*][as 别名]
"""
"""
import 模块名
import 模块名1，模块名2

模块名.功能名
"""
"""
time 模块
import time
print("你好")
time.sleep(5)
print("我好")
"""


"""
-----模块特定功能
from time import sleep
print("你好")
sleep(5)
print("我好")
"""


# *表示全部的意思
"""
from t
ime import *
print("你好")
sleep(5)
print("你好")
"""


"""
# 模块定义别名
import 模块名 as 别名
# 功能定义别名
from 模块名 import 功能 as 别名
"""
# import time as t
# t.sleep(5)
from time import sleep as sl
print("你好")
sl(5)
print("我很好")







