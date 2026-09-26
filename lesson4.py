# ============ 第四课：文件读写 + 错误处理 ============

# ---------- 第一部分：写文件 ----------
# with open(文件名, 模式, 编码) as f:   # w = 写入（覆盖）
with open("笔记.txt", "w", encoding="utf-8") as f:
    f.write("今天学了第四课\n")
    f.write("文件读写真有用！\n")
print("① 写入完成，去看看 笔记.txt 文件")

# ---------- 第二部分：读文件 ----------
with open("笔记.txt", "r", encoding="utf-8") as f:   # r = 读取
    content = f.read()                                 # 读全部内容
print("② 文件内容：")
print(content)

# ---------- 第三部分：追加内容 ----------
with open("笔记.txt", "a", encoding="utf-8") as f:   # a = 追加（不覆盖）
    f.write("这行是追加进去的\n")

# ---------- 第四部分：错误处理 try/except ----------
# 不加保护：输入"abc" → 程序直接崩溃报错
# 加了 try/except：出错也不崩，还能给用户友好提示
try:
    num = int(input("③ 输入一个数字："))
    print("你输入的是", num)
except ValueError:
    print("这不是数字！但程序没有崩溃。")
