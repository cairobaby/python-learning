# ============ 第二课：让程序会"思考"和"重复" ============

# ---------- 第一部分：条件判断 if ----------
# 比较符号：> 大于  < 小于  >= 大于等于  <= 小于等于  == 等于  != 不等于
age = int(input("你今年几岁："))

if age >= 18:
    print("你成年了！可以自己创建 GitHub 账号。")
elif age >= 12:
    print("你是青少年，学编程正是好时候！")
else:
    print("你还小，但学编程不分年龄！")

# ---------- 第二部分：for 循环（重复固定次数） ----------
print("--- 循环开始：重复5次 ---")
for i in range(1, 6):        # range(1,6) = 1,2,3,4,5
    print("第", i, "次：Python 真好玩！")

# ---------- 第三部分：while 循环 + 猜数字 ----------
print("--- 猜数字游戏（1-10），只有3次机会 ---")
secret = 7
count = 0
while count < 3:
    guess = int(input("猜一个数字（1-10）："))
    count = count + 1
    if guess == secret:
        print("猜对了！太棒了！")
        break                 # break = 立刻结束循环
    elif guess > secret:
        print("大了！")
    else:
        print("小了！")

if count == 3 and guess != secret:
    print("机会用完了，答案是 7。")
