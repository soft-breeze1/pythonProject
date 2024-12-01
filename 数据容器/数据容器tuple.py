# tuple 元组
# tuple = (1,2,3,4,5)
# print(tuple)
# print(type(tuple))
# ---------------------单个元素的元组要在后面加一个逗号
# t = ("hello",)
# print(t)
# t1 = ((1,2,3),(4,5,6))
# print(t1)
# a = t1[1][2]
# print(a)
# b = t1.count((4,5,6))
# print(b)
# 元组不可修改
# index = 0
# t2 = (1,2,3,4,5,6,7,8,9)
# while index < len(t2):
#     print(t2[index])
#     index += 1
# for element in t2:
#     print(element)

# 元组内部的  list  可以修改
# t3 = (1,2,[3,4])
# print(t3)
# t3[2][0] = 1
# t3[2][1] = 5
# print(t3)

student_message = ('周杰伦',11,['football','music'])
student_age = student_message[1]
print(f"其年龄所在的下标位置为:{student_age}")
student_name = student_message[0]
print(f"学生的姓名为:{student_name}")
student_message[2].pop(0)
student_message[2].append('coding')
print(student_message)
