# 부모클래스 정의
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))
    def coding(self):
        print(" -- 현재 코딩 중 --")
    def eating(self):
        print(" -- 현재 식사 중 --")

#######################        
# 자식클래스 정의 
# #  클래스 상속 방법 : 자식클래스(부모클래스)
class Student(Person):
    # 덮어쓰기 (재정의, override)
    def __init__(self, name, phoneNumber, subject, studentID):
        # self.name = name
        # self.phoneNumber = phoneNumber
        # 명시적으로 부모 초기화 메소드 호출
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID

    # 덮어쓰기 (재정의)
    def printInfo(self):
        print("Info(Name : {0}, PhoneNumber : {1})".format(self.name, self.phoneNumber))
        print("Info(subject : {0}, studentId : {1})".format(self.subject, self.studentID))

p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
p.printInfo()
s.printInfo()
s.coding()
s.eating()

