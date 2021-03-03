# 특정 문자를 직접 지정해 다른 문자로 치환하거나 제거한다
# string인 경우에는 for문을 쓸 필요 없다

# string
txt='.Hello.world.'

print(txt.replace('.', '#')) # 특정 문자 치환
print(txt.replace('.', '')) # 특정 문자 제거

# list
txt_li=['.Hello.world.', '.Hello.python.', '.Hello.javascript.']
for i in range(3):
    txt_li[i]=txt_li[i].replace('.', '#')
print(txt_li)

txt_li=list(map(lambda x:x.replace('.', '#'), txt_li))
print(txt_li)