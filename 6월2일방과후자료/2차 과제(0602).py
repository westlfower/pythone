#공을 버튼에 따라 움직이고 마우스 드래그 이동 까지 구현

import tkinter as tk

window=tk.Tk()
canvas=tk.Canvas(width=480,height=300,bg="white")
canvas.pack()

x=100
y=100
r=20

MOVE_STEP=30

start_x=0
start_y=0

circle=canvas.create_oval(x-r,y-r,x+r,y+r,fill="blue",tag="BG")

def on_press(event):
    global start_x, start_y
    start_x=event.x
    start_y=event.y
    
def on_drag(event):
    global start_x, start_y
    #이동할 거리 계산
    dx=event.x-start_x
    dy=event.y-start_y
    #원을 이동
    canvas.move("BG",dx,dy)
    #시작점 갱신
    start_x=event.x
    start_y=event.y

canvas.tag_bind("BG","<ButtonPress-1>",on_press)
canvas.tag_bind("BG","<B1-Motion>",on_drag)

window.mainloop()
