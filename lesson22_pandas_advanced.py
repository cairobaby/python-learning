# ============ 第二十二课：pandas 进阶——数据清洗与报表 ============
import pandas as pd
import sqlite3

conn = sqlite3.connect("ledger.db")
df = pd.read_sql("SELECT * FROM records", conn)
conn.close()

# ========== 第一部分：真实数据分析 ==========
print("========== 你的记账本数据 ==========")
print(f"共 {len(df)} 条记录")

# ① 检查空值：isnull() 找空，sum() 数数量
print("\n=== 空值统计（0 = 没有缺失）===")
print(df.isnull().sum())

# ② 检查重复行
print("\n=== 重复行数量（0 = 没有重复）===")
print(df.duplicated().sum())

# ③ 日期处理：字符串 "2026-10-03" → 真正的日期类型
df["date"] = pd.to_datetime(df["date"])
print("\n=== date 列类型（现在是 datetime64）===")
print(df.dtypes)

# ④ 按月份统计：to_period("M") 把日期归到"月"
df["月份"] = df["date"].dt.to_period("M")
print("\n=== 每月消费 ===")
print(df.groupby("月份")["amount"].sum())

# ⑤ 导出 Excel 报表
df.to_excel("消费报表.xlsx", index=False)
print("\n✅ 已导出 消费报表.xlsx（用 Excel 打开看看！）")

# ========== 第二部分：数据清洗演练（不碰真实数据） ==========
print("\n========== 数据清洗演练 ==========")
# 模拟一份"脏数据"：有缺金额的、有重复的
dirty = pd.DataFrame({
    "date": ["2026-10-01", "2026-10-02", "2026-10-01", None],
    "category": ["餐饮", "交通", "餐饮", "购物"],
    "amount": [15.5, 8.0, 15.5, None],     # 重复行 + 两个空值
})
print("=== 脏数据 ===")
print(dirty)

# ⑥ 删除有空值的行：dropna()
clean1 = dirty.dropna()
print("\n=== dropna() 删掉空值行后 ===")
print(clean1)

# ⑦ 删除重复行（保留第一条）
clean2 = clean1.drop_duplicates()
print("\n=== drop_duplicates() 删掉重复后 ===")
print(clean2)

# ⑧ 另一种处理：空值填默认值 fillna()（比如金额空就填 0）
filled = dirty.fillna({"amount": 0, "date": "未知日期"})
print("\n=== fillna() 用默认值填空 ===")
print(filled)
