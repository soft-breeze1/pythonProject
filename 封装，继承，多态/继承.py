# 演示单继承
class Phone:
    IMEI = None             #序列号
    producer = 'ITCAST'     #厂商
    
    
    def call_by_4g(self):
        print("4g通话")

class Phone2022(Phone):
    face_id  ='10001'   # 面部识别id

    def call_by_5g(self):
        print("2022年新功能，5g通话")

# phone = Phone2022()
# print(phone.producer)
# phone.call_by_4g()
# phone.call_by_5g()

# 演示多继承
class NFCReader:
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")

class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启了")

class MyPhone(Phone, NFCReader,RemoteControl):
    # 左边继承的优先级最高
    pass     #  空内容， 可以用 pass 关键字


phone = MyPhone()
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control()

print(phone.producer)



"""
复写父类属性
复写父类方法
"""
class Phone1:
    IMEI = None            # 序列号
    producer = 'ITCAST'     # 厂商

    def call_by_5g(self):
        print("使用5g网络进行通话")

class MyPhone1(Phone1):
    producer = 'ITHEIMA'         # 复写父类属性

    def call_by_5g(self):
        print("开启CPU单核模式，确保通话的时候省电")
        # print("使用5g网络进行通话")
        """
        方式1
        print(f"父类的厂商是:{Phone1.producer}")
        Phone1.call_by_5g(self)    ********************括号里要加 self 指针
        """
        """
        方式2
        print(f"父类的厂商是:{super().producer}")
        super().call_by_5g()
        """
        print("关闭CPU单核模式，确保性能")

phone1 = MyPhone1()
phone1.call_by_5g()
print(phone1.producer)

"""
调用父类成员       super()
"""

