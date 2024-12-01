"""
打开文件
读写文件
关闭文件
"""

"""
open(name,mode,encoding)
"""
# f = open('python.txt','r',encoding='utf-8')
"""
r:只读
w:只写
a:追加
"""
# open('C:\111','r',encoding = 'utf-8')
"""
文件对象.read(num)
"""
"""
文件对象.readlines()
"""
# open("C:/111/111.txt","r",encoding = "utf-8")
f = open("C:/111/111.txt","r",encoding = "utf-8")
# A = f.read()
# print(A)
content = f.readlines()
print(f"content对象的类型是:{type(content)}")
print(content)
f.close()
"""
指针
A = f.read(2)
A = f.read(3)
A 会在先读完两个字后，继续读后续的3个字。
在read()后，全部内容都会被读完，再readlines()就显示没有内容了,即[] 
"""
"""
readline()
只读取一行
"""
f = open("C:/111/111.txt","r",encoding = "utf-8")
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(line1)
print(line2)
print(line3)

# for 循环遍历文件
for line in f:
    print(f"每一行数据是:{line}")

f.close()
"""
time.sleep(5)    
5为程序持续运行时间
"""
"""
with open()   
通过with open()语法打开文件，可以自动关闭
"""
with open("C:/111/111.txt","r",encoding = "utf-8") as f:
    for line in f:
        print(f"每一行数据是:{line}")
# with open() 自动将文件关闭了
# time.sleep(500000)

with open("C:/111/word.txt",encoding = "utf-8") as F:
    count = 0
    for line in F:
        line = line.strip()
        print(line)
        words = line.split(' ')
        print(words)
        for word in words:
            if word == 'itheima':
                count += 1
    print(count)

"""
f = open("C:/111/word.txt",encoding = "utf-8")
content = f.read()
count = content.count('itheima')
print(count)
"""

"""
文件写入
f.write('Hello world')
内容刷新，                 =============    {刷新内容到硬盘中}
f.flush()
"""
# import time
b = open("C:/111/qqq.txt",'w',encoding = "utf-8")
b.write("Hello world")
#----------------flush() 刷新
b.flush()
#----------------close() 自带flush功能
b.close()
# time.sleep(600000)

"""
w 模式，文件不存在，会创建新文件
w 模式，文件存在，会清空原有内容
close() 自带flush功能
"""

f = open("C:/111/jjj.txt",'a',encoding = "utf-8")
f.write("\n学python最佳选择")
f.close()

fr = open("C:/111/bill.txt",'r',encoding = "utf-8")
fw = open("C:/111/mmm.txt",'w',encoding = "utf-8")
for line in fr:
    line = line.strip()
    if line.split(',')[-1] == '测试':
        continue
    fw.write(line)
    fw.write('\n')
"""
由于前面对内容进行了strip()的操作，所以要手动的写出换行符
"""
fr.close()
fw.close()