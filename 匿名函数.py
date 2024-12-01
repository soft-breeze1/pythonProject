"""
lambda 传入参数:函数体(一行代码)
"""
def test_func(compute):
    result = compute(1,2)
    print(f"计算结果是:{result}")
def compute(x,y):
    return x+y
test_func(compute)
# ================================================
def test_func2(compute):
    result = compute(1,2)
    print(f"计算结果是:{result}")

test_func2(lambda x, y:x + y)    #  函数体(一行代码)

