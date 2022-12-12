def fun():
    if a == b == c:
        return True
    else:
        return False


a, b, c = map(int, input().split())
print(fun())
