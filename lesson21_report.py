# ============ 挑战：消费分析报告（pandas 版） ============
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]

conn = sqlite3.connect("ledger.db")
df = pd.read_sql("SELECT * FROM records", conn)
conn.close()

print("=== 你的消费分析报告 ===")
print(f"总支出：¥{df['amount'].sum()}")
print(f"共 {len(df)} 笔，平均每笔 ¥{df['amount'].mean():.2f}")
print(f"最大一笔：¥{df['amount'].max()}（{df.loc[df['amount'].idxmax(), 'note']}）")

print("\n=== 每类消费占比 ===")
by_cat = df.groupby("category")["amount"].sum()
print(by_cat)
print(f"\n占比：\n{(by_cat / by_cat.sum() * 100).round(1)}%")

# 饼图（pandas 自带绘图）
by_cat.plot.pie(autopct="%1.0f%%")
plt.title("消费占比")
plt.savefig("消费饼图_pandas.png")
print("\n饼图已保存：消费饼图_pandas.png")
