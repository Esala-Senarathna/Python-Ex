n = int(input())
y=[]
for i in range(n):
    x = int(input())
    y.append(x)
y = sorted(y, reverse=True)
for j in y:
    print(j,end="")
