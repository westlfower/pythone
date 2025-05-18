



#tkinter, Label, Entry, Text, Button

import tkinter as tk

l_font=("Malgun Gothic",25)


window=tk.Tk()

tk.Label(window,text="a=: ",font=l_font).grid(row=0,column=0)
a_value=tk.Entry(window,font=l_font)
a_value.grid(row=0,column=1)

tk.Label(window,text="b=: ",font=l_font).grid(row=1,column=0)
b_value=tk.Entry(window,font=l_font)
b_value.grid(row=1,column=1)


def calculator():
    a=int(a_value.get())
    b=int(b_value.get())
    text.delete("1.0",tk.END)
    text.insert(tk.END,(f"a={a},b={b}일 때, \n"))
    text.insert(tk.END,(f"2a-3b=2*{a}-3*{b}={2*a-3*b}"))

tk.Button(window,text="계산",font=l_font,command=calculator).grid(row=2,column=0)
text=tk.Text(window,height=5,width=30,font=l_font)
text.grid(row=3,columnspan=2)

#window.mainloop()
