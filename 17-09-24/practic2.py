l = []

for n in range(1, 100):
    bn = bin(n).replace('0b', '')
    bn = bn.zfill(8)

    bn = bn + '2'
    if bn[-2] == '0':
        bn = bn.replace('02', '')
    else:
        bn = bn.replace('12', '')

    bn = bn[::-1]
    r = int(bn, 2)
    if n == r:
        l.append(n)

print(max(l))