# 🐍 python-learning — cairobaby 的编程学习之旅

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-网站框架-black)
![SQLite](https://img.shields.io/badge/SQLite-数据库-003B57)
![pandas](https://img.shields.io/badge/pandas-数据分析-150458)
![Chart.js](https://img.shields.io/badge/Chart.js-可视化-FF6384)
![课程](https://img.shields.io/badge/课程-31课-success)
![状态](https://img.shields.io/badge/状态-学习中-brightgreen)

> 从零基础到独立项目：一个普通人的 Python 全栈学习记录。
> AI 陪练 + 动手实战，每课都有可运行代码。

---

## 🚀 我的在线作品

| 作品 | 网址 | 说明 |
|---|---|---|
| 📒 记账本网站 | https://cairobaby.pythonanywhere.com | 记账/筛选/统计/分析/预算/导出 CSV |

**记账本功能**：记一笔 → 按日期筛选 → 分类统计卡片 → 每月趋势柱状图 → 饼图分析 → 预算检查 → **导出 CSV（Excel 可打开）** → 内置天气查询 🌤

---

## 🛠 技术栈（学了什么）

```
Python 基础 ──→ 函数/类/继承/多态 ──→ 爬虫/API
     │
     ├─ Flask 网页 ──→ 模板/表单 ──→ 云端部署（PythonAnywhere）
     │
     ├─ SQLite 数据库 ──→ SQL 增删改查
     │
     ├─ pandas ──→ 清洗/统计/透视表/Excel 报表
     │
     └─ matplotlib + Chart.js ──→ 图表可视化
```

## 📚 学习路径（30 课全记录）

<details>
<summary>点击展开课程列表</summary>

| 阶段 | 课程 | 内容 |
|---|---|---|
| GitHub | 1 | GitHub 入门：仓库/推送/Token |
| 基础 | 2-4 | 装环境、列表/字典/函数、try/except |
| 数据 | 5-7 | 爬虫入门、API、文件读写 |
| 面向对象 | 8-10 | 类/继承/多态 |
| 可视化 | 11-12 | matplotlib 图表、turtle 游戏 |
| 存储 | 13 | JSON 数据存储 |
| 网站 | 14-16 | Flask 入门、模板表单、云端部署 |
| 数据库 | 17-18 | SQLite、数据库版记账本 |
| Git | 19 | 分支实战 |
| 重构 | 20 | 面向对象重构 |
| 数据分析 | 21-22 | pandas 入门/进阶 |
| 图表 | 23 | 网站加 Chart.js |
| 爬虫 | 24 | 天气 API 实战 |
| 笔记 | 25 | Markdown 学习笔记 |
| 综合 | 26-30 | 天气网站、合并部署、美化、筛选导出、趋势图 |

</details>

## 📁 仓库结构

```
python-learning/
├── ledger_web.py          # 记账本网站（主程序，含天气）
├── weather_web.py         # 天气网站（独立版）
├── lesson01~30_*.py       # 每课代码
├── NOTES.md               # 学习笔记
├── templates/             # 网页模板
└── static/                # CSS 样式
```

## 💡 学习心得

- **GitHub 间歇性断网不可怕**：本地 commit 永远安全，网络恢复一条 `git push` 搞定
- **先跑通再优化**：每课都先写出能跑的代码，再谈美化
- **错误是老师**：从 SyntaxError 到 500 错误，每个坑都写进笔记

## 📝 关于

本仓库是 AI 陪练式学习（豆包 + 30 课系统教学）的完整记录，从"GitHub 是什么"到"部署自己的网站"，全部实战。
