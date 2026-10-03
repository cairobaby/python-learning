# ============ 第二十六课：天气爬虫网站版 ============
# 爬虫(24课) + Flask(14课) + pandas(21课) + Chart.js(23课) 全合体
from flask import Flask, request, render_template
import requests
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("weather.html", city="茂名")

@app.route("/weather")
def weather():
    city = request.args.get("city", "茂名")      # 从网址 ?city= 读城市
    url = f"https://wttr.in/{city}?format=j1"    # 爬虫：请求天气 API
    try:
        resp = requests.get(url, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
    except requests.RequestException:
        return "<h1>🌐 网络错误</h1><p><a href='/'>← 返回</a></p>"
    if resp.status_code != 200:
        return f"<h1>❓ 城市没找到：{city}</h1><p><a href='/'>← 返回</a></p>"

    data = resp.json()                           # 解析 JSON（24课技能）
    now = data["current_condition"][0]

    # pandas 整理 3 天预报（21课技能）
    rows = []
    for day in data["weather"]:
        rows.append({
            "日期": day["date"],
            "最低温": int(day["mintempC"]),
            "最高温": int(day["maxtempC"]),
            "天气": day["hourly"][4]["weatherDesc"][0]["value"],
        })
    df = pd.DataFrame(rows)

    return render_template("weather.html",
                           city=city,
                           temp=now["temp_C"], feels=now["FeelsLikeC"],
                           desc=now["weatherDesc"][0]["value"],
                           humidity=now["humidity"], wind=now["windspeedKmph"],
                           days=df.to_dict("records"),
                           dates=df["日期"].tolist(),
                           highs=df["最高温"].tolist(),
                           lows=df["最低温"].tolist())

if __name__ == "__main__":
    app.run()
