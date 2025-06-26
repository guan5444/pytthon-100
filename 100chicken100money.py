for i in range(0, 21):
    for j in range(0, 34):
        k = 100 - i - j
        if  k % 3 == 0 and 5 * i + 3 * j + k // 3 == 100:
            print(f'公鸡：{i}只 母鸡:{j}只 小鸡：{k}只')