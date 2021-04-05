# collections 라이브러리 활용 1
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1) # left_add = data.appendleft(1)와 같은 변수 지정을 할 수 없다(typeerror 발생)
data.append(5)

# print(data)
# print(list(data)) 


# 추가 실습
# Queue 구현을 위해 deque 라이브러리 사용
queue=deque()

# 삽입(stack과 동일하게 오른쪽 끝부터 추가됨)
queue.append(5)
print(queue)
queue.append(2)
print(queue)
queue.append(3)
print(queue)
queue.append(7)
print(queue)

# 삭제(맨 앞의 값부터 잘려나감)
queue.popleft()
print(queue)
queue.popleft()
print(queue)

# 출력
print(queue) # 그대로 출력
queue.reverse()
print(queue) # 가장 최근에 들어온 값부터 출력