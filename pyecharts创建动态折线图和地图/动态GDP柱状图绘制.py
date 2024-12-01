from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

"""
扩展列表的sort方法
"""
my_list = [["a",33],["b",55],["c",11]]

"""
基于带名函数
"""

def choose_sort_key(mlement):
    return mlement[1]

my_list.sort(key=choose_sort_key, reverse=True)
print(my_list)

"""
基于匿名函数
"""
my_list.sort(key=lambda element: element[1], reverse=True)
print(my_list)


"""
=======================================================================================
"""


f = open("C:/111/1960-2019全球GDP数据.csv",'r',encoding='GB2312')
data_lines = f.readlines()
f.close()

# 删除第一行数据
data_lines.pop(0)
# 将数据转为字典存储，格式为:
# {年份:{[国家,gdp],[国家,gdp],......},年份:{[国家,gdp],[国家,gdp],......},......}
# {1960:{[美国,123],[中国,321],......},年份:{[美国,123],[中国,321],......},......}

data_dict = {}

for line in data_lines:
    year = int(line.split(",")[0])    #年份
    country = line.split(",")[1]      #国家
    gdp = float(line.split(",")[2])   #gdp数据
    # 如何判断字典里面有没有指定的key呢
    try:
        data_dict[year].append([country,gdp])
    except KeyError:
        # 年份第一次出现时定义一个空列表
        data_dict[year] = []   #  空列表是value的列表，不是key的列表
        data_dict[year].append([country, gdp])

"""
====================================================================================
"""

# 创建时间线对象
timeline = Timeline({"theme":ThemeType.LIGHT})

# 排序年份
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key = lambda element : element[1], reverse=True)
    # 取出本年份前8名的国家    0,1,2,3,4,5,6,7
    year_data = data_dict[year][8::-1]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])    # x 轴添加国家
        y_data.append(country_gdp[1] / 100000000)    # y 轴添加gdp数据

    bar = Bar()
    #  数据反转
    # x_data.reverse()
    # y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)" , y_data , label_opts=LabelOpts(position="right"))
    # 反转x轴和y轴
    bar.reversal_axis()

    #设置每一年图标的标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8GDP数据")
    )

    # for循环每一年的数据，基于每一年的数据，创建每一年的bar对象
    # 在for中，将每一年的bar对象添加到时间线中
    timeline.add(bar,str(year))    #--------------======名字是字符串

# 设置时间线自动播放
timeline.add_schema(
    play_interval=1000,                           #自动播放的时间间隔，单位毫秒
    is_timeline_show=True,                        #是否在自动播放的时候，显示时间线
    is_auto_play=True,                            #是否自动播放
    is_loop_play=False,                           #是否循环自动播放
)

# 绘图
timeline.render("1960-2019全球GDP前8国家.html")

