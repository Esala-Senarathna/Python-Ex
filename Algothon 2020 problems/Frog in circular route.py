N = input().split(",")
G = input().split(",")
s = 1-(len(N))
print(s)
count = 0
for j in range(1-(len(N)),1,1):
    if count == (len(N) - 2): count = 0
    remainGain = int(G[count])
    for i in range(j,1,1):

        if int(N[count]) > remainGain:
            count += 1
            s = i + 1
            print(i)
            break
        else:
            remainGain =  remainGain + (int(G[count]) - int(N[count]))
            if i != 0: remainGain = remainGain + int(G[count+1])
            else: remainGain =  remainGain + int(G[0])
            count += 1

# if s > 0: s = -1
print(s)

# 3,4,3
# 2,3,4