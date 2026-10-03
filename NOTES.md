# 🐍 Python 学习笔记（cairobaby）

> 从零基础到独立项目：24 课全记录
> 配套代码在本仓库，GitHub: https://github.com/cairobaby/python-learning

## 📚 课程总结表

> 挑战：每课用一句话写"我学到了什么"（参考已填的示例）

| 课 | 主题 | 我的总结（一句话） |
|---|---|---|
| 1 | GitHub 入门 | 代码存在 GitHub 上，改完要 add → commit → push 三步走 |
| 2 | 装 Python & VSCode | 用 .venv 虚拟环境隔离项目依赖 |
| 3 | 列表/字典/函数 | 列表用 [] 存一串，字典用 {} 存"键:值"，def 定义函数 |
| 4 | try/except 错误处理 | 可能出错的地方用 try/except 兜底，程序不崩 |
| 5 | 爬虫入门 | requests 能抓网页，编码可能乱码要用 encoding 指定 |
| 6 | 调用 API | requests.get() + .json() 就能读 GitHub 等接口数据 |
| 7 | 写文件 | with open("xx.txt", "w") 自动关闭文件 |
| 8 | 面向对象入门 | 类是图纸，对象是造出来的实物，self 指"自己" |
| 9 | 继承 | 子类(父类) 继承父类一切，super() 让父类先帮忙 |
| 10 | 多态 | 同一个函数传不同对象，各自干各自的活 |
| 11 | matplotlib 图表 | plt.plot 画折线，plt.pie 画饼图，中文要设字体 |
| 12 | turtle 游戏 | 游戏主循环 + 碰撞检测 = 游戏的心脏 |
| 13 | JSON 存储 | json.load/dump 把数据存成文件，跨程序用 |
| 14 | Flask 入门 | 路由 @app.route 让网址对应一个函数 |
| 15 | 模板与表单 | render_template + 表单把网页变成"可交互" |
| 16 | 云端部署 | PythonAnywhere 把网站放上网，手机也能访问 |
| 17 | SQLite 数据库 | 数据存数据库表，SELECT/INSERT/UPDATE/DELETE |
| 18 | 数据库版记账本 | 网页 → Python → 数据库，真实软件架构 |
| 19 | Git 分支 | 分支让开发互不干扰，改完再合并 |
| 20 | 面向对象重构 | 把记账本拆成类，代码更好维护 |
| 21 | pandas 入门 | DataFrame 是表格，筛选/排序/分组一行搞定 |
| 22 | pandas 进阶 | dropna 清洗、按月统计、透视表、导出 Excel |
| 23 | 网站加图表 | pandas 统计 + tojson 传前端 + Chart.js 画图 |
| 24 | 爬虫实战 | 爬虫 = 请求 → 响应 → 解析，JSON 嵌套逐层剥 |
| 25 | 记账本 | 杀旧服务器 → 重启 → 刷新 `/report` |
## 🔧 常用命令速查（Git）

```bash
git add 文件名     # ① 把改动放上"货架"
git commit -m "说明"  # ② 打包存进本地仓库
git push          # ③ 推到 GitHub
git status        # 查看状态
git log --oneline # 查看提交历史
```

## 🚀 我的项目清单

- [x] 记账本网站（Flask + SQLite，线上版）
- [x] 天气爬虫 + 趋势图
- [ ] （写下你的下一个项目！）

## 📝 我的坑与心得

> 把你踩过的坑记这里，以后再也不踩第二次

- （例）GitHub 经常连不上，本地提交不会丢，网络恢复再 push 就行
- Git 命令必须在仓库文件夹里执行！报 `not a git repository` = 走错文件夹了，先 `cd`
**Git 是 "就地操作" 的**：必须在仓库文件夹里跑命令。你需要在 `python-learning` 文件夹里执行。
- 
