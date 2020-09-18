import math


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def r_area(abc):
        abc.area = float(int(abc.length) * int(abc.width))
        print("{:.2f}".format(abc.area))


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def c_area(abc):
        abc.area = float(math.pi * (int(abc.radius) ** 2))
        print("{:.2f}".format(abc.area))


num = int(input())
for i in range(num):
    l1 = []
    l1 = input().split()
    if l1[0] == "circle":
        obj = Circle(l1[1])
        obj.c_area()
    else:
        obj = Rectangle(l1[1], l1[2])
        obj.r_area()
