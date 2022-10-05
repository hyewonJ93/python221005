# function2.py
# 교집합 글자 리턴
def intersect(prelist, postlist):
    # 지역변수
    result = []
    # H(0) | A(1) | M(2)
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

# 호출
print( intersect("HAM", "SPAM"))


#######################################
# 가변형식은  레퍼런스 참조로 원본 값이 변경됨 deepcopy가 아니면...
# 가변형식
def change(x):
    x[0] = "H"

# 호출
wordlist = ["J", "A", "M"]
change(wordlist)
print("함수호출 후 x : ", wordlist)

#######################################
# 복사본 수정
def change2(x):
    # 복사
    x1 = x[:]
    x1[0] = "H"
    print("함수내부 : " , x1)
    
# 호출
wordlist = ["J", "A", "M"]
change2(wordlist)
print("함수호출 후 x1 : ", wordlist)


# 불변형식에서 함수내부에서 읽기 + 쓰기
# global 사용 시 전역변수 값 변경 가능
g = 1
def testScope(a):
    #global g
    g = 2
    return a + g

# 함수호출
print(testScope(1))
print("전역변수 g : ", g)


# 기본값
def times(a = 10, b = 20):
    return a * b

print(times())
print(times(5))
print(times(5,6))


# 키워드 인자
def connectURI(server, port):
    strURL = "http://" + server + ":" + port
    return strURL


print(connectURI("credu.com", "80"))
### 키워드인자방식 
print(connectURI(port = "80", server = "credu.com"))



