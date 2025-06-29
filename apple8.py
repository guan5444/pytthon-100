# def fac(num):
#     result = 1
#     for n in range(1, num + 1):
#         result *= n
#     return result
#
# m = int(input('请输入m：'))
# n = int(input('请输入n：'))
# print(fac(m) // fac(n) // fac(m - n))

from math import factorial as f
m = int(input('请输入m：'))
n = int(input('请输入n：'))
print(f(m) // f(n) // f(m - n))