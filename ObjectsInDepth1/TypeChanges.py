#Added something
class Square:
    def __init__(self, d):
        self.d = d

    def square(self):
        return self.d * self.d


class Cube:
    def __init__(self, d):
        self.d = d

    def cube(self):
        return self.d * self.d * self.d


sq = Square(4)
print(type(sq))  # square
print(sq.square())  # 16

sq.__class__ = Cube

print(type(sq))  # cube
print(sq.cube())  # 64

# What happens if the arguments have different names?

# class Cube2:
#     def __init__(self, e):
#         self.e = e
#
#     def cube(self):
#         return self.e * self.e * self.e
#
# sq.__class__ = Cube2  # works
#
# print(type(sq))  # cube works
# print(sq.cube())  # "Cube object has no attribute e"


# What happens if attribute is a different type?
class Cube3:
    def __init__(self, d):
        self.d = d

    def cube(self):
        self.d.append(4)
        return self.d

cu = Cube3([4, 5])

print(cu.cube()) # works fine

sq.__class__ = Cube3
print(type(sq))  # cube3
print(sq.cube())  #int object has no attribute append





# What happens if the arguments aren't the same?

# class Rectangle:
#     def __init__(self, d, height):
#         self.d = d
#         self.height = height
#
#     def area(self):
#         return self.d * self.height
#
#
# rect = Rectangle(5, 10)
#
# print(rect.area())
#
# sq.__class__ = Rectangle # legal
#
# print(type(sq))
#
# print(sq.area())  # not legal