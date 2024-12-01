"""
collect
将RDD各个分区内的数据，统一收集到Driver中，形成一个 List 对象
"""
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = 'C:/Users/GS_ASUS/anaconda3/python.exe'

conf = SparkConf().setMaster("local[*]").setAppName("Spark App")

sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])

"""
reduce
对RDD数据集按照你传入的逻辑进行聚合
func (T,T) -> T
"""

num = rdd.reduce(lambda x, y: x + y)
print(num)

"""
take
取RDD的前N个元素，组合成 list 返还给你
"""

take_list = rdd.take(3)
print(take_list)

"""
count
计算RDD有多少条数据，返回值是一个数字
"""
num_count = rdd.count()
print(f"RDD内有{num_count}个元素")

sc.stop()