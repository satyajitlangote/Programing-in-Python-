x=5
def fun():
    x=10
    d=globals()
    print("local x=%d\n  global x=%d"%(x,d['x']))
    fun()