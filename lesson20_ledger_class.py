# ============ 第二十课：面向对象实战——记账本重构为类 ============
# 第十七课：函数式数据库记账本 → 第二十课：类组织
# 核心：类 = 把"数据"和"操作数据的方法"装进一个盒子
# 对比函数版：8 个散落的函数 → 1 个 Ledger 类的 8 个方法

import sqlite3
import datetime
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]

class Ledger:
    """记账本类：一个对象 = 一个记账本"""

    def __init__(self, db_file="ledger.db"):
        # 构造器：连数据库 + 建表（只做一次！函数版每个函数都要 connect/close）
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            note TEXT
        )
        """)
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS budget (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            value REAL NOT NULL
        )
        """)
        self.conn.commit()

    # --- 记一笔 ---
    def add(self):
        category = input("类别（餐饮/交通/购物/其他）：")
        try:
            amount = float(input("金额："))
        except ValueError:
            print("金额必须是数字！")
            return
        note = input("备注：")
        today = datetime.date.today().strftime("%Y-%m-%d")
        self.cur.execute("INSERT INTO records (date, category, amount, note) VALUES (?, ?, ?, ?)",
                         (today, category, amount, note))
        self.conn.commit()
        print("✓ 已记录")

    # --- 查看全部 ---
    def show(self):
        self.cur.execute("SELECT id, date, category, amount, note FROM records")
        rows = self.cur.fetchall()
        if not rows:
            print("还没有记录")
            return
        total = sum(row[3] for row in rows)
        for row in rows:
            print(f"{row[0]}. {row[1]} {row[2]} ¥{row[3]} {row[4]}")
        print(f"共 {len(rows)} 笔，总金额：¥{total}")

    # --- 分类统计 + 画饼图 ---
    def stats(self):
        self.cur.execute("SELECT category, SUM(amount) FROM records GROUP BY category")
        data = self.cur.fetchall()
        for cat, total in data:
            print(f"  {cat}：¥{total}")
        labels = [d[0] for d in data]
        sizes = [d[1] for d in data]
        plt.pie(sizes, labels=labels, autopct="%1.0f%%")
        plt.title("我的消费分类")
        plt.savefig("消费饼图.png")
        print("图表已保存：消费饼图.png")

    # --- 删除 ---
    def delete(self):
        self.show()
        try:
            idx = int(input("要删除的编号："))
        except ValueError:
            print("请输入数字")
            return
        self.cur.execute("DELETE FROM records WHERE id = ?", (idx,))
        self.conn.commit()
        print(f"已删除编号 {idx}")

    # --- 设置预算 ---
    def set_budget(self):
        try:
            budget = float(input("输入你的月预算："))
        except ValueError:
            print("请输入数字")
            return
        self.cur.execute("DELETE FROM budget")
        self.cur.execute("INSERT INTO budget (value) VALUES (?)", (budget,))
        self.conn.commit()
        print(f"✓ 预算已设为 {budget} 元")

    # --- 检查预算 ---
    def check_budget(self):
        self.cur.execute("SELECT value FROM budget ORDER BY id DESC LIMIT 1")
        row = self.cur.fetchone()
        budget = row[0] if row else 1000
        self.cur.execute("SELECT SUM(amount) FROM records")
        total = self.cur.fetchone()[0] or 0
        if total > budget:
            print(f"⚠️ 超支警告！预算 {budget}，已花 {total}，超支 {total - budget}")
        else:
            print(f"✅ 预算还剩：{budget - total} 元")

    # --- 按类别查询（新方法）---
    def search_by_category(self):
        category = input("输入要查询的类别：")
        self.cur.execute("SELECT id, date, category, amount, note FROM records WHERE category = ?",
                         (category,))
        rows = self.cur.fetchall()
        if not rows:
            print(f"没有 {category} 的记录")
            return
        for row in rows:
            print(f"{row[0]}. {row[1]} {row[2]} ¥{row[3]} {row[4]}")


    # --- 关闭连接（用完要关）---
    def close(self):
        self.conn.close()

# 使用：先造一个记账本对象，然后调用它的方法
if __name__ == "__main__":
    ledger = Ledger()          # 造对象（自动连接数据库+建表）
    while True:
        print("\n--- 记账本（类版）---")
        print("1.记一笔  2.查看  3.分类统计  4.删除  5.预算检查  6.设置预算  7.退出 8.按类别查询")
        choice = input("请选择（1-8）：")
        if choice == "1":
            ledger.add()
        elif choice == "2":
            ledger.show()
        elif choice == "3":
            ledger.stats()
        elif choice == "4":
            ledger.delete()
        elif choice == "5":
            ledger.check_budget()
        elif choice == "6":
            ledger.set_budget()
        elif choice == "7":
            print("再见！")
            break
        elif choice == "8":
            ledger.search_by_category()
        else:
            print("无效选择，请重新输入")
    ledger.close()
