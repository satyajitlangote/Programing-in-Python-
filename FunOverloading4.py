class Math:
    @staticmethod
    def multiply(a,b):
        return a*b
    @staticmethod 
    def multiply(a,b,c):
        return a*b*c

class Math:
    @staticmethod 
    def multiply(*t):
        result=1
        for num in t:
            result *=num
        return result
print(Math.multiply(2,3))
print(Math.multiply(2,3,4,5))
