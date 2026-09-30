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
@app.route("/sum/<a>/<b>")
def add(a, b):
    result = int(a) + int(b)      # 网址传来的都是文字，int() 转成数字
    return f"<h1>{a} + {b} = {result}</h1>"

# ④ 启动网站（运行后浏览器访问 http://127.0.0.1:5000/）
if __name__ == "__main__":
    app.run()
