from functools import singledispatch
@singledispatch
def process(value):
    raise NotImplementedError("Unsupported type")
@process.register(int)
def _(value):
    return f"Processing an integer:{value}"
@process.register(str)
def _(value):
    return f"Processing a string :{value}" 
print(process(10))
print(process("hello"))   