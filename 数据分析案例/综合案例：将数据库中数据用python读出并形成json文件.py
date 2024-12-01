from pymysql import Connection
import json
# import datetime

conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='0000',
    autocommit=True
)
# print(conn.get_server_info())

cursor = conn.cursor()
conn.select_db('py_sql')
# cursor.execute('select country, CAST(data as char)')
cursor.execute('select * from orders')

result = cursor.fetchall()


# "date": "order_id":,"money":,"province":
record_list1 = []
record_list2 = []
for row in result:
    # print(row[0])
    # record_dict = {}
    # print(row[0].strftime('%Y-%m'))
    record_dict = {}
    record_dict["date"] = row[0].strftime('%Y-%m-%d')     #  将时间戳 换为 字符串
    record_dict["order_id"] = row[1]
    record_dict["money"] = row[2]
    record_dict["province"] = row[3]
    if row[0].strftime('%Y-%m') == '2011-01':
    # print(record_dict)
        record_list1.append(record_dict)
    else:
        record_list2.append(record_dict)

# print(record_list1)
# print(record_list2)


def write(data,path):
    for record in data:
#     print(record)
        data_json = json.dumps(record,ensure_ascii=False)

        with open(path,'a',encoding='utf-8') as f:
            f.write(data_json)
            f.write("\n")


write(record_list1,"C:/111/2011年1月及2月销售数据/2011年1月销售数据JSON版.txt")
write(record_list2,"C:/111/2011年1月及2月销售数据/2011年2月销售数据JSON版.txt")


"""
for r in record_list1:
    data_json = json.dumps(r, ensure_ascii=False)

    with open("C:/111/2011年1月及2月销售数据/2011年1月销售数据JSON版.txt",'a', encoding='utf-8') as f:
        f.write(data_json)
        f.write('\n')

for q in record_list1:
    data_json = json.dumps(q, ensure_ascii=False)

    with open("C:/111/2011年1月及2月销售数据/2011年2月销售数据JSON版.txt",'a', encoding='utf-8') as f:
        f.write(data_json)
        f.write('\n')
"""

conn.close()



