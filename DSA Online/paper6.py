def sumCube(n):
    if n ==  1: return 1
    else: return sumCube(n -1) + (n * n * n)

while True:
    n = int(input("Enter an integer: "))
    if n == -1: break
    print("Sum of cubes: " +str(sumCube(n)))
