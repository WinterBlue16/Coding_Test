# 풀이 1
a, b, c, d = map(int, input().split())
byte = (a*b*c*d)/8
KB = byte/1024
print("%.1f" % (KB/1024), 'MB')