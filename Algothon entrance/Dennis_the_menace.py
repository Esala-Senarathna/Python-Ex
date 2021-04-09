N = input().split(" ")
num = int(input())
for i in range(0, len(N)):
    N[i] = int(N[i])
N.sort()
N = N[::-1]
sum = 0
for j in range(num):
    sum = sum + N[j]
print(sum)