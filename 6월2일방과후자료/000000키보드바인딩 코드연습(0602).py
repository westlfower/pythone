#공을 버튼에 따라 움직이고 마우스 드래그 이동 까지 구현

import tkinter as tk

window=tk.Tk()
canvas=tk.Canvas(width=480,height=300,bg="white")
canvas.pack()
x=100
y=100
r=20

MOVE_STEP=30


circle=canvas.create_oval(x-r,y-r,x+r,y+r,fill="blue",tag="BG")

#키보드 조작
def move_left(event):
    global x
    canvas.delete("BG")
    x=x-MOVE_STEP
    circle=canvas.create_oval(x-r,y-r,x+r,y+r,fill="blue",tag="BG")
    
def move_right(event):
    global x
    canvas.delete("BG")
    x=x+MOVE_STEP
    circle=canvas.create_oval(x-r,y-r,x+r,y+r,fill="blue",tag="BG")

canvas.bind("<Left>",move_left)
canvas.bind("<Right>",move_right)
canvas.focus_set()



window.mainloop()
