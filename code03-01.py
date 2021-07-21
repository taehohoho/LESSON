## 함수부
def add_data(friend) :  # 함수 = Function = 기능
    katok.append(None)
    kLen = len(katok)
    katok[kLen -1 ] = friend
    
def insert_data(position, friend) :
    katok.append(None)
    kLen = len(katok)
    for i in range(kLen-1, position, -1) :
        katok[i] = katok[i-1]
        katok[i-1] = None
        
    katok[position] = friend

def delete_data(position) :
    kLen = len(katok)
    katok[position] = None
    for i in range(position+1, kLen, 1) :
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[kLen-1])

## 전역변수
katok = [ ] # 빈 배열


## 메인코드
# 데이터 생성
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
add_data('모모')
print(katok)


# 데이터 삽입
insert_data(3, '미나')
print(katok)


# 데이터 삭제
delete_data(4)
print(katok)


