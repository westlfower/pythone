import tkinter as tk

def get_entry_value():
    try:
        a = int(entry.get())
        return a
    except ValueError:
        return None

def draw_pyramid():
    m = get_entry_value()
    text_box.delete("1.0", tk.END)  # 이전 출력 지우기
    if m is None or m < 1:
        text_box.insert(tk.END, "자연수를 입력하세요.\n")
        return
    pyramid = ""
    for i in range(1, m+1):
        pyramid += " "*(m-i) + "*"*(2*i-1) + " "*(m-i) + "\n"
    text_box.insert(tk.END, pyramid)

window = tk.Tk()
window.geometry("400x400")

entry = tk.Entry(window, width=10, font=("Arial", 20))
entry.place(x=50, y=20)

button = tk.Button(window, text="피라미드 출력", command=draw_pyramid)
button.place(x=200, y=20)

text_box = tk.Text(window, width=30, height=15, font=("Consolas", 14))
text_box.place(x=50, y=70)

window.mainloop()
