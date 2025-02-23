# Is Function Overloading allowed in python 
def greet(name,greeting="Hello"):
    return f"{greeting},{name}!"
print(greet("Satyajit"))
print(greet("Rohit","Hi"))