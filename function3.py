# function3.py
# 가변인자(내부에서 tuple로 받기 *변수명)
def union(*ar):
    # 지역변수에 글자 모아두기
    result = []
    # HAM(0) | EGG(1) 
    for item in ar:
        for x in item:
            if x not in item:
                result.append(x)
    return result

# 호출
print(union("HAM", "EGG"))
print(union("HAM", "EGG", "SPAM"))

######################################
# 정의되지 않은 인자처리
# **변수명 -> 사전형으로 key = value
def userURIBuilder(server, port, **user):
    strURL = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL

# 호출
# 줄이 변경되는 경우 알아서 한줄로 인식. 인식이 안될경우 \붙이기
print(userURIBuilder("credu.com", "80", id = "kim", password = "1234"))
print(userURIBuilder("credu.com", "80", id = "kim", password = "1234",
 name = "mike"))

# 람다함수
g = lambda x, y:x*y
print(g(3,4)) 
print(g(5,6)) 
print((lambda x:x*x)(3)) 
print(globals())


print(" --- 필터링있음 --- ")
lst = [10,25,30]
iterL = filter(lambda x:x>20, lst)
for item in iterL:
    print(item)


