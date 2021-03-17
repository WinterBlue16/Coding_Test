# 약수 구하기(작은 수부터 k번째 약수)
if __name__=='__main__':
    n, k=map(int, input().split())
    print(solution(n, k))

def solution(n, k):
    divisor=[]
    count=0

    for i in range(1, n+1):
        if n%i==0:
            divisor.append(i)
            count+=1
            if count==k:
                break

    if len(divisor) < k:
        return 0

    return divisor[-1]

if __name__=='__main__':
    n, k=map(int, input().split())
    print(solution(n, k))

# 약수 구하기(큰 수부터 k번째 약수)
# def solution(n, k):
#     divisor=[]
#     v=n
#     count=0

#     while True:
#         if n%v==0:
#             divisor.append(v)
#             v-=1
#             count+=1
#             if count==k:
#                 break
#         else:
#             v-=1
    
#     if len(divisor) < k:
#         return 0

#     return divisor[-1]