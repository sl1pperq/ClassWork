import random

p = []

for q in range(10000):
    l = []

    for u in range(40):
        l.append('4')

    for o in range(25):
        l.append('2')

    random.shuffle(l)

    s = '3' + ''.join(l) + '3'

    summa = 0

    while '3' in s:
        if '342' in s:
            s = s.replace('342', '4123')
        if '34' in s:
            s = s.replace('34', '413')
        if '32' in s:
            s = s.replace('32', '13')
        if '33' in s:
            s = s.replace('33', '424')

    for i in range(0, len(s)):
        j = int(s[i])
        summa += j

    p.append(summa)

print(max(p))