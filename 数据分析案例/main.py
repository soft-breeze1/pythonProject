"""
数据分析案例
"""

"""
面向对象，数据分析案例，主业务逻辑代码
实现步骤：
1.设计一个类，可以完成数据的封装
2.设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
3.读取文件，生产数据对象
4.进行数据需求的逻辑计算（计算每一天的销售额）
5.通过PyEcharts进行图形绘制
"""

from file_define import FileReader,TextFileReader,JsonFileReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType


test_file_reader = TextFileReader("C:/111/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("C:/111/2011年2月销售数据JSON.txt")

jan_data:list[Record] = test_file_reader.read_data()
fed_data:list[Record] = json_file_reader.read_data()
# 将2个月份的数据合并为1个list来存储
all_data:list[Record] = jan_data + fed_data
# for i in all_data:
#     print(i)

# 开始进行数据计算
# {"2011-01-01":1274}
data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        # 当前日期已经有记录了，所以和老记录做累加即可
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

# print(data_dict)

# 可视化图表开发
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(data_dict.keys()))               #添加x轴的数据
bar.add_yaxis("销售额",list(data_dict.values()),label_opts=LabelOpts(is_show=False))     #添加y轴的数据
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)

bar.render("每日销售额柱状图.html")