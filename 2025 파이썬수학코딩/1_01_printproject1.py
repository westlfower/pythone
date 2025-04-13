print(' '*0,'*'*5)
print(' '*1,'*'*3)
print(' '*2,'*'*1)


for x in range (0,7+1,1):
    print(' '*x, '*'*(7*2+1-2*x))

running=True

while running:
  k=input("피라미드는 숫자 1을, 평해사변형은 숫자 2를, 사다리꼴은 숫자 3을  입력해 주세요. 게임을 끝내려면 0을 눌러주세요.")
  n=input("n층 짜리 도형을 그릴까요?. n의 값을 정해 주세요. ")
  m=int(n)
  if k=="1":
    for x in range (0,m+1,1):
      print(' '*x, '*'*(m*2+1-2*x))
      
  elif k=="2":
    for x in range (0,m+1,1):
      print(' '*x, '*'*(2*m+1))
  elif k=="0":
      running=False

  else:
    for x in range (0,m+1,1):
      print(' '*(m-x), '*'*(3*m-2*(m-x)))



