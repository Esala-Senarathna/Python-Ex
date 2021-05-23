N = input().split(" ")
S = input().split(" ")
Q = input().split(" ")
L = []
for i in Q:
    sum = 0
    for n,j in enumerate(S):
        sum += int(j)
        if sum >= int(i):
            L.append(n+1)
            break
for k in L: print(k)