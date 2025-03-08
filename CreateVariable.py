"""class myclass:
    a=5
    def _init_(self):
        self.x=10
        y=4
        myclass.b=34
        def f1(self):
            myclass.c=65
            @staticmethod
            def f2(self):
                myclass.d=66
            @classmethod
            def f3(cls):
                cls.e=15
                myclass.f=53
myclass.g=11"""


class MyClass:
    a = 5 
    def __init__(self):
        self.x = 10
        y = 4
        MyClass.b = 34
    def f1(self):
        MyClass.c = 65 
    @staticmethod
    def f2():
        MyClass.d = 66
    @classmethod
    def f3(cls):
        cls.e = 15
        MyClass.f = 53
MyClass.g = 11
obj = MyClass()
print("Instance variable x:", obj.x)
print("Class variable a:", MyClass.a)
print("Class variable b:", MyClass.b)
obj.f1()
print("Class variable c:", MyClass.c)
MyClass.f2()
print("Class variable d:", MyClass.d)
MyClass.f3()
print("Class variable e:", MyClass.e)  
print("Class variable f:", MyClass.f)  g
print("Class variable g:", MyClass.g)  