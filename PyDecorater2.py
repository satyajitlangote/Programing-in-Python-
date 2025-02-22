class Calculator:
    def _init_(self,func):
        self.function=func
        def _call_(self,*t,**d):
            result=self.function(*t,**d)
            return result**2
@Calculator
def add(a,b):
    return a+b
add(10,20)



