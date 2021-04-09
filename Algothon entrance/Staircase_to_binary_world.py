n = int(input())
p = n
for i in range(n):
    for j in range(p,1, -1):
        print(" ",end="")
    for k in range(i+1):
        print("#",end="")
    p = p-1
    print("")
