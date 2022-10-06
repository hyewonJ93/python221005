# demoFile.py
f = open("c:\\work\\test.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

# 파일읽기
f = open("c:\\work\\test.txt", "rt", encoding="utf-8")
print(f.read())
print(f.tell())
# 파일포인터 리셋 seek(0)
f.seek(0)
# , end="" print 함수 자동 줄바꿈이 있으므로 줄바꿈 없도록 처리
print(f.readline(), end="")
print(f.readline(), end="")

f.seek(0)
# ['첫번째\n', '두번째\n', '세번째\n']
result = f.readlines()
print(result)

for item in result:
    # print(item, end="")
    print(item.replace("\n", ""))

f.close()

#################################
# 기존 파일에 첨부하는 경우
# a+ 파일이 없는 경우는 생성함, 기존 데이터가 있는경우 사라지지 않음
# wt를 사용하는 경우 기존에 데이터가 있는경우 기존 데이터는 사라짐
#################################
f = open("c:\\work\\test.txt", "a+", encoding="utf-8")
# f = open("c:\\work\\test.txt", "wt", encoding="utf-8")
f.write("다른데이터\n")
f.close()
