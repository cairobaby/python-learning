study = ["学Python", "写代码", "推GitHub", "发博客"]

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
        print(f"已添加，共 {len(study)} 条")

    elif choice == "3":
        index = int(input("要删除的编号：")) - 1
        if 0 <= index < len(study):
            print("已删除：", study.pop(index))
        else:
            print("编号无效")

    elif choice == "4":
        print("再见！")
        break

    else:
        print("无效选择")
