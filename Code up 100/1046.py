# 풀이 1
a, b, c = map(int, input().split())
total= a+b+c
print(total, '%.1f'% (total/3), sep='\n')

# 풀이 2
import numpy as np

nums = map(int, input().split())
nums = list(nums)
print(sum(nums), '%.1f' % np.mean(nums), sep='\n')
