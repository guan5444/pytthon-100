a, b = 0, 1
for _ in range(20):
    a, b = b, a + b
    print(f'{a}', end=' ')