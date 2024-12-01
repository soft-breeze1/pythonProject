from pyspark import SparkConf, SparkContext
import os
import json
os.environ['PYSPARK_PYTHON'] = 'C:/Users/GS_ASUS/anaconda3/python.exe'

conf = SparkConf().setMaster("local[*]").setAppName("Spark App")

sc = SparkContext(conf=conf)


# TODO 需求1:  城市销售额排名

file_rdd = sc.textFile("C:/Users/GS_ASUS/Desktop/黑马程序员python资料/第15章资料/资料/orders.txt")
# 取出json字符串
json_str_rdd = file_rdd.flatMap(lambda x: x.split("|"))
# 将一个json字符串转换为字典
dict_rdd = json_str_rdd.map(lambda x: json.loads(x))

# 取出城市和销售额数据
city_with_money_rdd = dict_rdd.map(lambda x: (x['areaName'],int(x['money'])))

# 按城市分组按销售额聚合
city_result_rdd = city_with_money_rdd.reduceByKey(lambda x,y:x+y)

# 按销售额聚合结果进行排序
result_rdd = city_result_rdd.sortBy(lambda x:x[1],ascending=False,numPartitions=1)
print("需求1的结果是: ", result_rdd.collect())

# TODO 需求2: 全部城市有哪些商品类别在售卖
# 取出所有商品的类别
category_rdd = dict_rdd.map(lambda x : x['category']).distinct()
print("需求2的结果是: ",category_rdd.collect())
# 对所有商品进行去重

# TODO 需求3: 北京有哪些商品类别在售卖
# 过滤北京市的数据
beijing_data_rdd = dict_rdd.filter(lambda x:x['areaName'] == '北京')
# 取出全部商品类别
result3_rdd = beijing_data_rdd.map(lambda x:x['category']).distinct()

print("需求3的结果是: ", result3_rdd.collect())
# 进行商品类别去重

