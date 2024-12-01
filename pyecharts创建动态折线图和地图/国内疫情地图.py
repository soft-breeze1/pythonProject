import json
from pyecharts.charts import Map
from pyecharts.options import *

f = open("C:/python文本文件/疫情.txt", 'r', encoding='utf8')
data = f.read()
f.close()

data_dict = json.loads(data)
# 从字典中取出省份的数据
province_data_list = data_dict["areaTree"][0]["children"]

# 组装每个省份和确诊人数为元组，并将各个省的数据豆封装到列表内
data_list = []
for province_data in province_data_list:
    # 省份名称
    if province_data["name"] == "上海":
        province_name = province_data["name"]+"市"
    elif province_data["name"] == "北京":
        province_name = province_data["name"]+"市"
    elif province_data["name"] == "重庆":
        province_name = province_data["name"]+"市"
    elif province_data["name"] == "天津":
        province_name = province_data["name"]+"市"
    elif province_data["name"] == "香港":
        province_name = province_data["name"]+"市"
    elif province_data["name"] == "澳门":
        province_name = province_data["name"]+"市"
    elif province_data["name"] == "内蒙古":
        province_name = province_data["name"] + "自治区"
    elif province_data["name"] == "新疆":
        province_name = province_data["name"] + "维吾尔自治区"
    elif province_data["name"] == "西藏":
        province_name = province_data["name"] + "自治区"
    elif province_data["name"] == "宁夏":
        province_name = province_data["name"] + "回族自治区"
    elif province_data["name"] == "广西":
        province_name = province_data["name"] + "壮族自治区"
    else:
        province_name = province_data["name"]+"省"
    # 省份确诊人数
    province_confirm = province_data["total"]["confirm"]
    data_list.append((province_name, province_confirm))
print(data_list)

map = Map()
map.add("各省份确诊人数", data_list,"china")

map.set_global_opts(
    title_opts = TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,         #是否显示
        is_piecewise=True,   #是否分段
        pieces=[
            {"min":1,"max":99,"label":"1-99","color":"#CCFFFF"},
            {"min":100,"max":999,"label":"100-999","color":"#FFFF99"},
            {"min":1000,"max":4999,"label":"1000-4999","color":"#FF9966"},
            {"min":5000,"max":9999,"label":"5000-9999","color":"#FF6666"},
            {"min":10000,"max":99999,"label":"10000-99999","color":"#CC3333"},
            {"min":100000,"label":"100000+","color":"#990033"},
        ]
    )
)

map.render("全国疫情地图.html")