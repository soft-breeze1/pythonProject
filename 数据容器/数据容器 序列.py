# 切片
# 序列[起始下标:结束下标:步长]
# 不包含 结束下标
# 步长 表示 取元素的间隔
my_list = [0,1,2,3,4,5,6]
result = my_list[1:4]   # 步长默认是1，可以省略
print(result)


my_tuple = (0,1,2,3,4,5,6)
result1 = my_tuple[:]    # 起始和结束不写 代表从头到尾
print(result1)


my_str = "01234567"
result2 = my_str[::2]
print(result2)
result3 = my_str[::-1]    # 倒过来
print(result3)


my_tuple = (0,1,2,3,4,5,6)
result4 = my_tuple[::-2]
print(result4)

str = "万过薪月，员序程马黑来，nohtyP学"
# new_str = str[::-1]
# print(new_str)             # 倒序字符串
# a = new_str[9:14:1]
# print(a)

# b = str[5:10:1][::-1]
# print(b)
# 不能直接将字符倒序打印，要先正序打印，再倒序打印

# c = str[9:4:-1]
# print(c)
# 先从开始的9，再4

d = str.split('，')       #  split后得到list
print(d)
# a = d[1]
# print(a)
d1 = str.split('，')[1].replace('来','')[::-1]
print(d1)
