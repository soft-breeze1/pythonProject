"""
rdd.fliter(func)
# func:(T) -> bool 传入一个参数进来随意类型，
返回值必须是True or False
"""
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = 'C:/Users/GS_ASUS/anaconda3/python.exe'

conf = SparkConf().setMaster("local[*]").setAppName("Spark App")

sc = SparkContext(conf=conf)

rdd = sc.parallelize([1,2,3,4,5])

# 对RDD中的数据进行过滤
rdd2 = rdd.filter(lambda num: num % 2 == 0)
# True就保留，False就不要了

print(rdd2.collect())

