# ============ 第十一课：数据可视化 ============
# 把第五课下载的图片大小画成柱状图

import os
import matplotlib.pyplot as plt

# ① 解决中文显示（matplotlib 默认字体不支持中文）
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]   # 用微软雅黑
plt.rcParams["axes.unicode_minus"] = False              # 负号正常显示

# ② 读取 images 文件夹里每张图片的大小（数据来源：第五课成果）
names = []
sizes = []
for f in sorted(os.listdir("images")):
    if f.endswith(".jpg"):
        names.append(f)
        sizes.append(os.path.getsize(os.path.join("images", f)))

print("读到的图片：", len(names), "张")
print("数据示例：", dict(zip(names[:3], sizes[:3])))

# ③ 画柱状图
plt.figure(figsize=(10, 5))              # 画布大小
plt.bar(names, sizes, color="red")   # 柱状图：x=文件名，y=大小
plt.grid(axis="y")
plt.title("图片下载大小（字节）")
plt.xlabel("文件名")
plt.ylabel("大小（字节）")
plt.xticks(rotation=45)                  # 文件名斜着放，避免重叠
plt.tight_layout()                       # 自动调整间距
plt.savefig("chart1.png")                # 保存成图片
print("图表已保存：chart1.png")




plt.figure()
plt.plot(names, sizes, marker="o", color="orange")   # marker="o" 画点
plt.title("图片大小趋势")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("chart2.png")

# ============ 学霸关：仓库语言分布饼图 ============
import requests
resp = requests.get("https://api.github.com/users/cairobaby/repos", timeout=20)
repos = resp.json()

langs = {}
for repo in repos:
    lang = repo["language"]
    langs[lang] = langs.get(lang, 0) + 1     # 统计每种语言数量

plt.figure()
plt.pie(langs.values(), labels=langs.keys(), autopct="%1.0f%%")   # 饼图+百分比
plt.title("我的仓库语言分布")
plt.savefig("chart3.png")
print("图表已保存：chart3.png")