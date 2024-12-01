"""
===============================$$$$$$$$$$4===============先声明函数 再 使用
"""
name = input("请输入您的姓名：")
money = 5000000
def zhucaidan():
    print("----------------主菜单----------------")
    print(f"{name},您好，欢迎来到黑马银行ATM。请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择:")
def caxunyue(show_header):
    if show_header:
        print("----------------查询余额----------------")
    print(f"{name},您好，您的余额剩余:{money}元")

def chuenkuan(num):
    global money
    money = money + num
    print("----------------存款----------------")
    print(f"{name},您好，您存款{num}元成功")
    caxunyue(False)

def qukuan(num):
    global money
    if money >= num:
        money = money - num
        print("----------------取款----------------")
        print(f"{name},您好，您取款{num}元成功")
        caxunyue(False)
    else:
        print("您的余额不足,已返回主菜单。")

while True:
    keyboard_input = zhucaidan()
    if keyboard_input == "1":
        caxunyue(True)
        continue   #   通过continue继续下一次循环
    elif keyboard_input == "2":
        num = int(input("您想要存多少钱？请输入:"))
        chuenkuan(num)
        continue
    elif keyboard_input == "3":
        num = int(input("您想要取多少钱？请输入:"))
        qukuan(num)
        continue
    else:
        print("程序退出。")
        break