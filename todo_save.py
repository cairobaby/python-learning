# ===== 待办清单 · 永久保存版 =====

# ① 启动时从文件读取（程序一开就加载上次的清单）
try:
    with open("我的清单.txt", "r", encoding="utf-8") as f:
        study = [line.strip() for line in f]
except FileNotFoundError:
    study = ["找工作", "写代码", "上班", "下班"]  # 默认清单

# ② 保存函数：把清单写回文件
def save():
    with open("我的清单.txt", "w", encoding="utf-8") as f:
        for task in study:
            f.write(task + "\n")

# ③ 菜单循环
while True:
    print("===== 待办清单 =====")
    print("1.查看  2.添加  3.删除  4.退出")
    choice = input("请选择（1-4）：")

    if choice == "1":
        for i, task in enumerate(study, start=1):
            print(f"{i}. {task}")

    elif choice == "2":
        new = input("输入新待办：")
        study.append(new)
        save()                    # 保存到文件
        print(f"已添加，共 {len(study)} 条，已保存")

    elif choice == "3":
        try:
            index = int(input("要删除的编号：")) - 1
        except ValueError:
            print("请输入数字！")
            continue              # 回到菜单重新来
        if 0 <= index < len(study):
            print("已删除：", study.pop(index))
            save()                # 保存到文件
        else:
            print("编号无效")

    elif choice == "4":
        print("再见！")
        break

    else:
        print("无效选择")
