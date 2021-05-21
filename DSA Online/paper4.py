#power function
def power(base, exp):
    if exp == 0: return 1 #base condition
    else: return  base * power(base, exp-1) #recursive function call

while True: #infinite loop
    x = int(input("Enter a number for x: "))
    n = int(input("Enter an integer for n: "))
    if n == -1: break #loop breaking condition
    print("Answer: " + str(power(x,n))) #function call