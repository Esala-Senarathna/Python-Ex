N = input().split("x = ")
N = list(N[1])

x = N[::-1]
print(N)
for i in x:
    print(i,end="")
