# ============ 第九课：继承 —— 让类"生"出子类 ============

# ① 父类（基类）：狗 —— 上一课写的，直接复用
class Dog:
    def __init__(self, name, age):
        self.name = name    # 名字
        self.age = age      # 年龄

    def bark(self):
        print(f"{self.name}：汪汪！")

    def introduce(self):
        print(f"我叫{self.name}，今年{self.age}岁")

# ② 子类（派生类）：导盲犬 —— 继承 Dog 的一切
class GuideDog(Dog):                    # 括号里写父类 = 继承！
    def __init__(self, name, age, owner):
        super().__init__(name, age)     # super() = 请父类先帮忙存 name/age
        self.owner = owner              # 子类自己的新属性

    def guide(self):                    # 子类的新方法（父类没有）
        print(f"{self.name}正在引导{self.owner}过马路")

    def introduce(self):                # 覆盖（override）：同名方法重写
        print(f"我是导盲犬{self.name}，{self.age}岁，我的主人是{self.owner}")

class PoliceDog(Dog):
    def __init__(self, name, age, owner):
        super().__init__(name, age)     # super() = 请父类先帮忙存 name/age
        self.owner = owner              # 子类自己的新属性

    def patrol(self):       # 巡逻方法
        print(f"{self.name}正在巡逻，发现可疑物品！")
        
    def introduce(self):                # 覆盖（override）：同名方法重写
        print(f"我是警察犬{self.name}，{self.age}岁，我的主人是{self.owner}")

# ③ 使用
my_dog = Dog("旺财", 3)
guide = GuideDog("小亮", 2, "张阿姨")
police_dog = PoliceDog("小李", 4, "警号001")


print("--- 普通狗 ---")
my_dog.introduce()
my_dog.bark()

print("--- 导盲犬 ---")
guide.introduce()      # 用覆盖后的自我介绍
guide.bark()           # 继承来的方法：照样会叫！
guide.guide()          # 子类独有的技能

print("--- 警察犬 ---")
police_dog.introduce() # 用覆盖后的自我介绍
police_dog.bark()      # 继承来的方法：照样会叫
police_dog.patrol()    # 子类独有的技能