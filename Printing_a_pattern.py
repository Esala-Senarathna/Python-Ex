N = int(input())

for i in range(N+1):
    for j in range(i):
        print("*",end="")
    print()
for k in range(N-1,0,-1):
    for j in range(k):
        print("*", end="")
    print()