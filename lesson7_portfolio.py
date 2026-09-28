# ============ 第七课：用 Python 生成网页 ============
# 目标：把 GitHub 仓库数据变成一份"作品集"网页
# 原理：Python 拼出 HTML 字符串 → 保存成 .html 文件 → 浏览器打开

import requests

# ① 用第六课的知识拿到你的仓库数据
url = "https://api.github.com/users/cairobaby/repos"
resp = requests.get(url, timeout=20)
repos = resp.json()

# ② 拼 HTML：三引号字符串可以写多行
html = """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>我的 Python 作品集</title>
  <style>
    body { font-family: 微软雅黑; background: #f5f5f5; padding: 30px; }
    h1 { color: #2c3e50; }
    li { margin: 8px 0; font-size: 18px; }
  </style>
</head>
<body>
  <h1>我的 Python 作品集</h1>
  <p>这些仓库是我学习编程的成果：</p>
  <ul>
"""
for repo in repos:
    name = repo["name"]
    lang = repo["language"]
    html_url = repo["html_url"]
    html += f'    <li><a href="{html_url}">{name}（{lang}）</a></li>\n'

html += """  </ul>
</body>
</html>
"""

# ③ 保存成网页文件
with open(r"C:\Users\19761\Documents\cairobaby.github.io\portfolio.html", "w", encoding="utf-8") as f:
    f.write(html)
