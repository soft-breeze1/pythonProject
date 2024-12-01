"""
exit() 退出python环境
"""

"""
dasawoyexiasjsw
"""
print("Hello World")
print(type("SANDBANK"))
# 写一个整形字面量
print(666)
print("sasassa")
money = 50
print("钱包还有:",money)
money = money - 10
print("还剩余:",money,"元")
print(type(money))
int_type = type(money)
print(int_type)
num_str = str(11)
print(type(num_str),num_str)
float_str = str(1.5)
print(type(float_str),float_str)
num_int = int("11")
print(type(num_int),num_int)
float = float("1.23")
print(type(float),float)
num = int("2121")
print(type(num),num)
q = 121
print(type(q),q)
fdsf = "1212"
name = "张三"
nAme = 666
print(name)
print(nAme)
Class = 111
print(Class)
print("1+1=",1+1)
print("2+2=",2+2)
print("11//2=",11//2)
print("11%2=",11%2)
print("11**2=",11**2)
a=1
c=2
c+=a
print(c)
c%=a
print(c)
"""
raise
"""
name = '"sasasa"'
print(name)
# \用来注释
name = "\"kxkixkk\""
print(name)
# 字符串的拼接
name1 = "张飞"
age = "22"
number = "20021020"
print("我的年龄为"+age+",我的名字是"+name1+",我的学号为"+number)
# 字符串格式化
name = "黑马程序员"
message = "学IT就来 %s" % name
print(message)
mk = 11
js = 22
meeeee = "第一个数字是 %s, 第二个数字是 %s" % (mk, js)
print(meeeee)
print("第一个数字是 %s, 第二个数字是 %s" % (mk, js))
name2 = "王亮"
age2 = 25
money2 = 18.88
message2 = "%s,他的年龄为 %d ,他现在钱包还有 %.2f " % (name2,age2,money2)
print(message2)
# 字符串的精度控制            [[[[[[m.n]]]]]
number2 = 4.35555
print("%7.4f"%number2)
"""
4.35555 的宽度为7位，设置宽度小于7位不生效，设置宽度大于等于7位才有用
"""
# 快速格式化
# f"内容{变量}"
# f: format
print(f"{name2}, 他的年龄为{age2}, 他现在钱包还有{money2}")
print(f"1+2的结果是：{1+2}")
print("2+2的结果是：%d" %(2+2))
print("字符串在Python中的类型名是： %s" % type("字符串"))
