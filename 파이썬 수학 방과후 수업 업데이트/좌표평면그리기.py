import tkinter as tk

window=tk.Tk()
canvas=tk.Canvas(width=1200,height=600,bg='white')
canvas.pack()

for i in range(0,20,1):
    canvas.create_line(60*i,0,60*i,600)
for j in range(0,10,1):
    canvas.create_line(0,60*j,1200,60*j)

