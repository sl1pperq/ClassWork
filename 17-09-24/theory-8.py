# Из любой в десятичную

print(int('123', 4))
print(int('1010', 2))
print(int('F5A0', 16))
print(int('100', 10))

# В двоичную, восьмеричную, и т.д из десятичной

a = bin(37).replace('0b', '')
print(int(a, 2))

# Из десятичной в любую

a = 134
ss = 5
res = ''
while a > 0:
    res = str(a % ss) + res
    a = a // ss
print(res)

def f(a, ss):
    res = ''
    while a > 0:
        res = str(a % ss) + res
        a = a // ss
    return res
print(f(134, 5))