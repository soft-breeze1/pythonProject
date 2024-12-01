"""
对RDD数据进行去重，返回新RDD
"""
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = 'C:/Users/GS_ASUS/anaconda3/python.exe'

conf = SparkConf().setMaster("local[*]").setAppName("Spark App")

sc = SparkContext(conf=conf)


rdd = sc.parallelize([1,1,3,3,5,5,7,8,9,10])

rdd2 = rdd.distinct()

print(rdd2.collect())

