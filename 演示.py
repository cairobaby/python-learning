# 迷你演示：三种模式的区别

# 第1步：w = 写入（把文件"清空重写"）
with open("演示.txt", "w", encoding="utf-8") as f:
    f.write("第一行内容\n")

# 第2步：a = 追加（接着末尾写，不清空）
with open("演示.txt", "a", encoding="utf-8") as f:
    f.write("第二行内容（追加的）\n")

# 第3步：r = 读取（只看内容，不能写）
with open("演示.txt", "r", encoding="utf-8") as f:
    print("--- 现在文件里是 ---")
    print(f.read())

# 第4步：再用 w 写一次，看看会发生什么
with open("演示.txt", "w", encoding="utf-8") as f:
    f.write("新的第一行（w模式重写后，之前的都没了）\n")

with open("演示.txt", "r", encoding="utf-8") as f:
    print("--- w 重写之后 ---")
    print(f.read())
