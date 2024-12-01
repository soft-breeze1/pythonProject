"""
json 本质上是一个带有特定格式的字符串
不同语言的传递数据格式
"""
"""
json数据的格式,json内部都是字典
{"name":"admin","age":18}
"""

"""
列表或字典可以转换为json格式
"""
import json
data = [{"name":"老王","age":18},{"name":"张三","age":20}]
# 将 python 数据转换为   json  格式
data = json.dumps(data,ensure_ascii=False)
# 如果有中文，就不用 ascii码去转换他
print(data)
print(type(data))

d = {"name":"周杰伦","age":18}
json_str = json.dumps(d,ensure_ascii=False)
print(json_str)
print(type(json_str))

"""
将json数据转换为   python  格式
data = json.loads(data)
"""

s = '[{"name":"老王","age":18},{"name":"张三","age":20}]'
list = json.loads(s)
print(list)
print(type(list))

z = '{"name":"周杰伦","age":18}'
k = json.loads(z)
print(k)
print(type(k))







