# ============ 第六课：调用 API 获取数据 ============
# 目标：用 GitHub 公开 API 查你自己的所有仓库
# 合规：这是你自己的公开数据，随便查

import requests

# GitHub 公开 API（不需要登录，返回 JSON 数据）
url = "https://api.github.com/users/cairobaby/repos"
resp = requests.get(url, timeout=20)
print("① 状态码：", resp.status_code)     # 200 = 成功

# ② .json() 把响应转成 Python 的列表（每个元素是一个仓库字典）
repos = resp.json()
print("② 你的仓库数量：", len(repos))

# ③ 遍历每个仓库，取出想要的信息
print("③ 仓库清单：")
for repo in repos:
    name = repo["name"]                  # 仓库名
    desc = repo["description"]           # 描述（可能为 None）
    lang = repo["language"]              # 主要语言
    stars = repo["stargazers_count"]     # 星标数
    private = repo["private"]            # 是否私有
    created_at = repo["created_at"]       # 创建日期（ISO 8601 格式）
    print(f"   {name} | {lang} | ⭐{stars} | {desc if desc else '（无描述）'}")
    print(f"   是否公开：{private} | 创建日期：{created_at[:10]}")

with open("repos.txt", "w", encoding="utf-8") as f:
    f.write("仓库信息\n")
    for repo in repos:
        f.write(f"{repo['name']} | {repo['language']}\n")
print("写入完成，去看看 repos.txt 文件")

python_count = 0
for repo in repos:
    if repo["language"] == "Python":
        python_count += 1
print(f"Python 仓库数量：{python_count}")