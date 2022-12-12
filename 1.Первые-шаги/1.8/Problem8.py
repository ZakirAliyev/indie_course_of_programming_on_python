n = int(input())

if n // 1440 == 0:
    print(n // 60, n % 60)
else:
    m = n % 1440
    print(m // 60, m % 60)
