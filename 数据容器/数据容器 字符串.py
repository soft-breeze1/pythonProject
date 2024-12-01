my_str = "itheima and itcast"
value1 = my_str[2]
print(value1)
value2 = my_str[-1]
print(value2)
# 字符串是不可修改的容器
a = my_str.index('and')
print(a)

# ********
# 字符串的替换   replace  得到一个新字符串
new_my_str = my_str.replace('it','程序')
print(new_my_str)
# 字符串的分割   split
my_str1 = "hello python itheima itcast"
new_my_str1 = my_str1.split(" ")
# 空格 为 分隔符
print(new_my_str1)
# 字符串的规整,去前后空格或字符。  strip
my_str2 = "212312 1"
my_str3 = my_str2.strip("212")  #----!!!!!!!!!
print(my_str3)
# **********

count = my_str2.count("12")
print(count)

jjjj = "itheima itcast boxuegu"
a = jjjj.count("it")
print(f"有{a}个it字符")
new_jjjj = jjjj.replace(' ','|')
print(f"替换后的字符串为:{new_jjjj}")
a = new_jjjj.split("|")
print(f"分割后得到:{a}")


str33 = "上海"
list1 =str33.split();
print(list1)
print(list1.append('市'))

a11 = ['上','海']
a11.append('市')
print(a11)
a222 = str(a11.append('市'))
print(a222)


str333 = "上海"
str333 = str333+"市"
print(str333)

