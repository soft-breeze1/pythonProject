from file_define import FileReader,TextFileReader,JsonFileReader
from data_define import Record
from pymysql import Connection


test_file_reader = TextFileReader("C:/111/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("C:/111/2011年2月销售数据JSON.txt")

jan_data:list[Record] = test_file_reader.read_data()
fed_data:list[Record] = json_file_reader.read_data()
# 将2个月份的数据合并为1个list来存储
all_data:list[Record] = jan_data + fed_data

# 构建mysql链接对象
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='0000',
    autocommit=True
)
# 获取游标对象
cursor = conn.cursor()

# 选择数据库
conn.select_db("py_sql")

# 组织sql语句
for record in all_data:
    sql = (f"insert into orders(order_date,order_id,money,province) " 
           f"values('{record.date}','{record.order_id}','{record.money}','{record.province}')")
    # print(sql)
# 执行sql语句
    cursor.execute(sql)

# 关闭mysql链接对象
conn.close()














