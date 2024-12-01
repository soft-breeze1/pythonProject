"""
和文件相关的类定义
"""
import json

from data_define import Record

# 先定义一个抽象类用来做顶层设计，确保有哪些功能需要实现
class FileReader:

    def read_data(self) -> list[Record]:
        """
        读取文件的数据，读到的每一条数据豆转换为Record对象,将他们都封装到list内即可
        """
        pass

class TextFileReader(FileReader):

    def __init__(self,path):
        self.path = path            # 定义成员变量记录文件的路径

    # 复写(实现抽象方法)父类的方法
    def read_data(self) -> list[Record]:
        f = open(self.path,'r',encoding='utf-8')

        record_list:list[Record] = []

        for line in f.readlines():
            line = line.strip("\n")     # 消除读取到的每一行数据中的换行符\n
            # line =line.strip()        # 或者是strip()
            data_list = line.split(",")
            record = Record(data_list[0],data_list[1],int(data_list[2]),data_list[3])
            record_list.append(record)

        f.close()

        return record_list



class JsonFileReader(FileReader):

    def __init__(self,path):
        self.path = path        # 定义成员变量记录文件的路径


    def read_data(self) -> list[Record]:
        f = open(self.path, 'r', encoding='utf-8')

        record_list: list[Record] = []

        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict['date'],data_dict['order_id'],int(data_dict['money']),data_dict['province'])
            record_list.append(record)

        f.close()

        return record_list

if __name__ == '__main__':
    test_file_reader = TextFileReader("C:/111/2011年1月销售数据.txt")
    json_file_reader = JsonFileReader("C:/111/2011年2月销售数据JSON.txt")
    list1 = test_file_reader.read_data()
    list2 = json_file_reader.read_data()

#     for l in list1:
#         print(l)
#
#     for i in list2:
#         print(i)
#
# sss = ['按时,da,asf,大','萨阿丹,ffds,afa,阿松大']
# for i in sss:
#     print(i)