# ============ 挑战：月度消费报告（Excel 多表 + 透视表） ============
import pandas as pd
import sqlite3

conn = sqlite3.connect("ledger.db")
df = pd.read_sql("SELECT * FROM records", conn)
conn.close()
df["date"] = pd.to_datetime(df["date"])
df["月份"] = df["date"].dt.to_period("M")

# 透视表：行=月份，列=类别，值=金额（Excel 的招牌功能！）
pivot = df.pivot_table(values="amount", index="月份",
                       columns="category", aggfunc="sum", fill_value=0)
print("=== 每月各类别消费矩阵 ===")
print(pivot)
