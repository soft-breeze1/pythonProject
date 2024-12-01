"""
演示地图可视化的基本使用
"""
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
# 准备地图对象
map = Map()
# 准备数据
data = [
    ("北京市",2),
    ("上海市",55),
    ("湖南省",299),
    ("台湾省",156),
    ("广东省",83)
]
# 添加数据


"""
========-=-=--=-=--=-===-===-=-地图数据是列表，里面是元组
"""


# map.add(地图名，地图数据，地图类型)
map.add("测试地图", data, "china")

# 设置全图选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":9,"label":"1-9","color":"#CCFFFF"},
            {"min":10,"max":99,"label":"10-99","color":"#FF6666"},
            {"min":100,"max":500,"label":"100-500","color":"#990033"},
        ]
    )
)

# 绘图
map.render()










