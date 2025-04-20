
# 직각 삼각형 그리기

# 직접 print로

print("*")
print("**")
print("***")
print("****")
print("*****")

#for 문을 이용해서
for i in range(1,7,1):
    print("*"*i)

# 피라미드 만들기

print("   *   ")
print("  ***  ")
print(" ***** ")
print("*******")

#수식 이용
# 맨 밑에가 7개(홀수개) 첫층 1개, 2층 3개, 3층 5개, n층은? 2n-1
print(" "*3+"*"*1+" "*3)
print(" "*2+"*"*3+" "*2)
print(" "*1+"*"*5+" "*1)
print(" "*0+"*"*7+" "*0)

#for 문 이용

for i in range(1,5,1):
    print(" "*(4-i)+"*"*(2*i-1)+" "*(4-i))


for i in range(1,10,1):
    print(" "*(9-i)+"*"*(2*i-1)+" "*(9-i))

#input 이용 n층 짜리 피라미드 만들기 (심화)

n= input("몇 층 짜리 피라미드를 만들까요? 숫자를 입력해주세요  ")
m=int(n)

for i in range(1,m+1,1):
    print(" "*(m-i)+"*"*(2*i-1)+" "*(m-i))

# if 문 이용 삼각형 또는 피라미드 그리기

running=True
while running:
  n=input("0을 입력하면 중단, 1을 입력하면 직각삼각형 , 2를 입력하면  피라미드" )
  if n=="0":
     running=False
  elif n=="1":
      m= input("몇 층 짜리 피라미드를 만들까요? 숫자를 입력해주세요  ")
      k=int(m)
      for i in range(1,k+1,1):
        print("*"*i)
  elif n=="2":
      m= input("몇 층 짜리 피라미드를 만들까요? 숫자를 입력해주세요  ")
      k=int(m)
      for i in range(1,k+1,1):
        print(" "*(k-i)+"*"*(2*i-1)+" "*(k-i))
      
      
    
