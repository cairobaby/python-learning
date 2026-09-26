# ===== 演示2：有 try/except → 程序不崩 =====
print("--- 演示2：有保护 ---")
try:
    num = int(input("输入一个数字："))
    print("你输入了", num)
except ValueError:
    print("这不是数字！但程序继续运行。")

print("这句话依然能执行 → 程序没崩")
