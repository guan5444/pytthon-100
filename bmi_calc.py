'''
BMI计算器
'''
height = float(input('请输入身高cm： '))
weight = float(input('请输入体重Kg： '))
bmi = weight / (height / 100) ** 2
print(f'{bmi = :.2f}')
if 18.5 <= bmi < 24:
    print('你的身材很棒')
elif bmi < 18.5:
    print('你的身材有点瘦')
else:
    print('你的身材有点胖')