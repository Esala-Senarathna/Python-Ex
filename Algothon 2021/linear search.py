N = int(input())
I = input().split()
F = input()
for j,i in enumerate(I):
    if i == F:
        print(j)
        exit()
print("Value not found")