"""
集合  会  去重
无序     存储
"""
"""
空集合
set()
"""
my_set = {"黑马程序员",1,2}
print(my_set)
b = set(my_set)
print(b)

# 集合  元素  的  添加          add
my_set.add(3)
print(my_set)

# 移除元素                     remove
my_set.remove(3)
print(my_set)

# 元素  随机  取出               pop
element = my_set.pop()
print(element)
print(my_set)

# 集合清空                     clear
my_set.clear()
print(my_set)

my_set = {"黑马程序员",1,2}

"""
集合取差集                   difference  
{集合1特有的}
取  集合1 有的 但 集合2 没有的元素
"""
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference(set2)
print(f"取出差集后的set3:{set3}")
print(set1)
print(set2)

"""
                    集合1.difference_update(集合2)
{相同的删除}
==========    将集合1中与集合2相同的元素删除
===================  只  修改了 集合1  ，没修改集合2
"""
set1 = {1,2,3}
set2 = {1,5,6}
set1.difference_update(set2)
print(set1)
print(set2)

# 集合合并                     union
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.union(set2)
# -----------------------不要  重复的  元素
print(set3)
print(set1)
print(set2)

# 统计集合元素  len()
set1 = {1,2,3,4,5}
num = len(set1)
print(num)

"""
集合的遍历
集合不支持下标索引，不能用while循环
可以用for循环
"""
set1 = {1,2,3,4,5}
for element in set1:
    print(element)



#  list 的元素  变成  集合中的元素

my_list = ['黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast','itheima','itcast','best']
a = set()
for element in my_list:
    a.add(element)
print(a)
