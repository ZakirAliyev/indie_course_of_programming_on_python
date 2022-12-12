def fun():
    if x % 7 == 0 and y % 7 == 0:
        return True
    else:
        return False


x, y = map(int, input().split())
print(fun())
