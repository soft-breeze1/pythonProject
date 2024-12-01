from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = 'C:/Users/GS_ASUS/anaconda3/python.exe'

conf = SparkConf().setMaster("local[*]").setAppName("Spark App")
conf.set("spark.default.parallelism","1")

sc = SparkContext(conf=conf)

#  TODO 需求1 : 热门搜索时段Top3(小时精度)

file_rdd = sc.textFile("C:/Users/GS_ASUS/Desktop/黑马程序员python资料/第15章资料/资料/search_log.txt")
result1 = file_rdd.map(lambda x: (x.split("\t")[0][:2],1)).\
    reduceByKey(lambda x,y:x+y).\
    sortBy(lambda x:x[1],ascending=False,numPartitions=1).\
    take(3)
print(f"需求1的结果是:{result1}")

#  TODO 需求2 : 热门搜索词Top3

result2 = file_rdd.map(lambda x: (x.split("\t")[2],1)).\
    reduceByKey(lambda x,y:x+y).\
    sortBy(lambda x:x[1],ascending=False,numPartitions=1).\
    take(3)
print(f"需求2的结果是:{result2[0][0]},{result2[1][0]},{result2[2][0]}")

#  TODO 需求3 : 统计黑马程序员关键字在什么时候被搜索的最多

result3 = file_rdd.map(lambda x:x.split("\t")).\
    filter(lambda x:x[2] == '黑马程序员').\
    map(lambda x:(x[0][:2],1)).\
    reduceByKey(lambda x,y:x+y).\
    sortBy(lambda x:x[1],ascending=False,numPartitions=1).\
    take(1)
print(f"需求3的结果是:{result3[0][0]}")

#  TODO 需求4 : 将数据转换为JSON格式，写出到文件中

result4 = file_rdd.map(lambda x:x.split("\t")).\
    map(lambda x: {"time": x[0],"user_id": x[1],"key_word": x[2],"rank1": x[3],"rank2": x[4],"url": x[5]}).\
    saveAsTextFile("D:/output_json")