import tkinter as tk

#창 만들기

window=tk.Tk()

#창 크기 

window.geometry("650x350")

#도화지를 윈도우 위에 여기에 그림을 그린다.

canvas=tk.Canvas(width=600,height=300,bg="white")
canvas.pack()

# 도화지 위에 그림 뛰우기

img=tk.PhotoImage(file="chip00.png")


#터미널에 canvas.create_image(0,0,image=img) 처보면서 위치 지정해보기
#이미지 크기가 60x60 무엇을 발견할 수 있는가?

canvas.create_image(30,30,image=img)

#리스트로 여러 이미지 저장해보기

img_bg=[tk.PhotoImage(file="chip00.png"),tk.PhotoImage(file="chip01.png"),
        tk.PhotoImage(file="chip02.png"),tk.PhotoImage(file="chip03.png")]

# for x in range(0,10,1):
#    canvas.create_image(30+60*x,30,image=img_bg[x%4])

#터미널에 입력해보기
