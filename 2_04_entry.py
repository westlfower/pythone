import tkinter as tk



def draw_triangle():
    m=entry.get()
    n=int(m)
    text_box.delete("1.0",tk.END)
    triangle=""

    for i in range(1,n+1,1):
        triangle+="*"*i+"\n"
        
    text_box.insert(tk.END,triangle)
window=tk.Tk()
window.geometry("800x500")
entry=tk.Entry(window,width=10, font=("Arial",20))
entry.place(x=50,y=20)

button=tk.Button(window,text="삼각형 출력",command=draw_triangle)
button.place(x=200,y=20)

text_box=tk.Text(window,width=30,height=15,font=("Arial",14))
text_box.place(x=50,y=70)

    

window.mainloop()
