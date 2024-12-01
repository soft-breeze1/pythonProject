"""
多  返回  值
"""
def test_return():
    return 1,'小孩子',[1,2,3]
x,y,z = test_return()
print(x)
print(y)
print(z)

"""
=位置参数
=关键字参数
=缺省参数
=不定长参数
"""
def user_info(name,age,gender):
    print(f"姓名是:{name},年龄是:{age},性别是:{gender}")

# 位置参数
user_info('小明',20,'男')

# 关键字参数
user_info(name = '潇潇',age = 11,gender = '女')
user_info(age = 11,gender = '男',name = '小王')
user_info('甜甜',gender = '女',age = 9)

# 缺省参数
# 默认参数
def user_info(name,age,gender = '男'):
    #默认参数   gender = '男'  必须在最后
    print(f"姓名是:{name},年龄是:{age},性别是:{gender}")
user_info('小天',13)
user_info('小天',13,gender='女')

"""
不定长参数，也叫 可变参数
分为 {位置传参} 和 {关键字传参}
"""
# \\\\\\\\\\\\\\\\\\\\\\\\\\\{位置传参}
def user_info(*args):
    print(args)
user_info('Tom')
user_info('Tom',18)
#============================形成一个元组tuple

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\{关键字传参}
def user_info(**kwargs):    #key word  == kw
    print(kwargs)
user_info(name = 'Tom',age = 18,id = 110)

#=============================形成一个 字典{   }


#  函数作为参数

def test_func(compute):
    result = compute(1,2)
    print(f"compute参数的类型是:{type(compute)}")
    print(f"计算结果是:{result}")

def compute(x,y):
    return x + y
test_func(compute)
