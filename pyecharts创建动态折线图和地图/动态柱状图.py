# 基础柱状图
from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

bar = Bar()
"""
加入的x轴就是每个小组的名字
"""
bar.add_xaxis(["中国","美国","英国"])
"""
加入的y轴是(动态图的名字,y轴的每个小组的数据)
"""
bar.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position="right"))

# 反转xy轴
bar.reversal_axis()
bar.render("基础柱状图.html")

