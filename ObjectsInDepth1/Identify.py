## Basic class with init
class C:
    def __init__(self, arg1, arg2):
        self.str = arg1
        self.lst = arg2

ic = C("arun", [1, 2])

print(ic.str)


