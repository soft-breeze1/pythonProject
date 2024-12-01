"""
演示变量的类型注解
"""
import json
import random

# 基础数据类型注解
var_1: int = 10
var_2: str = 'itheima'
var_3: bool = True

# 类对象类型注解
class Student:
    pass
stu: Student = Student()

# 基础容器类型注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_dict: dict = {'itheima':666}

# 容器类型详细注解
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int,str,bool] = (1, 'itheima', True)
my_dict: dict[str,int] = {'itheima':666}

# 在注释中进行类型注解
var_1 = random.randint(1,10)   # type:int
var_2 = json.loads('{"name":"zhangsan"}')  # type: dict[str,str]
def func():
    return 10
var_3 = func()      # type:int

# 类型注解的限制
var_4: int = 'itheima'
var_5: str = 123


"""
形参注解
"""
def add(a:int, b:int):
    return a + b

#  返回值的类型注解
def func(data:list) -> list:
    return data

print(func(1))



"""
Union联合类型注释
使用Union类型 必须先导包
"""
from typing import Union

my_list: list[Union[int,str]] = [1,2,'itheima','itcast']

def func(data:Union[int,str]) -> Union[int,str]:
    pass
func(True)



