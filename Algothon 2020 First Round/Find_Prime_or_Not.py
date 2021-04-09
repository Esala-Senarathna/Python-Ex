N = int(input())

for i in range(N-1,1,-1):
    if N % i == 0:
        print(N ,"is not a prime number")
        exit()
print(N, "is a prime number")

