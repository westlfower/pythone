#변수
score=0
print(score)
score=score+100
print(score)

#변수로 문자열 다루기

name="김현준"
print("당신의 이름은 "+name)

#리스트
#리스트 내의 상자를 엘리먼트 라고 한다. 상자의 순서를 관리하는 번호를 인덱스
#리스트명= [ 데이터0, 데이터1, 데이터2,...]
enemy=["슬라임","해골병사","마법사"]
print(enemy[0])
print(enemy[1])
print(enemy[2])

# for 문 이용한 반복문
for i in range(0,3):
    print(enemy[i])
    
for i in range(0,3,1):
    print(i)
# 조건문
# a==b   a!=b   a>=b    a<=b

a=input("수를 입력해주세요")
number=int(a)
if number>0:
    print("양수 입니다.")
else:
    print("양수가 아닙니다.")

    
print("방과후 선생님 이름은?")
ans=input()
if ans == "김현준":
    print("정답입니다.")
else:
    print("틀렸습니다.")

print("방과후 선생님 이름은?")
ans=input()
if ans == "김현준" or ans == "KIMHYUNJUN":
    print("정답입니다.")
else:
    print("틀렸습니다.")

#while 이용한 반복문
i=0
while i<5:
    print(i)
    i=i+1

running=True
while running:
    a=input("질문을 멈추려면 숫자 0을 눌러 주세요")
    if a=="0":
        running=False

#함수

def win():
     print("당신이 승리했습니다.!")
win()

def recover(val):
     print("당신의 체력은?")
     print(val)
     print("회복했다!")

recover(100)

def add(a,b):
    return a+b
c=add(1,2)
print(c)
