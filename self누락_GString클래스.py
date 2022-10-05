# 전역변수
str = "Not Class Member"

class GString:
    def __init__(self):
        # 인스턴스 멤버 변수
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        # 버그 self.str로 작성해야 First Message가 나옴
        print(str)

g = GString()
g.set("First Message")
g.print()

