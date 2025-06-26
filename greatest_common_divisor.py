a = int(input('请输入数字a:'))
b = int(input('请输入数字b:'))
while a != b:
    a, b = min(a, b), abs(a-b)
print(f'{a}为最大公约数')

