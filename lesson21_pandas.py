# ============ 第二十一课：pandas 数据分析入门 ============
# 用你自己的记账本数据学习 pandas
# 对照：第10课字典累加 / 第17课 SQL / 第21课 pandas（一行顶一遍）
import pandas as pd
import sqlite3

# ① 从数据库读出数据 → DataFrame（带行列的表格）
conn = sqlite3.connect("ledger.db")
df = pd.read_sql("SELECT * FROM records", conn)
conn.close()

# ② 看看这个"表"
print("=== 前3行 ===")
print(df.head(3))          # 只看前 3 行（数据多时不用全看）

print("\n=== 表格形状（行, 列）===")
print(df.shape)

print("\n=== 列名 ===")
print(df.columns.tolist())

# ③ 每列的类型
print("\n=== 每列类型 ===")
print(df.dtypes)

# ④ 筛选：金额 > 15 的记录（对比 SQL 的 WHERE）
print("\n=== 金额 > 15 的记录 ===")
print(df[df["amount"] > 15])

# ⑤ 排序：按金额从高到低（对比 SQL 的 ORDER BY）
print("\n=== 按金额从高到低 ===")
print(df.sort_values("amount", ascending=False))

# ⑥ 分组统计：每个类别花了多少钱（对比 SQL 的 GROUP BY）
print("\n=== 分类统计（pandas 版）===")
print(df.groupby("category")["amount"].sum())

# ⑦ 一键统计：金额的所有指标
print("\n=== 金额的描述统计 ===")
print(df["amount"].describe())
