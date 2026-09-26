# ============ 第五课进阶：下载图片（稳健版） ============
# 图片来源：picsum.photos（专供测试的免费图片服务）
# 稳健版：下载前校验状态码和文件大小，防止存垃圾文件

import requests
import os

os.makedirs("images", exist_ok=True)      # 创建 images 文件夹（已存在也不报错）

print("开始批量下载 10 张随机图片：")
for i in range(1, 11): # 下载 10 张图片
    # 不带 id= 的地址返回随机图片（必定存在）；?random= 保证每次不同
    img_url = f"https://picsum.photos/300/200?random={i}"
    try:
        resp = requests.get(img_url, timeout=20)      # timeout 防止卡死
    except requests.RequestException:                  # 网络错误（断网/超时）
        print(f"images/风景{i}.jpg：网络错误，跳过")
        continue

    if resp.status_code == 200 and len(resp.content) > 5000:
        with open(f"images/风景{i}.jpg", "wb") as f:
            f.write(resp.content)
        print(f"   风景{i}.jpg 已下载（{len(resp.content)} 字节）")
    else:
        print(f"   风景{i}.jpg：异常，跳过（状态码{resp.status_code}，大小{len(resp.content)}）")

print("全部完成！去 images 文件夹看看")


downloaded = []
for i in range(1, 11):
    filename = f"images/风景{i}.jpg"
    if os.path.exists(filename):
        size = os.path.getsize(filename)
        downloaded.append((filename, size))

total_size = sum(size for _, size in downloaded)
count = len(downloaded)
average_size = total_size / count if count else 0
print(f"下载统计：共 {count} 张，总大小 {total_size / 1024:.2f} KB，平均大小 {average_size / 1024:.2f} KB")

with open("download_log.txt", "w", encoding="utf-8") as f:
    for filename, size in downloaded:
        f.write(f"{filename}：{size} 字节\n")
print("① 写入完成，去看看 download_log.txt 文件")


