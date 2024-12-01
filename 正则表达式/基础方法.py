import re

s = "python itheima"
# match 从头匹配,不看后面匹不匹配
result = re.match("python", s)
print(result)
print(result.span())
print(result.group())

# search 搜索匹配
se = "1python itheima python python"
result1 = re.search("python", se)
print(result1)
print(result1.span())
print(result1.group())

# findall 搜索全部匹配
result2 = re.findall("python",se)
print(result2)

