def fun():
    if a == b or b == c or a == c:
        return True
    return False


a, b, c = map(int, input().split())
print(fun())
