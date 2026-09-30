# ============ 第十三课：毕业项目——记账本 ============
# 串联全部知识：列表/字典 + 文件 + 函数 + 循环 + 异常处理 + JSON
# 数据存成 JSON 文件（Python 数据 ↔ 文件的桥梁）

import json
import os
import datetime


FILE = "records.json"          # 数据文件

# ① 加载数据（文件不存在就返回空列表）
def load():
    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# ② 保存数据（json.dump 把列表/字典直接写进文件）
def save(records):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

# ③ 记一笔
def add(records):
    category = input("类别（餐饮/交通/购物/其他）：")
    try:
        amount = float(input("金额："))     # 防输入错误：不是数字就报错
    except ValueError:
        print("金额必须是数字！")
        return
    note = input("备注：")
    today = datetime.date.today().strftime("%Y-%m-%d")   # 2026-09-30
    records.append({"日期": today, "类别": category, "金额": amount, "备注": note})
    save(records)
    print("✓ 已记录")

# ④ 查看所有（顺便算总额）
def show(records):
    if not records:
        print("还没有记录")
        return
    total = 0
    for i, r in enumerate(records, 1):
        print(f"{i}. {r.get('日期', '无日期')} {r['类别']} ¥{r['金额']} {r['备注']}")
        total += r["金额"]
    print(f"共 {len(records)} 笔，总金额：¥{total}")

# ⑤c 设置预算（存到单独的文件）
def set_budget():
    try:
        budget = float(input("输入你的月预算："))
    except ValueError:
        print("请输入数字")
        return
    with open("budget.txt", "w", encoding="utf-8") as f:
        f.write(str(budget))
    print(f"✓ 预算已设为 {budget} 元")

# ⑤ 预算检查（新函数）
def check_budget(records):
    try:
        with open("budget.txt", "r", encoding="utf-8") as f:
            budget = float(f.read().strip())
    except (FileNotFoundError, ValueError):
        budget = 1000     # 没设置过就用默认 1000
    total = sum(r["金额"] for r in records)     # 算总额
    if total > budget:
        print(f"⚠️ 超支警告！预算 {budget}，已花 {total}，超支 {total - budget}")
    else:
        print(f"✅ 预算还剩：{budget - total} 元")



# ⑤ 分类统计（字典累加：cats[类别] += 金额）
def stats(records):
    cats = {}
    for r in records:
        cat = r["类别"]
        cats[cat] = cats.get(cat, 0) + r["金额"]
    for cat, total in cats.items():
        print(f"  {cat}：¥{total}")

# ⑥ 删除
def delete(records):
    show(records)
    try:
        idx = int(input("要删除的编号：")) - 1
        if 0 <= idx < len(records):
            removed = records.pop(idx)
            save(records)
            print(f"已删除：{removed['类别']} ¥{removed['金额']}")
        else:
            print("编号无效")
    except ValueError:
        print("请输入数字")

# ⑦ 主菜单（while True 循环 + 分支，从第一课就会的套路）
def main():
    records = load()
    while True:
        print("\n--- 记账本 ---")
        print("1.记一笔  2.查看  3.分类统计  4.删除  5.预算检查  6.设置预算  7.退出")
        choice = input("请选择（1-7）：")
        if choice == "1":
            add(records)
        elif choice == "2":
            show(records)
        elif choice == "3":
            stats(records)
        elif choice == "4":
            delete(records)
        elif choice == "5":
            check_budget(records)
        elif choice == "6":
            set_budget()
        elif choice == "7":
            print("再见！")
            break
        else:
            print("无效选择，请重新输入")

main()
