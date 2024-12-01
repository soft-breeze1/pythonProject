"""
import random
num = random.randint(1,10)
A = 5.6
print("%5.2f"%A)
print("Hello,",end='')
print("World!",end='')
"""
"""
==============================制表符 \t
"""
print("Hello,\tWorld!")
print("你好,\t世界!")

"""
============================= 双循环while实现9*9乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={j*i}\t",end='')
        j += 1
    i += 1
    print()
======================================================== print空内容，就是输出一个换行
"""
# ============================== for
# for 临时变量 in 待处理数据集:
#     循环满足条件时执行的代码
# 定义字符串name
# for 循环处理字符串
# name = "itheima"
# for i in name:
#      print(i)
"""
============================== 统计以下字符串中有多少个a
name1 = "itheima is a brand of itcast"
count = 0
for x in name1:
    if x == "a":
        count += 1
print(f"itheima is a brand of itcast中共含有：{count}个字母a")
"""
"""
========================================================
for 本质上是遍历：序列类型
range(num)
range(num1,num2)
range(num1,num2,step)
range(num)获取一个从0开始，到num结束的数字序列（不含num本身）
如 range(5)  获得的数据是：[0,1,2,3,4]
range(5,10)获得[5,6,7,8,9] 从5开始，不包含10
range(5,10,2)获得[5,7,9] step 代表数字之间的步长 （step默认是1）
"""
# for i in range(5):
#     print(i)
# for i in range(5,10):
#     print(i)
# for i in range(5,10,2):
#     print(i)
# for i in range(10):
#     print("送玫瑰花")
# num = 100
# count = 0
# for i in range(1,num):
#     if i % 2 == 0:
#         count += 1
# print(f"1到100（不含100本身）范围内，有{count}个偶数")
# for i in range(5):
#     print(i)
# i = 1
# ======================================================== for 的嵌套循环
# for i in range(1,101):
#     print(f"第{i}天。")
#     for j in range(1,11):
#         print(f"第{j}朵玫瑰花。")
#     print("小美，我喜欢你。")
# print(f"第{i}天，表白成功。")
# i = 1
# while i <= 100:
#     print(f"第{i}天。")
#     j = 1
#     while j <= 10:
#         print(f"第{j}朵玫瑰花。")
#         j += 1
#     print("小美，我喜欢你。")
# ======================================================== j = 1 要分层嵌套到 while 中
#     i += 1
# print(f"第{i}天，表白成功。")
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}*{i}={j*i}",end='\t')
#     print()
# for i in range(10,0,-2):
#     print(i)

# ======================================================== continue
# continue 不会终止循环，但只能终止它所在的循环          {{{临时中断}}}
for i in range(1,6):
    print("语句1")
    for j in range(1,6):
        print("语句2")
        continue
        print("语句3")
    print("语句4")

"""
======================================================== break
break 会终止循环，但只能终止它所在的循环               {{{永久中断}}}
for i in range(1,6):
    print("语句1")
    for j in range(1,6):
        print("语句2")
        break
        print("语句3")
    print("语句4")
"""





