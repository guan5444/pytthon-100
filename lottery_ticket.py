

import random
redBallpool = list(range(1, 34))
selectBall = []
for i in range(6):
    num = random.randrange(len(redBallpool))
    selectBall.append(redBallpool[num])
    redBallpool.remove(redBallpool[num])
print('红球是：')
for selectBall in selectBall:
    print(selectBall, end=' ')
blueBall = random.randrange(1, 16)
print(f'篮球是：', blueBall)

