# def outer(func):
#     def inner():
#         print("我睡觉了")
#         func()
#         print("我起床了")
#
#     return inner
#
#
# def sleep():
#     import time
#     import random
#     print("睡眠中......")
#     time.sleep(random.randint(1,10))
#
# # sleep()
#
# fn = outer(sleep)
# fn()

# outer(sleep)()

"""
语法糖
"""

def outer(func):
    def inner():
        print("我睡觉了")
        func()
        print("我起床了")

    return inner

@outer
def sleep():
    import time
    import random
    print("睡眠中......")
    time.sleep(random.randint(1,10))

sleep()

# fn = outer(sleep)
# fn()








