n = int(input())
sum = 0

sum += n // 100
n = n % 100

sum += n // 20
n = n % 20

sum += n // 10
n = n % 10

sum += n // 5
n = n % 5

sum += n // 1
n = n % 1

print(sum)
