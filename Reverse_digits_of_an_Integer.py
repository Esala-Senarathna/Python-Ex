x = input().split("x = ")
k = x[1]
if int(k) >= (2**31 -1) or int(k) <= -2**31:
    print(int(k[::-1]))
else:
    print(0)