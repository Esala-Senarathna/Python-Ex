'''
n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

print(arr)
'''
arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
sum1,sum2 = 0, 0
for j in range(len(arr)):
    sum1 = sum1 + arr[j][j]
    sum2 = sum2 + arr[j][-1-j]
print(abs(sum1-sum2))