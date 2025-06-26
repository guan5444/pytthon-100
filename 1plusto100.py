i = 2
total = 0
while i <= 100:
    if i % 2 == 0:
        total = total + i
    i += 1
print('1~100偶数和=' , total)


i = 2
total = 0
while i <= 100:
    total = total + i
    i += 2
print('1~100偶数和=' , total)

i = 2
total = 0
while True:
    if i > 100:
        break
    total += i
    i += 2
print('1~100偶数和=' , total)


total = 0
for i in range(1, 101):
    if i % 2 != 0:
        continue
    total += i
    i += 2
print('1~100偶数和=' , total)