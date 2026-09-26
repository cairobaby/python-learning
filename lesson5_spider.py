# ============ 第五课：爬虫入门 ============
# 目标：爬取你自己的网站 cairobaby.github.io

import requests
from bs4 import BeautifulSoup

# ① 用 requests 抓取网页
url = "https://cairobaby.github.io"
resp = requests.get(url)
resp.encoding = resp.apparent_encoding    # 自动检测网页编码（解决中文乱码！）
print("① 状态码：", resp.status_code)     # 200 = 请求成功

# ② 把网页源码交给 BeautifulSoup 解析（方便按标签找内容）
soup = BeautifulSoup(resp.text, "html.parser")
print("② 解析完成")

# 提取网页标题 <title> 标签里的文字
page_title = soup.find("title")
print("网页标题：", page_title.text if page_title else "未找到")

# ③ 提取主标题 <h1> 标签里的文字
title = soup.find("h1")
print("③ 网页主标题：", title.text if title else "未找到")
subtitle = soup.find("div", class_="subtitle")
print("副标题：", subtitle.text if subtitle else "未找到")
bio = soup.find("p", class_="bio")
print("简介：", bio.text if bio else "未找到")

# ④ 提取网页里的所有链接 <a> 标签
print("④ 网页里的链接：")
links = soup.find_all("a")
for link in links:
    text = link.text          # 链接显示的文字
    href = link.get("href")   # 链接指向的地址
    print("   ", text, "→", href)

with open("pz.txt", "w", encoding="utf-8") as f:
    f.write("网页里的链接\n")
    for link in links:
        href = link.get("href")
        f.write(f"{href}\n")
print("① 写入完成，去看看 pz.txt 文件")





