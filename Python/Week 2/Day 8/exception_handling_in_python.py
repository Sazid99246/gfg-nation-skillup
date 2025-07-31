def find_minimum(a, b):
    try:
        return min([a + b, a - b, a * b, a / b])
    except ZeroDivisionError:
        return min([a + b, a - b, a * b, 0])
