'''
查询闰年
平年输出False 闰年输出True
'''

year = float(input('请输入需要查询的年份: '))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(f'{is_leap = }')
