#fibonacci method
def fibonacci(n):
    if n <= 1 : return n #base condition
    else: return fibonacci(n-1) + fibonacci(n-2) #recursive call

while True:
    n = int(input("Enter an Integer: ")) #inputs with prompts
    if n == -1: break #loop breaking condition
    print(str(n) +"th Fibinacci number: " + str(fibonacci(n-1))) #function call