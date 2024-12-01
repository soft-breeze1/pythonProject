"""
saveAsTextFile
"""
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = 'C:/Users/GS_ASUS/anaconda3/python.exe'
os.environ['HADOOP_HOME'] = "C:/Users/GS_ASUS/Desktop/黑马程序员python资料/第15章资料/资料/hadoop-3.0.0"

conf = SparkConf().setMaster("local[*]").setAppName("Spark App")
"""
方式1 :
conf.set("spark.default.parallelism", "1")
"""
sc = SparkContext(conf=conf)

rdd1 = sc.parallelize([1, 2, 3, 4, 5],numSlices=1)

rdd2 = sc.parallelize([('hello',3),('Spark',5),('Hi',7)],1)

rdd3 = sc.parallelize([[1,3,5],[6,7,9],[11,13,11]],1)

# 输出到文件中
rdd1.saveAsTextFile("D:/output1")
rdd2.saveAsTextFile("D:/output2")
rdd3.saveAsTextFile("D:/output3")

