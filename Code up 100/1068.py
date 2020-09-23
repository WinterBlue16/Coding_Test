# 풀이 1
a = int(input())

def grade(a):
    if 90<=a<=100:
        return 'A'
    elif 70<=a<=89:
        return 'B'
    elif 40<=a<=69:
        return 'C'
    else:
        return 'D'

print(grade(a))

# 풀이 2
a = int(input())

if a >=90:
    print('A')
elif a >=70:
    print('B')
elif a >=40:
    print('C')
else:
    print('D')