# ============ 第十二课：游戏开发入门（turtle 弹球）v4.0 豪华版 ============
# 功能：双球 + 闯关 + 金球 + 红球 + 暂停 + 音效 + 最高分
# 核心新知识：用"字典列表"管理多个对象（一个球 → 批量管理所有球）

import turtle
import random
import time
import winsound

# ① 创建窗口
screen = turtle.Screen()
screen.setup(600, 400)
screen.title("接球游戏")
screen.tracer(0)

# ② 挡板
paddle = turtle.Turtle()
paddle.shape("square")
paddle.shapesize(1, 5)
paddle.penup()
paddle.goto(0, -150)

# ③ 双球：用"字典列表"管理 —— 每个球有自己独立的龟、x速、y速
#    字典 = 装球的各种属性；列表 = 把所有球装在一起，循环批量处理
balls = []
for i in range(2):                    # 创建 2 个球
    b = turtle.Turtle()
    b.shape("circle")
    b.penup()
    b.goto(-50 + i * 50, 50)          # 两个球错开出生位置
    balls.append({
        "turtle": b,                  # 球本身
        "vx": 3 if i == 0 else -3,    # x 速度（方向相反，各飞一边）
        "vy": 3 + i,                  # y 速度（略有差异，轨迹不同）
    })

# ④ 红球列表（关卡越高红球越多）
reds = []

def spawn_red():
    """创建一个红球：位置必须离所有球都远，避免开局贴脸"""
    r = turtle.Turtle()
    r.shape("circle")
    r.color("red")
    r.penup()
    while True:
        x = random.randint(-260, 260)
        y = random.randint(-120, 160)
        far = True
        for b in balls:               # 检查所有球，只要有一个太近就重新随机
            if b["turtle"].distance(x, y) < 100:
                far = False
                break
        if far:
            r.goto(x, y)
            break
    reds.append({"turtle": r, "vx": random.choice([-3, 3]), "vy": random.choice([-2, 2])})

spawn_red()   # 开局 1 个红球

# ⑤ 金球（+5 分）
gold_ball = turtle.Turtle()
gold_ball.shape("circle")
gold_ball.color("gold")
gold_ball.penup()
gold_ball.goto(200, 100)

# ⑥ 键盘控制
def move_left():
    paddle.goto(paddle.xcor() - 30, paddle.ycor())

def move_right():
    paddle.goto(paddle.xcor() + 30, paddle.ycor())

paused = False
def toggle_pause():
    global paused
    paused = not paused
    if paused:
        screen.title("游戏暂停 | 按空格继续")
    else:
        screen.title(f"接球游戏 Lv{level} —— 得分：{score} | 剩余生命：{lives}")

screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(toggle_pause, "space")
screen.listen()

# ⑦ 游戏状态（循环外只初始化一次！）
score = 0
lives = 3
frame = 0
level = 1

# 最高分
try:
    with open("highscore.txt", "r", encoding="utf-8") as f:
        highscore = int(f.read().strip())
except (FileNotFoundError, ValueError):
    highscore = 0
print(f"当前最高分：{highscore}，挑战它！")
screen.title(f"接球游戏 Lv1 —— 最高分：{highscore}")

# ⑧ 扣命函数：任何球碰红球/落地都调它，代码只写一遍（DRY 原则）
def lose_life():
    global lives
    lives -= 1
    winsound.Beep(200, 200)
    if lives <= 0:
        screen.title(f"游戏结束！得分：{score}")
        return False                  # False = 命没了，游戏该结束
    # 所有球一起重生（向上飞，给玩家反应时间）
    for b in balls:
        b["turtle"].goto(0, 0)
        speed = 3 + score // 5
        b["vx"] = speed * random.choice([1, -1])
        b["vy"] = speed
    screen.title(f"接球游戏 Lv{level} —— 得分：{score} | 剩余生命：{lives}")
    return True                       # True = 还有命，继续玩

# ⑨ 主循环
game_over = False
while not game_over:
    if paused:
        screen.update()
        time.sleep(0.005)
        continue

    frame += 1

    # 所有球移动 + 撞墙/天花板反弹（一个循环处理两个球！）
    for b in balls:
        b["turtle"].goto(b["turtle"].xcor() + b["vx"], b["turtle"].ycor() + b["vy"])
        if b["turtle"].xcor() > 280 or b["turtle"].xcor() < -280:
            b["vx"] = -b["vx"]
        if b["turtle"].ycor() > 180:
            b["vy"] = -b["vy"]

    # 所有红球移动 + 反弹
    for r in reds:
        r["turtle"].goto(r["turtle"].xcor() + r["vx"], r["turtle"].ycor() + r["vy"])
        if r["turtle"].xcor() > 280 or r["turtle"].xcor() < -280:
            r["vx"] = -r["vx"]
        if r["turtle"].ycor() > 180 or r["turtle"].ycor() < -180:
            r["vy"] = -r["vy"]

    # 球碰金球 → +5 分，金球换位置
    for b in balls:
        if b["turtle"].distance(gold_ball) < 20:
            score += 5
            winsound.Beep(1500, 60)
            gold_ball.goto(random.randint(-260, 260), random.randint(-120, 160))

    # 球碰红球 → 扣命（开局 30 帧保护）
    if frame > 30:
        for b in balls:
            for r in reds:
                if b["turtle"].distance(r["turtle"]) < 20:
                    game_over = not lose_life()
                    break
            if game_over:
                break

    # 挡板接住球 → 得分 + 加速
    for b in balls:
        if b["turtle"].ycor() < -145 and abs(b["turtle"].xcor() - paddle.xcor()) < 60:
            score += 1
            speed = 3 + score // 5
            b["vx"] = speed * (1 if b["vx"] > 0 else -1)
            b["vy"] = -speed
            winsound.Beep(1000, 40)
            screen.title(f"接球游戏 Lv{level} —— 得分：{score}")

    # 球落地 → 扣命
    for b in balls:
        if b["turtle"].ycor() < -180:
            game_over = not lose_life()
            break

    # 闯关：每 20 分升一级，多一个红球（最多 3 个）
    new_level = 1 + score // 20
    if new_level > level and len(reds) < 3:
        level = new_level
        spawn_red()
        winsound.Beep(600, 300)
        screen.title(f"🎉 升到第{level}关！红球+1，注意躲避！")

    screen.update()
    time.sleep(0.005)

print(f"游戏结束，得分：{score}")
winsound.Beep(400, 400)

# 破纪录就写入新最高分
if score > highscore:
    highscore = score
    with open("highscore.txt", "w", encoding="utf-8") as f:
        f.write(str(score))
    print(f"🎉 新纪录！最高分更新为：{score}")
else:
    print(f"最高分仍是：{highscore}")

screen.bye()
