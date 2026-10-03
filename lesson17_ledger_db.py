# ============ 第十七课第3步挑战：数据库版记账本 ============
# 第十三课的 JSON 存储 → 换成 SQLite（sqlite3 内置，不用装）
import sqlite3
import datetime
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]

# ① 连接 + 建表（代替原来的 load/save 读写 JSON 文件）
def db():
    conn = sqlite3.connect("ledger.db")
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
    cur.execute("""
    CREATE TABLE IF NOT EXISTS budget (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        value REAL NOT NULL
    )
    """)
    return conn, cur

# ② 记一笔：JSON 的 records.append + save → INSERT
def add():
    category = input("类别（餐饮/交通/购物/其他）：")
    try:
        amount = float(input("金额："))
    except ValueError:
        print("金额必须是数字！")
        return
    note = input("备注：")
    today = datetime.date.today().strftime("%Y-%m-%d")
    conn, cur = db()
    cur.execute("INSERT INTO records (date, category, amount, note) VALUES (?, ?, ?, ?)",
                (today, category, amount, note))
    conn.commit()
    conn.close()
    print("✓ 已记录")

# ③ 查看：JSON 的遍历列表 → SELECT 全部（id 就是编号）
def show():
    conn, cur = db()
    cur.execute("SELECT id, date, category, amount, note FROM records")
    rows = cur.fetchall()
    conn.close()
    if not rows:
        print("还没有记录")
        return
    total = sum(row[3] for row in rows)
    for row in rows:
        print(f"{row[0]}. {row[1]} {row[2]} ¥{row[3]} {row[4]}")
    print(f"共 {len(rows)} 笔，总金额：¥{total}")

# ④ 分类统计：JSON 的字典累加 → GROUP BY 一行搞定！
def stats():
    conn, cur = db()
    cur.execute("SELECT category, SUM(amount) FROM records GROUP BY category")
    data = cur.fetchall()
    conn.close()
    for cat, total in data:
        print(f"  {cat}：¥{total}")
    labels = [d[0] for d in data]
    sizes = [d[1] for d in data]
    plt.pie(sizes, labels=labels, autopct="%1.0f%%")
    plt.title("我的消费分类")
    plt.savefig("消费饼图.png")
    print("图表已保存：消费饼图.png")

# ⑤ 删除：JSON 的 pop(编号) → 查出 id 再 DELETE WHERE id=?
def delete():
    show()
    try:
        idx = int(input("要删除的编号："))
    except ValueError:
        print("请输入数字")
        return
    conn, cur = db()
    cur.execute("DELETE FROM records WHERE id = ?", (idx,))
    conn.commit()
    conn.close()
    print(f"已删除编号 {idx}")

# ⑥ 预算：读写 budget 表（代替 budget.txt）
def set_budget():
    try:
        budget = float(input("输入你的月预算："))
    except ValueError:
        print("请输入数字")
        return
    conn, cur = db()
    cur.execute("DELETE FROM budget")            # 清空旧预算
    cur.execute("INSERT INTO budget (value) VALUES (?)", (budget,))
    conn.commit()
    conn.close()
    print(f"✓ 预算已设为 {budget} 元")

def check_budget():
    conn, cur = db()
    cur.execute("SELECT value FROM budget ORDER BY id DESC LIMIT 1")  # 取最新预算
    row = cur.fetchone()
    conn.close()
    budget = row[0] if row else 1000             # 没设置就用默认 1000
    conn, cur = db()
    cur.execute("SELECT SUM(amount) FROM records")
    total = cur.fetchone()[0] or 0
    conn.close()
    if total > budget:
        print(f"⚠️ 超支警告！预算 {budget}，已花 {total}，超支 {total - budget}")
    else:
        print(f"✅ 预算还剩：{budget - total} 元")

# ⑦ 主菜单（和第十三课一模一样）
def main():
    while True:
        print("\n--- 记账本（数据库版）---")
        print("1.记一笔  2.查看  3.分类统计  4.删除  5.预算检查  6.设置预算  7.退出")
        choice = input("请选择（1-7）：")
        if choice == "1":
            add()
        elif choice == "2":
            show()
        elif choice == "3":
            stats()
        elif choice == "4":
            delete()
        elif choice == "5":
            check_budget()
        elif choice == "6":
            set_budget()
        elif choice == "7":
            print("再见！")
            break
        else:
            print("无效选择，请重新输入")

main()
