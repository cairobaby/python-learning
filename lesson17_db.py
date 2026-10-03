# ============ 第十七课：数据库入门（SQLite） ============
import sqlite3

# ① 连接数据库（文件不存在就自动创建 ledger.db）
conn = sqlite3.connect("ledger.db")
cur = conn.cursor()    # cursor = 数据库的"手"，用它执行命令

# ② 建表：IF NOT EXISTS = "没有才建"（重复运行不报错）
cur.execute("""
CREATE TABLE IF NOT EXISTS records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,   -- 自动编号
    date TEXT NOT NULL,                     -- 日期（文本）
    category TEXT NOT NULL,                 -- 类别
    amount REAL NOT NULL,                   -- 金额（小数）
    note TEXT                               -- 备注
)
""")

# ③ 插入两条记录：? 是占位符（防注入的安全写法）
cur.execute("INSERT INTO records (date, category, amount, note) VALUES (?, ?, ?, ?)",
            ("2026-10-01", "餐饮", 15.5, "午饭"))
cur.execute("INSERT INTO records (date, category, amount, note) VALUES (?, ?, ?, ?)",
            ("2026-10-02", "交通", 8.0, "打车"))

# ④ 查询：SELECT * = 全选；fetchall() = 拿回所有行
cur.execute("SELECT * FROM records")
rows = cur.fetchall()
for row in rows:
    print(row)          # 每行是一个元组 (id, date, category, amount, note)

# ⑤ 保存（commit）并关闭——重要！
conn.commit()
conn.close()

# ============ 第2步：查询增强（WHERE + 统计 + 删除） ============
import sqlite3
conn = sqlite3.connect("ledger.db")
cur = conn.cursor()

# ① WHERE 筛选：只查"餐饮"类（=? 还是占位符）
cur.execute("SELECT * FROM records WHERE category = ?", ("餐饮",))
print("--- 餐饮的记录 ---")
for row in cur.fetchall():
    print(row)

# ② 聚合函数：SUM 算总和（fetchone 拿一行）
cur.execute("SELECT SUM(amount) FROM records")
total = cur.fetchone()[0]
print(f"总金额：¥{total}")

# ③ GROUP BY 分组统计 = 第10课"字典累加"的数据库版！
cur.execute("SELECT category, SUM(amount) FROM records GROUP BY category")
print("--- 分类统计 ---")
for cat, amount in cur.fetchall():
    print(f"{cat}：¥{amount}")

# ④ DELETE 删除：WHERE 指定删哪条
cur.execute("DELETE FROM records WHERE note = ?", ("打车",))
print("已删除备注为'打车'的记录")

conn.commit()
conn.close()
