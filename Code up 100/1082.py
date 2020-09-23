# 풀이 1
a = int(input(), 16)
x = hex(a)[2:].upper()

for i in range(1, 16):
    b = hex(i)[2:].upper()
    c = hex(a*i)[2:].upper()
    print(x, '*', b, '=', c, sep='')