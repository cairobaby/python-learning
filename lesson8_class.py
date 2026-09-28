# ============ 第八课：面向对象入门 ============
# 核心思想：把"东西"和"它能做的事"打包成一个类

# ① 定义"狗"类 —— 类是"图纸/模板"
class Dog:
    # __init__ 是"构造器"：创建狗时自动执行，用来存属性
    def __init__(self, name, age, eat, breed):
        self.name = name    # 属性：名字（self 指"这只狗自己"）
        self.age = age      # 属性：年龄
        self.eat = eat      # 属性：饮食习惯
        self.breed = breed  # 属性：品种

    # 方法：狗能做的事（动词）
    def bark(self):
        print(f"{self.name}：汪汪！")

    def eat(self, food):
        print(f"{self.name}在吃{food}，它最喜欢吃{self.eat}")

    def introduce(self):
        print(f"我叫{self.name}，今年{self.age}岁，我喜欢吃{self.eat}，我是{self.breed}品种的狗")

# ② 用类创建"对象"（实例）—— 按图纸造出两只真实的狗
my_dog = Dog("旺财", 3, "骨头", "金毛")
your_dog = Dog("小白", 1, "狗粮", "柯基")

# ③ 让对象做事情
my_dog.introduce()     # 调用方法：旺财自我介绍
my_dog.bark()
your_dog.introduce()
