# ============ 第十课：多态 —— 同一句话，不同表现 ============

# 父类：狗
class Dog:
    def __init__(self, name, age, food):
        self.name = name
        self.age = age
        self.food = food

    def bark(self):
        print(f"{self.name}：汪汪！")

    def introduce(self):
        print(f"我叫{self.name}，今年{self.age}岁")

    def work(self):                       # 父类默认：狗在玩耍
        print(f"{self.name}在玩耍")

    def eat(self):
        print(f"{self.name}在吃{self.food}")

# 子类1：导盲犬 —— 覆盖 work
class GuideDog(Dog):
    def __init__(self, name, age, owner, food):
        super().__init__(name, age, food)
        self.owner = owner

    def work(self):                       # 覆盖：导盲犬的工作不同
        print(f"{self.name}在引导{self.owner}过马路")
    
    def eat(self):
        print(f"{self.name}在吃{self.food}")

# 子类2：警犬 —— 覆盖 work
class PoliceDog(Dog):
    def __init__(self, name, age, police_id, food):
        super().__init__(name, age, food)
        self.police_id = police_id

    def work(self):                       # 覆盖：警犬的工作不同
        print(f"{self.name}在巡逻，警号{self.police_id}")

    def eat(self):
        print(f"{self.name}在吃{self.food}")

class SearchDog(Dog):
    def __init__(self, name, age, food):
        super().__init__(name, age, food)

    def work(self):                       # 覆盖：搜救犬的工作不同
        print(f"{self.name}正在废墟搜救")

    def eat(self):
        print(f"{self.name}在吃{self.food}")        

# ★ 多态核心：一个"通用函数"，不管什么狗传进来都能干活
def show_work(dog):
    dog.introduce()    # 它知道怎么介绍自己
    dog.work()         # 它知道自己的"工作"是什么 —— 这就是多态！
    dog.eat()          # 它知道自己吃什么
    print("---")

# 把不同类型的狗装进同一个列表
dogs = [Dog("旺财", 3, "骨头"), GuideDog("小亮", 2, "张阿姨", "营养餐"), PoliceDog("小李", 4, "001", "特供狗粮"), SearchDog("小黄", 5, "狗粮")]

for d in dogs:
    show_work(d)       # 同一个函数，处理不同的狗
