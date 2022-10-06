# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        # 클래스 내부에 숨김 __변수명. 외부에서 접근불가
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
        # 블럭주석 ctrl + /
    def __str__(self):
        return "{0}, {1}, {2}".format(self.__id, 
        self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
#account1.balance = 15000000
print(account1)
#print(account1.__balance)
#변경된 이름으로 접근(테스트)
print(account1._BankAccount__balance) #백도어 확인가능
account1.__balance = 30000  # 동적확장이 됨.(사용X)
# print(account1)
