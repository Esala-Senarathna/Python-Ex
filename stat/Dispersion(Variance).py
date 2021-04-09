import statistics

n_num = input()
num = [y.strip() for y in n_num.split(' ')]
n = len(num)
lis = []
for i in range(0,n):
    x = float(num[i])
    lis.append(x)

lis.sort()
print(lis)

print("Population Variance: ", statistics.pvariance(lis))
print("Population SD: ", statistics.pstdev(lis))

print("Sample Variance: ", statistics.variance(lis))
print("Sample SD: ", statistics.stdev(lis))
