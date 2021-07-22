## 함수
# def isQueueFull() :
#     global size, queue, front, rear
#     if (rear == size -1):
#         return True
#     else :
#         return False
def isQueueFull() :
    global size, queue, front, rear
    if rear != size -1 :
        return False
    elif (rear == size -1) and (front == -1) :
        return True
    else :
        for i in range(front +1, size, 1) :
            queue [i-1] = queue[i]
            queue [i] = None
        front -= 1
        rear -= 1
        return False



def enQueue(data):
    global size, queue, front, rear   
    if(isQueueFull()):
        print('큐 꽉!')
        return
    rear += 1
    queue[rear] = data

def isQueueEmpty():
    global size, queue, front, rear   
    if (front == rear) :
        return True
    else :
         return False

def deQueue() :
    global size, queue, front, rear   
    if isQueueEmpty() :
        print('큐 텅!')
        return None
    
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global size, queue, front, rear   
    if isQueueEmpty() :
        print('큐 텅!')
        return None
    return queue[front+1]

## 전역
size =5
queue = [None for _ in range(size)]
front, rear = -1, -1


## 메인

# queue = ['화사', '솔라', '문별', '휘인', None]
# front = -1
# rear = 3

# print(isQueueFull())

# enQueue('화사')
# enQueue('솔라')
# enQueue('선미')
# enQueue('문별')
# enQueue('휘인')
# enQueue('재남')

enQueue('화사');enQueue('솔라')
print('출구<---', queue, '<--입구')
retData = peek()
print('다음 손님 대기하세요 -->', retData)

retData = deQueue()
print('입장 손님-->',retData)
retData = deQueue()
print('입장 손님-->',retData)
retData = deQueue()
print('입장 손님-->',retData)
print('출구<---', queue, '<--입구')