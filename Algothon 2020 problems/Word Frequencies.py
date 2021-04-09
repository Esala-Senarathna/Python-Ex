N = int(input())
a = list()
l = ""
out={}
for i in range(N):
    t = input()
    l = l + " " + t
    s = l.split(" ")
    s.pop(0)
    a = a + s
a = set(a)
print(len(a))
for j in a:
     print(j,l.count(j))