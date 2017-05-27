def fds():
    print("function")

fds()

print(fds.__call__)
print(type(fds))  # function


#Callable classes

class Caller:
    def __call__(self):
        return 30

    def regularMethod(self):
        return 40


c = Caller()
d = Caller()
print(type(c))

print(c() * c())  # 900 with __call__ defined, "caller object is not callable" without it

print(c.regularMethod())

print(callable(c)) # tests object callability


lst = [c, d]

for i in lst:
    print(i.regularMethod())
    print(i())






