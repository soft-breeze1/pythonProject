"""
import my_modle1
my_modle1.test(1,2)
"""

# from my_modle1 import test
# from my_modle2 import test
"""
不同模块，同名功能，后导入的会覆盖先导入的
"""
# test(1,2)

# from my_modle1 import test

"""
__all__ = ['函数名']
这时再调用 import * 就只能用这个函数了
"""
from my_modle1 import *
test_a(1,2)
# test_b(2,1)















