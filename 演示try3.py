# ===== 演示3：多个 except，分别处理不同错误 =====
try:
    x = int(input("输入被除数（比如 10）："))
    y = int(input("输入除数（比如 3）："))
    print(f"{x} ÷ {y} = {x / y}")
except ValueError:
    print("输入的不是数字！")
except ZeroDivisionError:
    print("除数不能为 0！")
