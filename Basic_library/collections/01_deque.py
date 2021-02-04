# collections 라이브러리 활용 1
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1) # left_add = data.appendleft(1)와 같은 변수 지정을 할 수 없다(typeerror 발생)
data.append(5)

print(data)
print(list(data)) 