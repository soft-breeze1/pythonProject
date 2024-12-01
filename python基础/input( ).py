print("Hello World")
name = "传智播客"
stock_prise = 19.99
stock_code = "003032"
stock_price_daily_growth_factor  = 1.2
growth_days =7
print(f"公司：{name},股票代码：{stock_code},当前股价：{stock_prise}")
print("每日增长系数是：%.1f,经过%d天的增长后，股价达到了：%.2f"%(stock_price_daily_growth_factor,growth_days,stock_prise*(stock_price_daily_growth_factor**growth_days)))
print(f"11/2的结果是：{11/2}")
"""
-------input(),无论键盘输入什么类型的数据，获取到的数据都是字符串类型
"""
print("请告诉我你是谁？")
name1 = input()
print("我知道了，你是: %s" %(name1))
# 输入数字类型
num = input("请告诉我你的银行卡密码：")
# 数据类型转换
num = int(num)
print("你的银行卡密码的类型是：%s"%type(num))
print("请输入您的用户名称")
user_name = input()
print("请输入您的用户类型")
user_type = input()
print(f"您好：{user_name},您是尊贵的：{user_type}用户，欢迎您的光临")
