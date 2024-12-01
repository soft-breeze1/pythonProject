from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = 'C:/Users/GS_ASUS/anaconda3/python.exe'

conf = SparkConf().setMaster("local[*]").setAppName("Spark App")

sc = SparkContext(conf=conf)

"""
rdd.sortBy(func,ascending=False,numPartitions=1)
"""
rdd = sc.textFile("C:/Users/GS_ASUS/Desktop/黑马程序员python资料/第15章资料/资料/hello.txt")
# 取出全部单词
word_rdd = rdd.flatMap(lambda x: x.split(" "))
# 将所有单词都转换成二元元组，单词位Key，value设置为1
# (hello,1) (spark,1) (itheima,1) (itheima,1)
word_with_one_rdd = word_rdd.map(lambda word: (word, 1))

# 分组并求和
result_rdd = word_with_one_rdd.reduceByKey(lambda x, y: x + y)

# 降序排列
final_rdd = result_rdd.sortBy(lambda x:x[1],ascending=False,numPartitions=1)

print(final_rdd.collect())

