# demoFormat.py
import sys
# url = "http://www.credu.com/?page=" + 1 => type error 1은 숫자형이므로 string형으로 변환이 필요함
url = "http://www.credu.com/?page=" + str(1)
print(url)

print("welcome to", "python", sep="~", end="!", file=sys.stderr)

# 파일에 쓰기
# mac, linux : 파일경로 /users/kim/DeskTop ...
#f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")
f = open(r"c:\work\demo.txt", "wt", encoding="utf-8") # r입력 후 파일경로\한개씩 작성 
print("file write", file=f)
f.close()

# 서식지정
print("--- 서식지정1 ---")
for x in range(1,6):
    print(x, "*", x, "=", x*x)

print("--- 서식지정2 ---")
for x in range(1,6):
    print(x, "*", x, "=", str(x*x).rjust(3))

print("--- 서식지정3 ---")
for x in range(1,6):
    print(x, "*", x, "=", str(x*x).zfill(3))

print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:2f}".format(4/3))
print("{0:,}".format(15000000))