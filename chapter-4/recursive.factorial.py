def factorial(n):
    if n in (0, 1):
        return 1 # case case
    return factorial(n - 1) * n # recursive case


print(factorial(4))