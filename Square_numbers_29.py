import math
N = int(input())
l = input().split()
sum = 0
for i in l:
    i = int(i)
    j = 0
    if i > 0:
        x = math.sqrt(i)
        x = int(x)
        if x*x == i:j = i
    sum = sum + j
print(sum)