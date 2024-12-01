"""
字典(映射)
"""
"""
键值对
{key:value,key:value,......,key:value}
空字典
my_dict = {}
my_dict = dict()
"""
my_dict = {'王力宏':99,'周杰伦':88,'林俊杰':77}
my_dict2 = {}  #  不是集合，而是字典
my_dict3 = dict()
print(f"字典1的内容是:{my_dict},类型是:{type(my_dict)}")
print(f"字典2的内容是:{my_dict2},类型是:{type(my_dict2)}")
print(f"字典3的内容是:{my_dict3},类型是:{type(my_dict3)}")


#  不重复
my_dict4 = {'王力1':99,'王力宏':88,'林俊杰':77}
print(my_dict4)

print(my_dict4["王力宏"])

# key 不可以是字典

stu_score_dict = {
    '王力宏':{
        '语文':77,
        '数学':66,
        '英语':33
    },'周杰伦':{
        '语文':88,
        '数学':86,
        '英语':55
    },'林俊杰':{
        '语文':99,
        '数学':96,
        '英语':66
    }
}
print(f"学生的考试信息是:{stu_score_dict}")
print(stu_score_dict['王力宏']['语文'])


"""
增加元素    更新元素
"""
my_dict5 = {'王力宏':99,'周杰伦':88,'林俊杰':77}
my_dict5['张召忠'] = 100
print(my_dict5)
my_dict5['王力宏'] = 55
print(my_dict5)


"""
删除元素    清空字典
"""
my_dict5.pop('周杰伦')
print(my_dict5)

my_dict5.clear()
print(my_dict5)



"""
获取全部的key
"""
my_dict5 = {'王力宏':99,'周杰伦':88,'林俊杰':77}
keys = my_dict5.keys()
print(keys)

"""
遍历字典
"""
for key in keys:
    print(key)
    print(my_dict5[key])
for key in my_dict5:
    print(key)
    print(my_dict5[key])
num = len(my_dict5)
print(num)


yuangong_message = {
    '王力宏':{
        '部门':'科技部',
        '工资':3000,
        '级别':1
    },'周杰伦':{
        '部门':'市场部',
        '工资':5000,
        '级别':2
},    '林俊杰':{
        '部门':'市场部',
        '工资':7000,
        '级别':3
} ,   '张学友':{
        '部门':'科技部',
        '工资':4000,
        '级别':1
} ,   '刘德华':{
        '部门':'市场部',
        '工资':6000,
        '级别':2
}
}
print(f"全体员工当前信息如下:\n{yuangong_message}")
for name in yuangong_message:
    if yuangong_message[name]['级别'] == 1:
        yuangong_message[name]['级别'] = 2
        yuangong_message[name]['工资'] += 1000
    else:
        continue
print(yuangong_message)

tuple1 = (1,2,3)
index = 0
while index < len(tuple1):
    print(tuple1[index])
    index += 1
print(tuple1[0])

A = max(tuple1)
B = min(tuple1)
print(A)
print(B)

my_dict6 = {'王力宏':99,'周杰伦':88,'林俊杰':77}
print(max(my_dict6))
print(min(my_dict6))

# 容器 的 排序
my_list1 = [3,1,2,5,4]
my_tuple = (3,1,2,5,4)
my_str = '31254'
my_set = {3,1,2,5,4}
my_dict = {'key1':3, 'key2':1, 'key3':2, 'key4':5, 'key5':4}
print(sorted(my_list1))
print(sorted(my_tuple))
print(sorted(my_str))
print(sorted(my_set))
print(sorted(my_dict))
                             # 全变成list


"""
倒序
"""
print(sorted(my_list1,reverse=True))
print(sorted(my_tuple,reverse=True))
print(sorted(my_str,reverse=True))
print(sorted(my_set,reverse=True))
print(sorted(my_dict,reverse=True))

"""
字符串大小比较
从头到尾比较，一位位比较，其中一位大，后面就无需比较了
"""

print('abd' > 'abc')
print('ab' > 'a')
print('a' > 'A')
print('ad' < 'bc')
#  a 比  b 小   ， 不用看  d  大于  c 了