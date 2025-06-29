def make_judgement(a, b, c):
    return a + b > c and a + c > b and b + c > a

print(make_judgement(3, 7, 9))