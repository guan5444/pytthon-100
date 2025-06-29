sentence = input('请输入一段话：')
counter = {}
for ch in sentence:
    if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
        counter[ch] = counter.get(ch, 0) + 1
        # print(f'{ch}出现了{counter[ch]}次')
sorted_key = sorted(counter, key = counter.get, reverse = True)
for key in sorted_key:
    print(f'{key}出现了{counter[key]}次')
