## 함수
def isStackFull() : # 스택 꽉 확인
    global size, stack, top
    if top == size-1 : 
        return True
    else : 
        return False
    
def push(data) : # 푸쉬
    global size, stack, top
    if (isStackFull()==True):
        print('스택 꽉!')
        return
    top += 1
    stack[top] = data
    
## 전역
size = 5
stack = [ None for _ in range(size)]
top = -1



## 메인
push('커피1')
push('커피2')
push('커피3')
push('커피4')
push('커피5')


print('바닥|', stack)

push('녹차')
print('바닥|', stack)