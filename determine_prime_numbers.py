num = int(input('请输入一个整数:'))
end = int(num ** 0.5)
print(f'{end }')
is_prime = True
for i in range(2, end + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print(f'{num}是一个素数')
else:
    print(f'{num}不是一个素数')
