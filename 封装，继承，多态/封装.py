"""
私有成员变量
私有成员方法
"""
"""
--------------------类对象无法访问私有成员
--------------------类中的其他成员可以访问私有成员
"""
class Phone:

    __current_voltage = 1   #  当前手机运行电压

    def __keep_single_core(self):
        print("让CPU以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g通话，并已设置为单核模式运行进行省电")

phone = Phone()
# phone.__keep_single_core()
# print(phone.__current_voltage)

phone.call_by_5g()



"""
call_by_5g          访问   __cheak_5g()私有方法
__cheak_5g私有方法    访问   __is_5g_enable私有变量
"""
class Phone1:
    __is_5g_enable = False
    def __cheak_5g(self):
        if self.__is_5g_enable :
            print("5g开启")
        else:
            print("5g关闭，使用4g网络")
    def call_by_5g(self):
        self.__cheak_5g()
        print("正在通话中")

phone1 = Phone1()
phone1.call_by_5g()

