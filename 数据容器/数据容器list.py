# 数据容器类型:列表(list),元组(tuple),字符串(str),
# 集合(set),字典(dict)
# 变量名称 = []
# 变量名称 = list()
# name_list = ['ss',554,True]
# print(name_list)
# print(type(name_list))
# list = [[1,2,3],[1,"a",False]]
# print(list)
# ==================下标索引 0 ,1,2,3,4
# 或者  -1,-2,-3,-4
# print(list[0][2])
# print(list[-1][1])
# print(list[1])
"""
在python中，如果将函数定义为class(类)的成员，
那么函数和称之为:方法
"""
# 1 查下标  index
list = ['ss',554,True]
# index = list.index('ss')
# print(index)
# 2 修改元素值  list[i] = x
# list[0] = 'q'
# print(list[0])
# 3 插入元素  insert(i,x)  i是指定位置
# list.insert(1,"aaaa")
# print(list)
# 4.1 追加元素  append()追加单个元素到列表尾部
# list.append("洒洒水")
# print(list)
# 4.2 extend(其他数据容器)将其他数据容器的内容全加到列表尾部
list1 = [1,2,3,4,5]
list.extend(list1)
print(list)
# 5.1 元素的删除  del 列表[下标]
# del list[0]      # []
# print(list)
# 5.2 列表.pop(下标)
# a = list.pop(1)      # 删除特定下标元素
# print(list)
# print(a) #取出的元素
# 6 列表修改   列表.remove(元素)  ------删除特定元素
# list.remove(2)
# print(list)
# 7 列表清空内容    列表.clear()
# list.clear()
# print(list)
# 8 统计列表中某元素数量    列表.count(元素)
# list.insert(4,1)
# print(list)
# b = list.count(1)
# print(b)
# # 9 统计列表数量 len(列表)
# c = len(list)
# print(c)
#
list3 = [21,25,21,23,22,20]
list3.append(31)
list3.extend([29,33,30])
print(list3)
h = list3[0]
print(list3)
print(f"取出第一个元素为{h}")
j = list3[-1]
print(f"取出最后一个元素为{j}")
index = list3.index(31)
print(index)

# list 的循环遍历         - -- - - -while  - - - - -for
# def list_while_func():
#     my_list = [1,2,3,4,5]
#     index = 0
#     while index < len(my_list):
#         element = my_list[index]
#         print(f"列表的元素：{element}")
#         index += 1
# list_while_func()
# def list_while_func():
#     my_list = [1, 2, 3, 4, 5]
#     for element in my_list:
#         print(f"列表的元素：{element}")
# list_while_func()

my__list = [1,2,3,4,5,6,7,8,9,10]
index = 0
new_list = []
for element in my__list:
    if element %2 == 0:
        new_list.append(element)
    else:
        continue
print(new_list)


while index < len(my__list):
    if my__list[index]%2 == 0:
        new_list.append(my__list[index])
        index += 1
    else:
        index += 1
print(new_list)




