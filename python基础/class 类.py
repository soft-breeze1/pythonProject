"""
创建一个类
"""
class Student:
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None

# 创建一个对象
stu_1 = Student()

# 对象属性进行赋值
stu_1.name = '林俊杰'
stu_1.gender = '男'
stu_1.nationality = '中国'
stu_1.native_place = '山东省'
stu_1.age = 31

# 获取对象中记录的信息
print(stu_1.name)
print(stu_1.gender)
print(stu_1.nationality)
print(stu_1.native_place)
print(stu_1.age)

"""
类的成员方法  self     {成员方法, 成员变量}
"""
class Student:
    name = None
    def say_hi(self):
        print(f"大家好啊,我是{self.name},欢迎大家多多关照")

    def say_hi2(self,msg):
        print(f"大家好,我是:{self.name},{msg}")


stu = Student()
stu.name = '周杰伦'
stu.say_hi2("哎哟,不错呦")

stu2 = Student()
stu2.name = '林俊杰'
stu2.say_hi2("小伙子,我看好你")

stu2 = Student()
stu2.name = '蔡徐坤'
stu2.say_hi2("练习时长两年半的个人练习生")


class Clock:
    id = None
    price = None
    def ring(self):
        import winsound
        winsound.Beep(2000,3000)
# -------------------(频率,时间)

clock1 = Clock()
clock1.id = "003032"
clock1.price = 16.66
print(f"闹钟ID:{clock1.id},价格:{clock1.price}")
clock1.ring()

clock2 = Clock()
clock2.id = "003033"
clock2.price = 21.99
print(f"闹钟ID:{clock1.id},价格:{clock1.price}")
clock2.ring()




