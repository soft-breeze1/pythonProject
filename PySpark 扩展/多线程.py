import time
import threading

"""
thread_obj = threading.Thread([group [, target [, name [, args [, kwargs]]]]])
- group：暂时无用，未来功能的预留参数
- target：执行的目标任务名
- args：以元组的方式给执行任务传参
- kwargs：以字典方式给执行任务传参
- name：线程名，一般不用设置


"""
def sing(msg):
    while True:      #-------------------无限循环
        print(msg)
        time.sleep(1)

def dance(msg):
    while True:
        print(msg)
        time.sleep(1)

if __name__ == '__main__':
    t1 = threading.Thread(target=sing,args = ("我要唱歌 哈哈哈...",))  # 带上逗号才是元组，不然就是括号
    t2 = threading.Thread(target=dance,kwargs={"msg":"我在跳舞哦,啦啦啦..."})
    t1.start()
    t2.start()









