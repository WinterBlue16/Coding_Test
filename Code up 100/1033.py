# 풀이 1
print(hex(int(input()))[2:].upper())

# 풀이 2
a = int(input())
print(format(a, 'x').upper())

# 풀이 3
a = int(input())
print(('%x' % a).upper())

# 풀이 4
a = int(input())
print('%X' % a)
