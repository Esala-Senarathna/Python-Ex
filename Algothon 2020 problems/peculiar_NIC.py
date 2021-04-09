from datetime import datetime
N = input()

x = int(N[0:2])
y = int(N[2:5])
year = int('19' + str(x))

if y > 500:
    g ="F"
    days = (y - 500)
else:
    g = "M"
    days = y

res = datetime.strptime(str(year) + "-" + str(days), "%Y-%j").strftime("%Y-%m-%d")

print(res)
print(g)
#982471273