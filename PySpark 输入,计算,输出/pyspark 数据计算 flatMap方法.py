"""
解除嵌套
"""
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = 'C:/Users/GS_ASUS/anaconda3/python.exe'


conf = SparkConf().setMaster("local[*]").setAppName("Spark App")

sc = SparkContext(conf=conf)

# [list1,list2,list3] 变成一个list  解除嵌套

rdd = sc.parallelize(["itheima itcast 666","itheima itheima itcast","python itheima"])
rdd2 = rdd.flatMap(lambda x: x.split(" "))
print(rdd2.collect())

