import requests
import json
import matplotlib.pyplot as plt
from flask import Flask, send_file
import json


plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]   # 中文字体（第11课）
plt.rcParams["axes.unicode_minus"] = False              # 负号正常显示

url = "https://api.github.com/users/cairobaby/repos"
resp = requests.get(url, timeout=20)
repos = resp.json()

print(f"你的仓库数量：{len(repos)}")
for repo in repos:
    print(f"  {repo['name']} | {repo['language']} | ⭐{repo['stargazers_count']}")

# ============ 第2步：存JSON + 统计语言分布（复习第13课+第10课） ============
import json

# ① 把仓库数据存成 JSON 文件（第13课知识：json.dump）
with open("repos_data.json", "w", encoding="utf-8") as f:
    json.dump(repos, f, ensure_ascii=False, indent=2)
print(f"\n✅ 已保存 {len(repos)} 个仓库到 repos_data.json")

# ② 统计语言分布（第10课知识：字典累加）
langs = {}
for repo in repos:
    lang = repo["language"]     # 可能为 None（没写语言）
    langs[lang] = langs.get(lang, 0) + 1   # 累加：没有就0，有就+1

print("📊 语言分布：")
for lang, count in langs.items():
    print(f"  {lang}：{count} 个仓库")

# ============ 第3步：画语言分布饼图（复习第11课） ============

# 语言为 None 的仓库显示为"未标记"（你可能有仓库没填语言）
labels = [str(l) if l else "未标记" for l in langs.keys()]
values = list(langs.values())

plt.figure(figsize=(6, 6))
plt.pie(values, labels=labels, autopct="%1.0f%%")       # 饼图+百分比
plt.title("我的 GitHub 仓库语言分布")
plt.savefig("dashboard_chart.png", dpi=150)             # 存成图片文件
print("✅ 饼图已保存：dashboard_chart.png，去看一眼")

app = Flask(__name__)

@app.route("/")
def dashboard():
    # 读第2步存的 JSON 数据
    with open("repos_data.json", "r", encoding="utf-8") as f:
        repos = json.load(f)
    # 统计语言分布（第10课字典累加）
    langs = {}
    for repo in repos:
        lang = repo["language"]
        langs[lang] = langs.get(lang, 0) + 1
    # 拼网页（第14课）
    html = "<h1>📊 我的 GitHub 数据仪表盘</h1>"
    html += f"<p>共 <b>{len(repos)}</b> 个仓库</p>"
    html += "<h2>🌐 语言分布</h2>"
    for lang, count in langs.items():
        html += f"<p>{lang if lang else '未标记'}：{count} 个</p>"
    html += "<h2>📈 饼图</h2>"
    html += "<img src='/chart' width='420'>"
    return html

@app.route("/chart")
def chart():
    return send_file("dashboard_chart.png")   # 新知识：把图片文件发给浏览器

if __name__ == "__main__":
    app.run()