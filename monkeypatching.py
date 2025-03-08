class test:
    def __init__(self,x):
        self.a=x
    def get_data(self):
        print("Send code to fetch data from database ")
    def f1(self):
        self.get_data()
    def f2(self):
        self.get_data()
t1=test(4)
print("Before Monkey Patching \n")
print("\n After Monkey  Patching ")
t1.f1()
t1.f2()
