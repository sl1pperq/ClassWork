def f(a, ss):
    res = ''
    while a > 0:
        res = str(a % ss) + res
        a = a // ss
    return res

l = []

for n in range(1, 1000):
    tn = f(n, 3)
    if n % 3 != 0:
        ost = f((n % 3) * 5, 3)
        tn = tn + ost

    r = int(tn, 3)
    if r > 146:
        l.append(n)

print(min(l))