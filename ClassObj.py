class Test:
    x=20
    def __init__(self,a,b):
        self.a=a
        self.b=b 
    def show(self):
            print(self.a,self.b)
            print(Test.x)
t1=Test(4,5)
t1.show()
print(t1.a)
print(t1.b)
