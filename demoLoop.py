# demoLoop.py

import itertools


value = 5
while value > 0:
    print(value)
    value -= 1
    #value = value - 1

# 시퀀스 형식은 for in을 사용
lst = [1,2,3,4,5,6,7,8,9,10]
for item in lst:
    print(item)


d = {"apple" : 100, "orange" : 200, "kiwi" : 300}
for k,v in d.items():
    print(k,v)

print("구구단 출력 시작")
for i in [2,3,4,5,6]:
    print("--{0}단---".format(i))
    for j in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(i,j,i*j))
print("구구단 출력 끝")

for i in [1,2,3,4,5,6,7,8,9,10]:
    print("*" * i)


print("---- break ----")
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i > 5:
        break
    print("item : {0}".format(i))

    
print("---- countinue ----")
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i % 2 == 0:
        continue
    print("item : {0}".format(i))


# 수열
print("--- 수열 ---")
print("range(10) ==> ", list(range(10)))
print("range(1,11) ==> ",list(range(1,11)))
print("range(2000,2023) ==> ",list(range(2000,2023)))

# 반복구문(수동 루프)
for i in range(10):
    print(i)

# 리스트 내장
print(" --- 리스트 내장 --- ")
lst = list(range(1,11))
print( [ i**2 for i in lst if i > 5])

tp = ("apple", "orange", "kiwi")
print([len(i) for i in tp])

d = {100 : "apple", 200 : "kiwi"}
print( [v.upper() for v in d.values()])


print(" --- 필터링없음 --- ")
lst = [10,25,30]
iterL = filter(None, lst)
for item in iterL:
    print(item)



print(" --- 필터링있음 --- ")
# 함수 정의
def getBiggerThan20(i):
    return i > 20

lst = [10,25,30]
iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)



