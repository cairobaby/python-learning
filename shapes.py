class Shape:
    def area(self):
        pass          # 父类占位，什么都不做

class Circle(Shape):          # 圆形
    def __init__(self, r):    # r = 半径
        self.r = r
    def area(self):           # 覆盖：圆的面积
        return 3.14 * self.r * self.r

class Rect(Shape):            # 长方形
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):           # 覆盖：长方形面积
        return self.w * self.h

# 统一处理
shapes = [Circle(2), Rect(3, 4), Circle(5)]
total = 0
for s in shapes:
    total += s.area()
print(f"总面积：{total}")
