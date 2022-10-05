# class2.py
# 1) 클래스 정의(type)
class Person:
    # 클래스 멤버 변수
    num_person = 0
    # 초기화 메소드
    def __init__(self):
        self.name = "default name"
        Person.num_person += 1
    # 인스턴스 메소드
    def print(self):
        print("My name is {0}".format(self.name))

# 2) 인스턴스(복사본 생성)
# 중단점 생성(break point)
p1 = Person()
p2 = Person()
p3 = Person()

# 3) 메소드 호출
print("인스턴스 갯수 : {0}".format(Person.num_person))

# 런타임시에 변수 추가
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)

