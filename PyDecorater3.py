# Python Decorater  
def decor_result(result_function):
    def distinction(marks):
        results = []
        for m in marks:
            if m >= 75:
                print("Distinction")
            results.append(result_function([m]))  # Corrected indentation
        return results
    return distinction

@decor_result
def result(marks):
    for m in marks:
        if m >= 33:
            pass
        else:
            print("Fail")
            return "FAIL"
    else:
        print("Pass")
        return "PASS"

# Use a different name for the decorated function
decorated_result = result([45, 78, 80, 34, 66, 90])
print("Result:", decorated_result)