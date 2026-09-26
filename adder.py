
while True:
    try:
        a = int(input("输入第一个数字："))
        b = int(input("输入第二个数字："))
        print(f"{a} + {b} = {a + b}")
        break
    except ValueError:
        print("输入的不是数字！")