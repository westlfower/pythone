import tkinter as tk

win=tk.Tk()

win.title("모눈종이 그리기")
#변수들
w=1200
h=600
bg_color="white"

#can=tk.Canvas(width=1200,height=600,bg="white")
can=tk.Canvas(width=w,height=h,bg=bg_color)
can.pack()

#직선그리기
'''
can.create_line(60*0,0,60*0,600,width=2)
can.create_line(60*1,0,60*1,600,width=2)
can.create_line(60*2,0,60*2,600,width=2)
can.create_line(60*3,0,60*3,600,width=2)
can.create_line(60*4,0,60*4,600,width=2)

'''

#for문
for i in range(0,20,1):
  can.create_line(60*i,0,60*i,600,width=2)
  
for j in range(0,10,1):
  can.create_line(0,60*j,1200,60*j,width=2)
  
can.create_rectangle(0,0,60,60,fill='black')
 
'''
#이중 for 문 (중급)
for i in range(0,20,1):
  for j in range(0,10,1):
    can.create_line(60*i,0,60*i,600,width=2)
    can.create_line(0,60*j,1200,60*j,width=2)
'''

    
win.mainloop()











