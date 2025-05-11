print("(ax+b)+(cx+d) 를 계산해 보자.")

a=input("a에 알맞은 정수를 입력해 주세요.  ")
a=int(a)
b=input("b에 알맞은 정수를 입력해 주세요.  ")
b=int(b)
c=input("c에 알맞은 정수를 입력해 주세요.  ")
c=int(c)
d=input("d에 알맞은 정수를 입력해 주세요.  ")
d=int(d)
e=(a+c)
f=(b+d)
print("계산 결과는",e,"x+","(",f,") 입니다.")

'''
업그레이드
'''

if f<0:
  print("계산 결과는",e,"x",f,"입니다.")
else:
  print("계산 결과는",e,"x+",f,"입니다.")

x=input("이 식에 대입할 x 값을 입력해주세요. x= ")
x=int(x)

result=e*x+f

print("x=",x,"를 대입한 결과는 ", e,"*",x,"+",f,"=",result, "입니다.")


  




