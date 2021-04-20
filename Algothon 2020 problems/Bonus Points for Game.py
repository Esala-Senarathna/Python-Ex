N = int(input())
count = 1
mul = 0
while(True):
    mul = count * 5
    count += 1
    if mul > N: break
if N >= 35:
    if N <= 90:
        if(mul - N) < 3: N = mul
print(N)