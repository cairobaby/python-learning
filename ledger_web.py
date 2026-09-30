# ============ 第十四课第二讲：网页版记账本 ============
# 目标：浏览器里记账！复用第十三课的数据（records.json）
# 新知识：表单（POST）+ 接收网页数据（request.form）
# 数据层直接复用第十三课记账本的 load/save

from flask import Flask, request
import json
import os
import datetime

app = Flask(__name__)
# ❌ 原写法：FILE = "records.json"   # 相对路径 = 从"程序运行目录"找文件
#   本地运行没问题，但部署到网上时运行目录和代码目录不一致 → 读不到数据
# ✅ 正确写法：用"代码文件所在目录"定位数据文件（不管在哪运行都能找到）
BASE = os.path.dirname(os.path.abspath(__file__))   # 这个 .py 文件所在的文件夹
FILE = os.path.join(BASE, "records.json")           # 拼出完整路径

# ① 数据层：和第十三课完全一样的两个函数
def load():
    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save(records):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

# ② 首页：显示表单 + 消费记录列表
@app.route("/")
def index():
    records = load()
    # 用 f-string 拼出整个网页（"字符串拼 HTML"是 Flask 之前最直观的做法）
    html = "<h1>📒 我的记账本</h1>"
    # 表单：method='post' 表示"提交到服务器"，action='/add' 表示提交到 /add 网址
    html += "<form method='post' action='/add'>"
    html += "类别：<input name='category'><br>"
    html += "金额：<input name='amount'><br>"
    html += "备注：<input name='note'><br>"
    html += "<button>记一笔</button>"
    html += "</form>"
    # 消费记录列表
    html += "<h2>消费记录</h2>"
    total = 0
    for i, r in enumerate(records, 1):
        html += f"<p>{i}. {r.get('日期', '无日期')} {r['类别']} ¥{r['金额']} {r['备注']}</p>"
        total += r["金额"]
    html += f"<p><b>总金额：¥{total}</b></p>"
    html += "<p><a href='/stats'>📊 分类统计</a> | <a href='/budget'>💰 预算检查</a></p>"
    return html

# ③ 接收表单：/add 路由，methods=["POST"] 表示"只接受网页提交过来的数据"
@app.route("/add", methods=["POST"])
def add():
    # request.form 拿到网页表单里的数据（字典）
    category = request.form["category"]
    amount = float(request.form["amount"])     # 金额转数字
    note = request.form["note"]
    # 和第十三课一模一样的"记一笔"
    records = load()
    today = datetime.date.today().strftime("%Y-%m-%d")
    records.append({"日期": today, "类别": category, "金额": amount, "备注": note})
    save(records)
    return "<h1>✓ 已记录</h1><p><a href='/'>← 返回记账本</a></p>"

# ④ 挑战A：分类统计页（复用第十三课的字典累加套路）
@app.route("/stats")
def stats():
    records = load()
    cats = {}
    for r in records:
        cats[r["类别"]] = cats.get(r["类别"], 0) + r["金额"]
    html = "<h1>📊 分类统计</h1>"
    for cat, total in cats.items():
        html += f"<p>{cat}：¥{total}</p>"
    html += "<p><a href='/'>← 返回记账本</a></p>"
    return html

# ⑤ 挑战B：预算检查页（复用第十三课的预算逻辑）
@app.route("/budget")
def budget():
    records = load()
    total = sum(r["金额"] for r in records)
    try:
        # ❌ 原写法：open("budget.txt")   相对路径，部署时同样找不到
        # ✅ 正确写法：和 records.json 一样用 BASE 定位
        with open(os.path.join(BASE, "budget.txt"), "r", encoding="utf-8") as f:
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

if __name__ == "__main__":
    app.run()
