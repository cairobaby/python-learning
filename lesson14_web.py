# ============ 第十四课：Web 开发入门（Flask） ============
# 目标：用 Python 开一个"网站"，浏览器能访问
# Flask = Python 最流行的网页框架（约 3 行就能开一个网站）

from flask import Flask
import datetime

app = Flask(__name__)     # ① 创建网站应用

# ② 路由：@app.route("/") 表示"访问网址根路径时执行下面函数"
@app.route("/")
def home():
   
    return f"<h1>你好，世界！</h1><p>这是我的第一个 Python 网站</p>"
<p><a href='/stats'>分类统计</a></p>
html += "<p><a href='/stats'>📊 分类统计</a> | <a href='/budget'>💰 预算检查</a></p>"

# 另一个路由：/about
@app.route("/about")
def about():
    return "<h1>关于我</h1><p>我正在学 Python + Flask，打算把记账本做成网页版</p>"

# ③ 动态路由：/hello/任意名字 → 名字会被传进函数
@app.route("/hello/<name>")
def hello(name):
    return f"<h1>你好，{name}！</h1>"

# 挑战A：/today 页面，显示今天日期（独立路由！）
@app.route("/today")
def today():
    today = datetime.date.today().strftime("%Y-%m-%d")
    return f"<h1>今天是 {today}</h1>"

# 挑战B：/sum/3/5 → 显示 3 + 5 = 8（动态路由传两个参数）
@app.route("/stats")
def add(a, b):
    result = int(a) + int(b)      # 网址传来的都是文字，int() 转成数字
    return f"<h1>{a} + {b} = {result}</h1>"

@app.route("/stats")
def stats():
    records = load()
    cats = {}                                    # 复习：字典累加
    for r in records:
        cats[r["类别"]] = cats.get(r["类别"], 0) + r["金额"]
    html = "<h1>分类统计</h1>"
    for cat, total in cats.items():
        html += f"<p>{cat}：¥{total}</p>"
    return html

# 挑战B：预算检查页（复用第十三课的预算逻辑）
@app.route("/budget")
def budget():
    records = load()
    total = sum(r["金额"] for r in records)
    try:
        with open("budget.txt", "r", encoding="utf-8") as f:
            b = float(f.read().strip())
    except (FileNotFoundError, ValueError):
        b = 1000
    html = "<h1>💰 预算检查</h1>"
    if total > b:
        html += f"<p style='color:red'>⚠️ 超支！预算 {b}，已花 {total}，超支 {total - b}</p>"
    else:
        html += f"<p>✅ 预算还剩：{b - total} 元</p>"
    html += "<p><a href='/'>← 返回记账本</a></p>"
    return html

# ④ 启动网站（运行后浏览器访问 http://127.0.0.1:5000/）
if __name__ == "__main__":
    app.run()
