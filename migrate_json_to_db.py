# ============ 一次性迁移脚本：records.json → ledger.db ============
# 在 PythonAnywhere 上运行一次：把线上旧 JSON 数据全部导入数据库
# 跑完可删，records.json 留着当备份
import sqlite3
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(BASE, "ledger.db")
FILE = os.path.join(BASE, "records.json")

# 建表（和 ledger_web.py 里一模一样）
conn = sqlite3.connect(DB)
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

# 读旧 JSON 数据
with open(FILE, "r", encoding="utf-8") as f:
    records = json.load(f)

# 逐条 INSERT 进数据库
for r in records:
    cur.execute("INSERT INTO records (date, category, amount, note) VALUES (?, ?, ?, ?)",
                (r["日期"], r["类别"], r["金额"], r["备注"]))

conn.commit()
conn.close()
print(f"✅ 迁移完成：{len(records)} 条记录已导入 ledger.db")
