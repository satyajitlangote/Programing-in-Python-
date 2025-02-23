def evenNum(n):
    i = 1
    while n:
        yield 2 * i
        i += 1
        n -= 1

# Directly convert the generator to a list
even_list = list(evenNum(5))
print(even_list)