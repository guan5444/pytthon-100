'''
输入圆形半径，计算圆形周长和面积
'''
import math

radius = float(input('请输入圆形半径： '))
perimeter = (math.pi * radius * 2)
area = radius * radius * math.pi
print('该圆形周长为:', perimeter)
print('该圆形面积:', area)
print('该圆形周长为: %.2f' % perimeter)
print('该圆形面积为: %.2f' % area)
print(f'该圆形周长为: {perimeter:.2f}')
print(f'该圆形面积为: {area:.2f}')
print(f'{perimeter = :.2f}')
print(f'{area = :.2f}')
