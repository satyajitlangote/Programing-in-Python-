def welcome(fx):
    def mfx(*t,**d):
        print("Before hello functions ")
        fx(*t,**d)
        print("Thanks for using the function")
        return mfx

@welcome
def hello():
        print("Hello !")
@welcome
def add(a,b):
    print(a+b)

#hello()
#add(1,3)