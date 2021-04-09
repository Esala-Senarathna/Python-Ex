N = int(input())
max = 0
word_frequency = {}
l = list()
for i in range(N):
    word = input().split()
    max = 0
    freq = -1
    word_frequency = {}
    for j in word:
        c = word.count(j)
        word_frequency[j] = c
        v = list(word_frequency.values())
        k = list(word_frequency.keys())
        l.append(k[v.index(max(v))])

print(word_frequency)
