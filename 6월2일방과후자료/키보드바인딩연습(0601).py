import tkinter as tk

window=tk.Tk()
canvas=tk.Canvas(width=480,height=300)
canvas.pack()

x=0
dx=0
ani=0
MOVE_STEP=10

img_bg=tk.PhotoImage(file="park.png")
img_dog=[tk.PhotoImage(file="dog0.png"),tk.PhotoImage(file="dog1.png"),
         tk.PhotoImage(file="dog2.png"),tk.PhotoImage(file="dog3.png")]
'''
def animation():
    global x, ani
    x=x+4
    if x==480:
        x=0
    canvas.delete("BG")
    canvas.create_image(x-240,150,image=img_bg,tag="BG")
    canvas.create_image(x+240,150,image=img_bg,tag="BG")
    ani=(ani+1)%4
    canvas.create_image(240,200,image=img_dog[ani],tag="BG")
    window.after(200,animation)
animation()
'''

canvas.create_image(x-240,150,image=img_bg)
canvas.create_image(x+240,150,image=img_bg)

canvas.create_image(380+dx,200,image=img_dog[ani],tag="BG")

def move_left(event):
    canvas.delete("BG")
    global ani, dx
    ani=(ani+1)%4
    dx=dx-MOVE_STEP
    canvas.create_image(380+dx,200,image=img_dog[ani],tag="BG")

canvas.bind("<Left>",move_left)

canvas.focus_set()
window.mainloop()
