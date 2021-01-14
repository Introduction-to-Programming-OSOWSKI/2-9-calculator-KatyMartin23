def calculate(c, x, y):
    if c == "add":
        return x + y
    elif c == "subtract":
        return x - y
    elif c == "multiply":
        return x * y
    else: return x / y
print(calculate("add", 5, 5))