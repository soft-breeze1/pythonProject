"""
__init__
"""
class Student:
    name = None   #可以省略
    age = None    #可以省略
    tel = None    #可以省略
    # 构建类对象会自动执行
    def __init__(self, name, age,tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创建了一个类对象")

stu = Student("周杰伦","31","18500006666")
print(stu.name)
print(stu.age)
print(stu.tel)

class Student:
    # name = None
    # age = None
    # adress = None
    def __init__(self, name, age, adress):
        self.name = name
        self.age = age
        self.adress = adress
        print(f"学生{i}信息录入完成,信息为:【学生姓名:{self.name},年龄:{self.age},地址:{self.adress}】")

for i in range(1,11):
    input(f"当前录入第{i}位学生信息,总共需录入10位学生信息")
    stu = Student(input("请输入学生姓名:"),int(input("请输入学生年龄:")),input("请输入学生地址:"))
