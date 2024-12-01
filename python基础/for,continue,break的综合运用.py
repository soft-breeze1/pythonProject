

# ===============================循环for,continue,break的综合运用
sum_money = 10000
for i in range(1,16):
    import random
    jixiao = random.randint(1,10)

    if jixiao < 5:
        print(f"员工{i}，绩效分{jixiao},低于5，不发工资，下一位。")
# ============continue 终止本次循环，进入下一位员工的工资发放，而break是终止全部循环
        continue
    else:
        sum_money -= 1000
        if sum_money < 0:
            break
        else:
            print(f"向员工{i}发放工资1000元，账户余额还剩余{sum_money}元")
            if i == 15:
                print("所有员工工资清算完毕。")
            else:
                continue
# 19-22行代码保证了当所有员工发完工资时，不会再说下一位，保证代码的健壮性
if sum_money > 0:
    print(f"公司账户还有{sum_money}元。")
else:
    print("工资发完了，下个月领取吧。")





