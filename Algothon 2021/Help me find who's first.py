dictionary = {}
for i in range(5):
    N = input().split(" ")


    if N[1] == 'A': gVal = 4.0
    elif  N[1] == 'B': gVal = 3.0
    elif  N[1] == 'C': gVal = 2.0
    elif  N[1] == 'D': gVal = 1.0
    elif  N[1] == 'F': gVal = 0.0

    if N[3] == 'A': gVal2 = 4.0
    elif  N[3] == 'B': gVal2 = 3.0
    elif  N[3] == 'C': gVal2 = 2.0
    elif  N[3] == 'D': gVal2 = 1.0
    elif  N[3] == 'F': gVal2 = 0.0

    CGPA = ((gVal * float(N[2])) + (gVal2 * float(N[4]))) / (float(N[2]) + float(N[4]))
    dictionary[N[0]] = CGPA
sort_orders = sorted(dictionary.items(), key=lambda x: x[1])
s=""
for l in sort_orders:
    s = s + l[0] + ","
print(s[:-1])