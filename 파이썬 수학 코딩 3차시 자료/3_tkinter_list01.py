import tkinter as tk
'''
기본 프레임.
window=tk.Tk()
window.geometry("500x500")
window.mainloop()
'''

fruits=[]
def save_list():
    fruit=entry.get()
    fruits.append(fruit)
    label2.configure(text=f"지금 까지 저장된 내용은 {fruits} 입니다.")
    
def save_memo():
    with open("fruits.txt","w",encoding="utf-8") as file:
        file.write(str(fruits))
    label3.configure(text=f"fruits.txt로 저장 성공")
    
window=tk.Tk()
window.geometry("500x500")
label=tk.Label(window,text="아래 빈칸에 과일 이름을 입력 후 저장 버튼 눌러 주세요.")
label.pack()
entry=tk.Entry(window)
entry.pack()
button=tk.Button(window,text="리스트에 추가",command=save_list)
button.pack()
                 
label2=tk.Label(window,text="저장된 목록을 보여줍니다.")
label2.pack()

button2=tk.Button(window,text="fruits.txt로 저장 ",command=save_memo)
button2.pack()

label3=tk.Label(window,text="")
label3.pack()

window.mainloop()
