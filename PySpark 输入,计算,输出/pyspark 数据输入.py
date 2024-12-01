from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("Spark App")

sc = SparkContext(conf=conf)

# # 通过parallelize方法将python对象加载到Spark内，成为RDD对象
# rdd1 = sc.parallelize([1, 2, 3, 4, 5])
# rdd2 = sc.parallelize((1, 2, 3, 4, 5))
# rdd3 = sc.parallelize("abcdefg")
# rdd4 = sc.parallelize({1, 2, 3, 4, 5})
# rdd5 = sc.parallelize({"key1":"value1", "key2":"value2"})
# """
# RDD打印字符串会将其拆分，一个一个字母打印
# RDD打印字典只会输出  key  ,不会输出  alue
# """
#
# # 如果要查看RDD里面有什么内容，需要用collect()方法
# print(rdd1.collect())
# print(rdd2.collect())
# print(rdd3.collect())
# print(rdd4.collect())
# print(rdd5.collect())


rdd = sc.textFile("C:/111/111.txt")
print(rdd.collect())
# 用过textFile方法，读取文件数据加载到Spark内，成为RDD对象

sc.stop()

