#demoSet.py
a = {1,2,3,3}
b = {3,4,4,5}

print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

lst = ["red", "blue", "green"]
for item in lst:
    print(item)


#대소문자 구분
Friend = 5
friend = 6
print(dir())
print(Friend)
print(friend)


#튜플
tp = (1,2,3)
print(len(tp))
print(tp[0])
print(tp.count(2))


#함수에서 한개이상 리턴
def times(a,b):
    return a+b, a*b

#함수를 호출
#print(times(3,4))

result = times(3,4)
print(result[0])
print(result[1])

##### calc(*arg) => *는 tuple을 이야기함
# 자주 사용하는 함수
# list(), str(), int, range()




