# ============ 第二十四课：爬虫实战——天气数据抓取 ============
# 目标：用 requests 抓真实天气 API（wttr.in，免费、支持中文城市、返回 JSON）
# 新知识：JSON 嵌套解析（字典套字典/列表）+ 防御式爬取
import requests

# ① 输入城市
city = input("输入城市（如：茂名/北京/上海/广州）：")

# ② 请求天气 API：?format=j1 表示"返回 JSON 格式"
url = f"https://wttr.in/{city}?format=j1"
try:
    resp = requests.get(url, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
except requests.RequestException:
    print("网络错误，抓取失败")
    exit()

# ③ 防御式检查：状态码不对就不继续
if resp.status_code != 200:
    print(f"抓取失败，状态码 {resp.status_code}")
    exit()

# ④ 解析 JSON：整个响应是"大字典"
data = resp.json()
now = data["current_condition"][0]     # 当前天气在列表的第一个元素里

print(f"\n📍 {city} 当前天气")
print(f"温度：{now['temp_C']}°C（体感 {now['FeelsLikeC']}°C）")
print(f"天气：{now['weatherDesc'][0]['value']}")   # 天气描述藏在"列表套字典"里
print(f"湿度：{now['humidity']}%   风速：{now['windspeedKmph']}km/h")

# ⑤ 未来几天预报（weather 是列表，每个元素是一天）
print("\n📅 未来预报")
for day in data["weather"]:
    date = day["date"]
    max_t = day["maxtempC"]           # 最高温
    min_t = day["mintempC"]           # 最低温
    desc = day["hourly"][4]["weatherDesc"][0]["value"]   # 中午时段的天气
    print(f"{date}：{min_t}°C ~ {max_t}°C，{desc}")
