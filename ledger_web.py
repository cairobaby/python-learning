# ============ 第十八课：网页版记账本升级数据库版 ============
# 第十四课：JSON 文件存储 → 第十七课：SQLite 数据库
# 网页 → Python → 数据库（真实软件架构）
# 目标：表单记的每一笔直接 INSERT 进 ledger.db，查询用 SELECT

from flask import Flask, request, render_template   
import json
import os
import datetime
import sqlite3                                # ← 新：数据库模块
import pandas as pd                           # ← 新：数据分析（第二十二课）

app = Flask(__name__)
# ❌ 原写法：FILE = "records.json"   # 相对路径 = 从"程序运行目录"找文件
#   本地运行没问题，但部署到网上时运行目录和代码目录不一致 → 读不到数据
# ✅ 正确写法：用"代码文件所在目录"定位数据文件（不管在哪运行都能找到）
BASE = os.path.dirname(os.path.abspath(__file__))   # 这个 .py 文件所在的文件夹
FILE = os.path.join(BASE, "records.json")           # 旧版：JSON 数据文件（保留作对照）
DB = os.path.join(BASE, "ledger.db")                # ← 新版：数据库文件

# ① 数据层（数据库版）：连接 + 建表
def db():
    conn = sqlite3.connect(DB)               # 连接数据库（没有就自动创建）
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        category TEXT NOT NULL,
        amount REAL NOT NULL,
        note TEXT
    )
    """)
    return conn, cur

# ② 读取：SELECT 全部，转成模板要的字典列表
def load():
    conn, cur = db()
    cur.execute("SELECT id, date, category, amount, note FROM records ORDER BY id")
    rows = cur.fetchall()
    conn.close()
    return [{"id": r[0], "日期": r[1], "类别": r[2], "金额": r[3], "备注": r[4]} for r in rows]

# ❌ 旧版 JSON 的 load/save（第十四课，保留作对照）
# def load():
#     if os.path.exists(FILE):
#         with open(FILE, "r", encoding="utf-8") as f:
#             return json.load(f)
#     return []
#
# def save(records):
#     with open(FILE, "w", encoding="utf-8") as f:
#         json.dump(records, f, ensure_ascii=False, indent=2)

# ② 首页：显示表单 + 消费记录列表
@app.route("/")
def index():
    records = load()
    total = sum(r["金额"] for r in records)          # 算好要显示的数据
    return render_template("index.html", records=records, total=total)
#def index():
    # records = load()
    # 用 f-string 拼出整个网页（"字符串拼 HTML"是 Flask 之前最直观的做法）
    #html = "<h1>📒 我的记账本</h1>"
    # 表单：method='post' 表示"提交到服务器"，action='/add' 表示提交到 /add 网址
    #html += "<form method='post' action='/add'>"
    #html += "类别：<input name='category'><br>"
    #html += "金额：<input name='amount'><br>"
    #html += "备注：<input name='note'><br>"
    # html += "<button>记一笔</button>"
    # html += "</form>"# 
    # 消费记录列表
    # html += "<h2>消费记录</h2>"     ← 这行原来漏了 #，导致 IndentationError
    # total = 0
    # for i, r in enumerate(records, 1):      ← 旧字符串拼HTML代码（已废弃，全部注释）
    #     html += f"<p>{i}. {r.get('日期', '无日期')} {r['类别']} ¥{r['金额']} {r['备注']}</p>"
    #     total += r["金额"]
    # html += f"<p><b>总金额：¥{total}</b></p>"
    # html += "<p><a href='/stats'>📊 分类统计</a> | <a href='/budget'>💰 预算检查</a></p>"
    # return html

# ③ 接收表单：/add 路由，methods=["POST"] 表示"只接受网页提交过来的数据"
@app.route("/add", methods=["POST"])
def add():
    # request.form 拿到网页表单里的数据（字典）
    category = request.form["category"]
    amount = float(request.form["amount"])     # 金额转数字
    note = request.form["note"]
    # 直接 INSERT 进数据库（? 占位符防注入）
    today = datetime.date.today().strftime("%Y-%m-%d")
    conn, cur = db()
    cur.execute("INSERT INTO records (date, category, amount, note) VALUES (?, ?, ?, ?)",
                (today, category, amount, note))
    conn.commit()
    conn.close()
    return "<h1>✓ 已记录</h1><p><a href='/'>← 返回记账本</a></p>"
    # ❌ 旧版：JSON 读改写
    # records = load()
    # records.append({"日期": today, "类别": category, "金额": amount, "备注": note})
    # save(records)

# ④ 分类统计页（数据库版：GROUP BY 一行搞定）
@app.route("/stats")
def stats():
    conn, cur = db()
    cur.execute("SELECT category, SUM(amount) FROM records GROUP BY category")
    data = cur.fetchall()
    conn.close()
    cats = {cat: total for cat, total in data}    # 转成模板要的字典
    return render_template("stats.html", cats=cats)
    # ❌ 旧版：字典累加（第十四课）
    # records = load()
    # cats = {}
    # for r in records:
    #     cats[r["类别"]] = cats.get(r["类别"], 0) + r["金额"]
#@app.route("/stats")
#def stats():
   # records = load()
   # cats = {}
   # for r in records:
   #     cats[r["类别"]] = cats.get(r["类别"], 0) + r["金额"]
   # html = "<h1>📊 分类统计</h1>"
    #for cat, total in cats.items():
    #    html += f"<p>{cat}：¥{total}</p>"
   # html += "<p><a href='/'>← 返回记账本</a></p>"
    #return html
# 
#⑤ 挑战B：预算检查页（复用第十三课的预算逻辑）
# # @app.route("/budget")
# def budget():
#     records = load()
#     total = sum(r["金额"] for r in records)
#     try:
#         # ❌ 原写法：open("budget.txt")   相对路径，部署时同样找不到
#         # ✅ 正确写法：和 records.json 一样用 BASE 定位
#         with open(os.path.join(BASE, "budget.txt"), "r", encoding="utf-8") as f:
#             b = float(f.read().strip())
#     except (FileNotFoundError, ValueError):
#         b = 1000
#     html = "<h1>💰 预算检查</h1>"
#     if total > b:
#         html += f"<p style='color:red'>⚠️ 超支！预算 {b}，已花 {total}，超支 {total - b}</p>"
#     else:
#         html += f"<p>✅ 预算还剩：{b - total} 元</p>"
#     html += "<p><a href='/'>← 返回记账本</a></p>"
    # return html

# ⑤ 挑战B：预算检查页（模板版）
@app.route("/budget")
def budget():
    records = load()
    total = sum(r["金额"] for r in records)
    try:
        with open(os.path.join(BASE, "budget.txt"), "r", encoding="utf-8") as f:
            b = float(f.read().strip())
    except (FileNotFoundError, ValueError):
        b = 1000
    return render_template("budget.html", total=total, b=b)

# ⑥ 删除：点卡片上的删除链接 → 按 id 删
@app.route("/delete/<int:record_id>")
def delete(record_id):
    conn, cur = db()
    cur.execute("DELETE FROM records WHERE id = ?", (record_id,))
    conn.commit()
    conn.close()
    return "<h1>🗑️ 已删除</h1><p><a href='/'>← 返回记账本</a></p>"

# ⑦ 一次性迁移：把旧 records.json 导入 ledger.db（线上部署用，跑一次后注释掉）
@app.route("/migrate_now")
def migrate_now():
    conn, cur = db()
    cur.execute("SELECT COUNT(*) FROM records")
    count = cur.fetchone()[0]
    if count > 0:
        conn.close()
        return f"<h1>数据库已有 {count} 条记录，跳过迁移</h1>"
    n = 0
    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as f:
            records = json.load(f)
        for r in records:
            cur.execute("INSERT INTO records (date, category, amount, note) VALUES (?, ?, ?, ?)",
                        (r.get("日期", ""), r["类别"], r["金额"], r["备注"]))   # .get 防御：早期记录没有"日期"字段
            n += 1
        conn.commit()
    conn.close()
    return f"<h1>✅ 迁移完成：{n} 条记录已导入 ledger.db</h1><p><a href='/'>← 返回记账本</a></p>"


# ⑧ 数据分析页：pandas 统计 + Chart.js 图表（第二十三课）
@app.route("/report")
def report():
    conn, cur = db()
    df = pd.read_sql("SELECT * FROM records", conn)
    conn.close()
    if len(df) == 0:
        return render_template("report.html", cats={}, months={}, total=0, count=0)
    by_cat = df.groupby("category")["amount"].sum()                      # 分类统计
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")      # 字符串 → 真日期 → 纯日期（去掉时间）
    by_month = df.groupby(df["date"].dt.to_period("M"))["amount"].sum()  # 按月统计
    return render_template("report.html",
                           cats=by_cat.to_dict(),
                           months={str(k): v for k, v in by_month.to_dict().items()},
                           total=df["amount"].sum(), count=len(df),
                           records=df.to_dict("records"))   # ← 新增：明细数据（字典列表)
if __name__ == "__main__":
    app.run()
