#창 만들기
import tkinter as tk

창=tk.Tk()
창.title("이거는 동암중 방과후 자료")

# 도화지 넣기
도화지=tk.Canvas(창, width=480, height=300,bg="white")
도화지.pack()

x=100
y=100
r=20
#그대로 복사 사용 중심이 (x,y) 반지름이 r인 원 그리기

도화지.create_oval(x-r,y-r,x+r,y+r,fill="blue")

def 출력(event):
    print(event.keysym)
def change(event):
    global r, x
    #r=r+5
    
    if event.keysym=="Right":
        x=x+10
    elif event.keysym=="Left":
        x=x-10
    도화지.create_oval(x-r,y-r,x+r,y+r,fill="blue")
    
도화지.bind("<KeyPress>",change)
도화지.focus_set()



