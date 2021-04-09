
def fibonacci(N):
    if N > 2: return fibonacci(N-1) + fibonacci(N-2)

    else: return 1

N =  int(input())
x =fibonacci(N)
print(x)