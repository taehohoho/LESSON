## 함수

## 변수
stack = [None, None, None, None, None]

top = -1



## 메인
# push를 구현
top +=1
stack[top] = '커피'
top +=1
stack[top] = '녹차'
print('바닥 |', stack)

# pop 구현
data = stack[top]
stack[top] = None
top -= 1

print('추출 --> ', data)
print('바닥 |', stack)

data = stack[top]
stack[top] = None
top -= 1

print('추출 --> ', data)
print('바닥 |', stack)