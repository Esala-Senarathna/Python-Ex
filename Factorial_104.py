def factorial(val):
    if val == 1: return 1
    else:
        return val * factorial(val-1)

N = int(input())
x = list()
for i in range(N):
    val = int(input())
    x.append(factorial(val))
for j in x:
    print(j)