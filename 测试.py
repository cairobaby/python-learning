try:
    with open("笔记.txt", "r", encoding="utf-8") as f:
        study = [line.strip() for line in f]
except FileNotFoundError:
    study = ["找工作", "写代码", "上班", "下班"]  # 默认清单

 