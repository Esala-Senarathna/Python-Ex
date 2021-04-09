N = input().split(" ")
start = int(N[0])
end = int(N[1])
divisor = int(N[2])
count = 0
for i in range(start, end+1):
    k = str(i)
    l = int(k[::-1])
    x = abs(i - int(l)) % divisor
    if x == 0: count = count +1
print(count)
