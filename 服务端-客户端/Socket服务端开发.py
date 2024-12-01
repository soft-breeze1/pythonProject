import socket

# 创建socket对象
socket_server = socket.socket()
# 绑定ip地址和端口
socket_server.bind(("127.0.0.1", 8888))
# 监听端口
socket_server.listen(1)
# listen 方法内接受一个整数型参数，表示接受的链接数量
# 等待客户端链接
"""
accept 方法返回的是二元元组(链接对象,客户端地址信息)
可以通过变量1,变量2 = socket_server.accept()的方式,
直接接受二元元组的两个元素
*******  accept 是阻塞的方法，如果没有链接，就卡在这一行不向下执行了
"""
conn, address = socket_server.accept()
print(f"接受到了客户端的链接，客户端的信息是:{address}")
"""
方法二:
result = socket_server.accept()
conn = result[0]        # 客户端和服务端的连接对象
address = result[1]     # 客户端的地址信息
"""
while True:
    # 接收客户端信息,要使用客户端和服务端的本次链接对象,而非socket_server对象
    data: str = conn.recv(1024).decode("utf-8")
    print(f"客户端发来的消息是,{data}")
    """
    recv 接受的参数是缓冲区大小，一般给1024即可
    recv 方法的返回值是一个字节数组，不是字符串，
    可以通过decode方法通过UTF-8编码，将字节数组转换为字符串对象
    """
    # 发送回复消息
    msg = input("请输入你要和客户端回复的消息: ")
    if msg == "exit":
        break
    # encode可以将字符串编码转换为字节数组对象
    conn.send(msg.encode("utf-8"))
# 关闭链接
conn.close()
socket_server.close()
# socket_server可以不关闭，用来接受下一次客户端的链接












