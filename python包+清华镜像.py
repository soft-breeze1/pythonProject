"""
import my_package.my_module1
import my_package.my_module2
my_package.my_module1.info_print1()
my_package.my_module2.info_print2()
"""
# from my_package import my_module2

"""
from my_package import my_module1
from my_package import my_module2
my_module1.info_print1()
my_module2.info_print2()
"""

"""
from my_package.my_module1 import info_print1
from my_package.my_module2 import info_print2
info_print1()
info_print2()
"""

from my_package import *
my_module1.info_print1()
# my_module2.info_print2()

"""
安装第三方包--pip
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple
用清华的镜像
"""

from my_utils.st_util import str_reverse
from my_utils.st_util import substr

print(str_reverse("黑马程序员"))
print(substr("黑马程序员", 2, 4))

from my_utils.file_util import print_file_info
from my_utils.file_util import append_to_file
print_file_info("C:/111/NEW.txt")
append_to_file("C:/111/NEW.txt",'我i的')


