__all__ = ['test_a']

def test_a(a,b):
    print(a + b)

def test_b(a,b):
    print(a - b)

# if __name__ == '__main__':
#     test(1,2)
"""
表示只有程序是直接执行的才会进入if 内部，
如果是被导入的，则if无法进入
"""


