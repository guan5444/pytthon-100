import random

num = random.randrange(1, 100)
while True:
    guessNum = int(input('请输入你猜的数字(1~100)'))
    if guessNum == num:
        print('猜对了')
        break
    elif guessNum > num:
        print('猜大了')
    else:
        print('猜小了')
