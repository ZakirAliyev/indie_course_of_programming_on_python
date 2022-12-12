n = int(input())

minute = n % 3600 // 60
second = n % 3600 % 60

print(n // 3600, end=":")

if minute < 10:
    print("0" + str(minute),end=":")
else:
    print(minute,end=":")

if second < 10:
    print("0" + str(second))
else:
    print(second)
