for i in range(100, 1000):
    if i == int((i // 100) ** 3 + (i % 100 // 10) ** 3 + (i % 10) ** 3):
        print(f'{i}', end=' ')