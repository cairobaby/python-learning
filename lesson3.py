# ============ 第三课：列表、字典和函数 ============

# ---------- 第一部分：列表 list ----------
# 列表 = 一列数据，用方括号 [ ] 装
fruits = ["苹果", "香蕉", "橙子"]
print("我的水果：", fruits)
print("第一个：", fruits[0])     # 下标从 0 开始！
fruits.append("西瓜")            # append = 在末尾添加
print("加一个后：", fruits)
print("一共有", len(fruits), "个水果")   # len = 数个数

# for 循环遍历列表
print("--- 遍历列表 ---")
for f in fruits:
    print("我喜欢", f)

# ---------- 第二部分：字典 dict ----------
# 字典 = 键值对，用花括号 { }，按"键"查"值"
me = {"名字": "cairobaby", "年龄": 30, "城市": "茂名"}
print("我的名字：", me["名字"])
me["爱好"] = "编程"              # 添加新键值
print("我的完整资料：", me)

# ---------- 第三部分：函数 def ----------
# 函数 = 把代码打包成"工具"，起个名字，随时调用
def greet(name):
    print(f"你好，{name}！欢迎来到 Python 世界。")

def add(x, y):
    return x + y                 # return = 把结果"交出来"

greet("cairobaby")
print("3 + 5 =", add(3, 5))
