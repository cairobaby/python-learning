import random


print("--- 猜数字游戏（1-100） ---")
secret = random.randint(1, 100)  # 随机生成一个1-100之间的整数
count = 0       
while True  :   
    guess = int(input("猜一个数字（1-10）："))
    count = count + 1
    if guess == secret:
        print(f"猜对了！太棒了！, 你一共猜了 {count} 次")
        break                 # break = 立刻结束循环
    elif guess > secret:
        print("大了！")
    else:
        print("小了！")

if count <= 7:
    print("太厉害了！")
elif count <= 12:
    print("不错哦！")
else:
    print("多练练再来挑战")




