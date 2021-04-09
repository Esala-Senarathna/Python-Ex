def checkPerfect(N):
    if N < 10:
        return N
    else:
        y = list()
        sum = 0
        z = True
        while(z):
            x = N % 10
            N = N // 10
            y.append(x)
            if N < 10: z = False
        for i in y:
            sum = sum + i
        return checkPerfect(sum)

N = int(input())
print(checkPerfect(N))

