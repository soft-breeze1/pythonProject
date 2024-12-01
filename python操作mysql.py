"""
创建到mysql的数据库链接
"""
from pymysql import Connection
# 获取到mysql数据库的链接对象
conn = Connection(
    host='localhost',      # 主机名
    port=3306,             # 端口
    user='root',           # 管理员账户
    password='0000',       # 密码
    autocommit=True        # 设置自动提交
)

# print(conn.get_server_info())

"""
创建数据库中的表

# 执行非查询性质SQL
cursor = conn.cursor()       # 获取到游标对象

# 选择数据库
conn.select_db('test')

# 使用游标对象，执行sql语句
cursor.execute("create table test_pymysql2(id int);")
"""

"""
打印数据库中表的数据

cursor = conn.cursor()
conn.select_db('world')
cursor.execute("select * from student")

results = cursor.fetchall()

print(results)    # 元组
for r in results:
    print(r)
"""


cursor = conn.cursor()
conn.select_db('world')
cursor.execute("insert into student values (10002,'林俊杰',32,'男')")

# 通过commit确认
# conn.commit()

conn.close()

