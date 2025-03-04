from pyspark import SparkConf, SparkContext

# 创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("Set_Spark_App")

# 基于SparkConf类对象创建SparkContext对象
sc = SparkContext(conf=conf)

# 打印PySpark的运行版本
print(sc.version)

# 停止SparkContext对象的运行(停止PySpark程序)
sc.stop()

"""
Spark : 分布式计算框架
"""