# 파이썬의 함수는 호출 시 키워드를 지정할 수 있었다
def f(a=0, b=0):
    return a + b

print(f(b=4))


# 키워드 지정 인수를 의무로 사용하도록 할 수 있는데, 키워드 지정 인수라고 부른다
def f(a=0, b=0, *, c=0, d=0):
    # * 뒤의 인수들이 키워드 지정 인수
    return a + b + c + d

print(f(b=3, c=8, d=10))
# 이처럼 키워드 지정 인수인 c와 d는 키워드 형식으로 인수를 전달하지 않으면 오류가 발생한다

f(1, 2, 3, 4)