from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = 'C:/Users/GS_ASUS/anaconda3/python.exe'

conf = SparkConf().setMaster("local[*]").setAppName("Spark App")

sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])
# def func(data):
#     return data * 10
#
# rdd2 = rdd.map(func)
"""
-----------map 算子
-----------链式调用
-----------(T) -> U
"""
rdd2 = rdd.map(lambda x: x * 10).map(lambda x: x + 5)


print(rdd2.collect())

# (T) -> T

