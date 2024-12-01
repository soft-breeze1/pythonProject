"""bool_1 = True
bool_2 = False
print(f"bool_1变量的内容是:{bool_1},类型是：{type(bool_1)}")
print(f"bool_1变量的内容是:{bool_2},类型是：{type(bool_2)}")"""
# -------if 的使用 4个空格的缩进,{注意有冒号}
# A = 10
# if A == 10:
#     print("111111")
# age = 20
# if age >= 18:
#     print("我已经成年了")
#     print("即将步入大学生活")
#
# print("时间过得真快啊")
#
# print("欢迎来到黑马儿童游乐园，儿童免费，成人收费。")
# # print("请输入您的年龄：")
# age = int(input("请输入您的年龄："))
# if age >= 18:
#     print("您已成年，游玩需要补票10元。")
# else:
#     print("您未成年，可以免费游玩。")
# print("祝您游玩愉快。")
# elif
# if else elif 的条件互斥

# num = 10
# if int(input("请输入第一次猜想的数字：")) == num:
#     print("恭喜第一次就猜对了呢！")
# elif int(input("不对，再猜一次：")) == num:
#     print("猜对了。")
# elif int(input("不对，再猜最后一次：")) == num:
#     print("恭喜，最后一次机会，你猜对了。")
# else:
#     print("Sorry,全部猜错了，我想的是：10")

# import random
# num = random.randint(1, 10)
# guess_num = int(input("请输入你要猜测的数字："))
# if guess_num == num:
#     print("恭喜，第一次就猜中了")
# else:
#     if guess_num > num:
#         print("你猜测的数字大了")
#     else:
#         print("你猜测的数字小了")
#     guess_num = int(input("请再次输入你要猜测的的数字："))
#     if guess_num == num:
#         print("恭喜，第二次猜中了")
#     else:
#         if guess_num > num:
#             print("你猜测的数字大了")
#         else:
#             print("你猜测的数字小了")
#         guess_num = int(input("请第三次输入你要猜测的的数字："))
#         if guess_num == num:
#             print("第三次猜中了")
#         else:
#             print("第三次机会用完了，没有猜中。")

"""
==============================
while 循环语句的使用
while 条件:
    条件满足时，做的事情1
    条件满足时，做的事情2
    条件满足时，做的事情3
    ......
"""
# i = 0
# while i < 10:
#     print(i)
#     i += 1
# i = 1
# sum = 0
# while i <= 100:
#     sum += i
#     i += 1
# print(sum)
"""
import  random
num = random.randint(1, 100)
i = 0
guess_number = 0
while guess_number != num:
    if guess_number < num:
        print("猜测的数字小了")
    else:
        print("猜测的数字大了")
    guess_number = int(input("请输入数字："))
    i += 1
print(f"你猜中了，你猜了{i}次")
"""
# =========================================================bool
import  random
num = random.randint(1, 100)
count = 0
flag = True
while flag:
    guess_number = int(input("请输入数字："))
    count += 1
    if guess_number == num:
        print("猜中了")
        flag = False
    else:
        if guess_number > num:
            print("猜测的数字大了")
        else:
            print("猜测的数字小了")
print(f"你猜中了，你猜了{count}次")