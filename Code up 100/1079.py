# 풀이 1
words = input().split()
for i in words:
    if i != 'q':
        print(i)
    else:
        break
print('q')

# 풀이 2
a = map(str, input().split())
for i in a:
    print(i)
    if i == 'q':
        break