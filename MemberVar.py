# Creating instance member variables in python

class Test:
    def _init_(self):
        self.a=5
    def f1(self):
        self.b=10

t1=Test()
t2=Test()
t1.f1()
t1.c=15
print(t1._dict_)
print(t2._dict_)


