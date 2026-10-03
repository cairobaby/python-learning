import requests
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]

city = input("输入城市：")
url = f"https://wttr.in/{city}?format=j1"
resp = requests.get(url, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
data = resp.json()

# ① 把爬到的天气整理成 DataFrame（一行一天）
rows = []
for day in data["weather"]:
    rows.append({
        "日期": day["date"],
        "最高温": int(day["maxtempC"]),
        "最低温": int(day["mintempC"]),
        "天气": day["hourly"][4]["weatherDesc"][0]["value"],
    })
df = pd.DataFrame(rows)
print("=== 未来天气（pandas 表格）===")
print(df)

# ② 画折线图：最高/最低温趋势
plt.plot(df["日期"], df["最高温"], marker="o", label="最高温")
plt.plot(df["日期"], df["最低温"], marker="o", label="最低温")
plt.xlabel("日期")
plt.ylabel("温度(°C)")
plt.title(f"{city} 未来天气趋势")
plt.legend()
plt.savefig(f"天气趋势_{city}.png")
print(f"\n✅ 图表已保存：天气趋势_{city}.png")