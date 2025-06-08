import tkinter

fnt1=("Malgun Gothic",20)
fnt2=("Malgun Gothic",40)

index=0
timer=0
x=10
y=10
w=50
h=30
key=""

def key_down(e):
    global key
    key=e.keysym
def key_up(e):
    global key
    key=""

def main():
    global index, timer, x,y
    canvas.delete("STATUS")
    canvas.delete("BG")
    timer=timer+1
    canvas.create_text(200,30,text="index"+str(index),fill="white",font=fnt1,tag="STATUS")
    canvas.create_text(400,30,text="timer"+str(timer),fill="cyan",font=fnt1,tag="STATUS")
    if key=='Left':
        x=x-10
    elif key=='Right':
        x=x+10
    canvas.create_rectangle(x,y,x+w,y+h,fill='blue',tag="BG")
    
    #print(key)
    root.after(100,main)

root=tkinter.Tk()
root.bind("<KeyPress>",key_down)
root.bind("<KeyRelease>",key_up)
canvas=tkinter.Canvas(width=600,height=400,bg="black")
canvas.pack()

main()
root.mainloop()
