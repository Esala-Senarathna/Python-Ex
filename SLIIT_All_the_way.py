n = input()
s = input()
ch = 'SLIIT'
ptr = 0
count = 0

for c in s:
   if c==ch[ptr]:
      if ptr==len(ch)-1:
         count += 1
         ptr = 0
      else:
         ptr += 1
print(count)
