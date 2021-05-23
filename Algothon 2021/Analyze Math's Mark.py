N = int(input())
s = input().split(" ")
k =[]
for i in s:
    k.append(int(i))
k.sort()
for j in k:
    print(j,end=" ")

