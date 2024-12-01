from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = 'C:/Users/GS_ASUS/anaconda3/python.exe'


conf = SparkConf().setMaster("local[*]").setAppName("Spark App")

sc = SparkContext(conf=conf)

rdd = sc.parallelize([('男',99),("男",88),('女',99),('女',66)])

rdd2 = rdd.reduceByKey(lambda x,y: x + y)

print(rdd2.collect())

