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