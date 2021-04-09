import random
N = int(input())

c = "Tom"
b = [2,3,5]
while(N > 1):
    if N == 10: y = 3
    elif N == 9: y = 2
    elif N == 8 or N == 7 or N == 6 or N == 5:
        if c == "Jerry":
            c = "Tom"
        else:
            c = "Jerry"
        break
    elif N == 4 or N == 3: y = 3
    elif N == 2: y = 2
    else: y = random.choice(b)

    N = N - y

    if N <= 1 : break

    if c == "Jerry":
        c = "Tom"
    else:
        c = "Jerry"
print(c)