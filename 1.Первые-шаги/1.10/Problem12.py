def fun():
    if a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or c ** 2 + b ** 2 == a ** 2:
        return True
    return False


a, b, c = map(int, input().split())
print(fun())
