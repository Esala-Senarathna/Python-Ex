L = input().split(", ")
N = int(input())
p =0
A=[]

if len(L) == 1:
    p = 1
    print(p)
    exit()

for o in L:
    A.append(int(o))
sorted(A)
for k,v in enumerate(A):
    if (v) > N :
        p = (k+1)
        break
    else: p = 1
    if (v) == N:
        p = (k + 1)
        break
    else: p = 1

if A[-1] < N :
    p = len(A) + 1
print(p)