"""
__str__
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # __str__    实现类对象 转 字符串的行为
    def __str__(self):
        return f"Student类对象，name:{self.name}, age:{self.age}"

    # __lt__     小于大于的比较
    def __lt__(self, other):
        return self.age < other.age

    # __le__     小于等于,大于等于 比较符号方法
    def __le__(self, other):
        return self.age <= other.age

    # __eq__      比较运算符实现方法
    def __eq__(self, other):
        return self.age == other.age

stu1 = Student("周杰伦", 31)
print(stu1)
print(str(stu1))


stu1 = Student("周杰伦", 31)
stu2 = Student("林俊杰", 36)
print(stu1 <= stu2)
print(stu1 >= stu2)
print(stu1 == stu2)






