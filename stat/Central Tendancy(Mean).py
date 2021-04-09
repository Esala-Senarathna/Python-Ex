n_num = input()
num = [y.strip() for y in n_num.split(' ')]
n = len(num)
lis = []
for i in range(0,n):
    x = float(num[i])
    lis.append(x)

lis.sort()
print(lis)

#Mean  
get_sum = sum(lis)
mean = get_sum / n
  
print("Mean / Average is: " + str(mean))

#Q1
if n % 2 == 0:
    quart1 = lis[n//4]
    quart2 = lis[n//4 - 1]
    q1 = quart2 + (quart1 - quart2)*(((n+1)/4)%1)
else:
    q1 = lis[n//4]
print("Q1 is: " + str(q1))

#Q2/Median  
if n % 2 == 0:
    median1 = lis[n//2]
    median2 = lis[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = lis[n//2]
print("Median is: " + str(median))

#Q3
if n % 2 == 0:
    quart3 = lis[3*(n+1)//4]
    quart4 = lis[3*(n+1)//4 - 1]
    q3 = quart4 + (quart3 - quart4)*((3*(n+1))/4%1)
else:
    q3 = lis[3*n//4]
print("Q3 is: " + str(q3))

#Mode
from collections import Counter
n = len(num)
  
data = Counter(lis)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
  
if len(mode) == n:
    get_mode = "No mode found"
else:
    get_mode = "Mode is / are: " + ', '.join(map(str, mode))
      
print(get_mode)

#55 57 58 63 64 64 56 58 70 72 72 74 74 74 74 75 76 76 77 77 79 79 80 80 81 81 81 82 82 82 83 83 83 84 85 88 88 88 88 89 89 90 90 90 91 92 92 94 95 95 95
