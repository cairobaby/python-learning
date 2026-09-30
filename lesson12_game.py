# ============ 第十二课：游戏开发入门（turtle 弹球） ============
# 用 Python 自带的 turtle 库做"接球游戏"：键盘←→控制挡板，接住弹球

import turtle
import random
import time       # 帧率控制：让游戏速度正常
import winsound   # 音效（Windows 内置库，无需安装）

# ① 创建窗口
screen = turtle.Screen()
screen.setup(600, 400)          # 窗口 600x400
screen.title("接球游戏")          # 标题
screen.tracer(0)                # 关闭自动刷新（手动刷新更快）

# ② 挡板（用海龟画一个扁长方形）
paddle = turtle.Turtle()
paddle.shape("square")          # 方块形状
paddle.shapesize(1, 5)          # 拉扁：宽是高的5倍
paddle.penup()                  # 移动时不画线
paddle.goto(0, -150)            # 放在底部中间

# ③ 球（圆形）
ball = turtle.Turtle()
ball.shape("circle")
ball.penup()
ball_vx = 3                     # 球的速度：x方向（单位：像素/帧）
ball_vy = 3                     # 球的速度：y方向

# 每5秒刷新一次红球的位置
red_ball = turtle.Turtle()
red_ball.shape("circle")
red_ball.color("red")
red_ball.penup()
# 红球初始位置：确保离球（0,0）至少 100 像素，避免开局"贴脸"直接结束
while True:
    red_ball.goto(random.randint(-260, 260), random.randint(-120, 160))
    if red_ball.distance(0, 0) > 100:
        break
red_ball_vx = random.choice([-3, 3])
red_ball_vy = random.choice([-2, 2])

# ④ 键盘控制：按 ← → 移动挡板
def move_left():
    paddle.goto(paddle.xcor() - 30, paddle.ycor())   # 左移30

def move_right():
    paddle.goto(paddle.xcor() + 30, paddle.ycor())   # 右移30

screen.onkey(move_left, "Left")     # 绑定左箭头
screen.onkey(move_right, "Right")   # 绑定右箭头
screen.listen()                     # 开始听键盘

# ⑤ 游戏主循环（游戏的心跳，每帧都执行）
score = 0
lives = 3                       # 学霸关：3 条命（只在循环开始前初始化一次！）
frame = 0                       # 帧计数器（开局保护用）

# 升级A：读取最高分（文件不存在或内容不对就当 0）
try:
    with open("highscore.txt", "r", encoding="utf-8") as f:
        highscore = int(f.read().strip())
except (FileNotFoundError, ValueError):
    highscore = 0
print(f"当前最高分：{highscore}，挑战它！")
while True:
    frame += 1
    ball.goto(ball.xcor() + ball_vx, ball.ycor() + ball_vy)   # 球移动

    red_ball.goto(red_ball.xcor() + red_ball_vx, red_ball.ycor() + red_ball_vy)

    if red_ball.xcor() > 280 or red_ball.xcor() < -280:
        red_ball_vx = -red_ball_vx
    if red_ball.ycor() > 180 or red_ball.ycor() < -180:
        red_ball_vy = -red_ball_vy
    
      # 碰到红球 → 扣一条命（和漏球一样），命没了才结束
    if frame > 30 and ball.distance(red_ball) < 20:
        lives -= 1                    # ① 扣一条命
        winsound.Beep(300, 150)       # 扣命音效（低沉）
        if lives <= 0:                # ② 命扣完了才结束
            screen.title(f"游戏结束！得分：{score}")
            break
        ball.goto(0, 0)               # ③ 球送回中间
        speed = 3 + score // 5        # 按当前难度等级重生
        ball_vx = speed * random.choice([1, -1])
        ball_vy = speed               # 向上飞（给玩家反应时间）
        # ⑤ 红球移到新位置（防止球重生后立刻再碰到）
        while True:
            red_ball.goto(random.randint(-260, 260), random.randint(-120, 160))
            if red_ball.distance(0, 0) > 100:
                break
        screen.title(f"接球游戏 —— 得分：{score} | 剩余生命：{lives}")


    # 撞左/右墙 → 反弹
    if ball.xcor() > 280 or ball.xcor() < -280:
        ball_vx = -ball_vx

    # 撞天花板 → 反弹
    if ball.ycor() > 180:
        ball_vy = -ball_vy

    # 挡板接住球 → 向上反弹，得分（判定线 -145，接近挡板 -150）
    if ball.ycor() < -145 and abs(ball.xcor() - paddle.xcor()) < 60:
        score += 1
        speed = 3 + score // 5                      # 升级B：难度递增，每得5分球速+1
        ball_vx = speed * (1 if ball_vx > 0 else -1)  # 保持方向，速度提升
        ball_vy = -speed                            # 向上弹，速度提升
        winsound.Beep(1000, 40)                     # 升级C：接球音效（短促高音）
        screen.title(f"接球游戏 —— 得分：{score}")

    # 球落地 → 扣一条命，命没了才结束（学霸关）
    if ball.ycor() < -180:
        lives -= 1                    # ① 扣一条命
        winsound.Beep(200, 200)       # 掉命音效（低沉拉长）
        if lives <= 0:                # ② 命扣完了才结束
            screen.title(f"游戏结束！得分：{score}")
            break
        ball.goto(0, 0)               # ③ 球送回中间
        speed = 3 + score // 5        # 按当前难度等级重生
        ball_vx = speed * random.choice([1, -1])
        ball_vy = speed               # 向上飞（关键！给玩家反应时间）
        screen.title(f"接球游戏 —— 得分：{score} | 剩余生命：{lives}")

    screen.update()   # 刷新画面（显示这一帧）——没有它窗口永远空白！
    time.sleep(0.005) # 每帧停 5 毫秒：控制游戏速度，让球看得清、来得及操作


print(f"游戏结束，得分：{score}")
winsound.Beep(400, 400)   # 结束音效

# 升级D：破纪录就写入新最高分
if score > highscore:
    with open("highscore.txt", "w", encoding="utf-8") as f:
        f.write(str(score))
    print(f"🎉 新纪录！最高分更新为：{score}")
else:
    print(f"最高分仍是：{highscore}")

screen.bye()   # 关闭游戏窗口并退出（不再卡住）


