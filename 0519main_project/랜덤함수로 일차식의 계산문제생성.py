#random.randint(a,b)

import random
running=True
while running:
  a=random.randint(-7,7)
  b=random.randint(-7,7)
  c=random.randint(-7,7)
  d=random.randint(-7,7)

  print("(",a,"x","+",b,")+(",c,"x+",d,") 를 간단히 하면")

  e=a+c
  f=b+d

  if f<0:
    print("계산 결과는",e,"x",f,"입니다.")
  else:
    print("계산 결과는",e,"x+",f,"입니다.")

  x=input("이 식에 대입할 x 값을 입력해주세요. x= ")
  x=int(x)

  result=e*x+f

  print("x=",x,"를 대입한 결과는 ", e,"*",x,"+",f,"=",result, "입니다.\n\n")


