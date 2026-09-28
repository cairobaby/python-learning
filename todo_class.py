class TodoList:
    def __init__(self):
        self.tasks = []          # 属性：任务列表

    def add(self, task):         # 方法：添加
        self.tasks.append(task)

    def show(self):              # 方法：显示
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def remove(self, index):     # 方法：删除
        self.tasks.pop(index - 1)

# 用起来：
todo = TodoList()
todo.add("写代码")
todo.add("学英语")
todo.show()
todo.remove(1)
todo.show()


class SaveTodoList(TodoList):  # 继承 TodoList
    def __init__(self, filename):
        super().__init__()       # 先继承父类的属性/方法
        self.filename = filename  # 新增属性：文件名
        self.load()              # 启动时加载文件

    def load(self):              # 新增方法：从文件加载
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                self.tasks = [line.strip() for line in f]
        except FileNotFoundError:
            self.tasks = []       # 文件不存在，初始化为空列表

    def save(self):              # 新增方法：保存到文件
        with open(self.filename, "w", encoding="utf-8") as f:
            for task in self.tasks:
                f.write(task + "\n")

new_todo = SaveTodoList("我的清单.txt")
new_todo.add("写代码")
new_todo.add("学英语")
new_todo.save()  # 保存到文件
new_todo.show()

