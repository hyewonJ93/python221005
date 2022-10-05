# demoDict.py
print("id : %s, name : %s" % ("kim","김유신"))

def calc(a,b):
    return a*b

#호출
args = (5,6)
print( calc(*args) )    # *args 는 튜플

#딕셔너리 초기화
device = {"아이폰" : 5, "아이패드" : 10, "윈도우타블렛" : 20}
print( device["아이패드"] )
device["맥북"] = 30
print( device )

#삭제
del device["아이폰"]
#수정
device["아이패드"] = 12

print(device)

for item in device.items():
    print(item)

print("--- 각각 받기 ---")
for k, v in device.items():
    print(k, v)

# tuple -> list 자료형 변경
tp = (1,2,3)
lst = list(tp)
lst.append(4)
print(lst)



phone = {"kim" : "111", "lee" : "222", "park" : "333"}
print("kim" in phone)
print("moon" in phone)

#참조를 복사
p = phone
p["moon"] = "1234"
print(p)
print( id(phone) )
print( id(p))

print("--- 논리식 ---")
print( 1 < 2)
print( 1 == 2)
print( 1 != 2)
print(True and True and True)
print(True and True and False)
print(True or True or False)

