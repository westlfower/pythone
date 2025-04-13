import tkinter as tk
from tkinter import ttk
import random

def generate_random_polynomial():
    # 랜덤한 이차 다항식 생성 (ax^2 + bx + c)
    a = random.randint(1, 10)  # x^2의 계수
    b = random.randint(-10, 10)  # x의 계수
    c = random.randint(-10, 10)  # 상수항
    return a, b, c, f"{a}x^2 + {b}x + {c}"

def factorize():
    try:
        # 사용자 입력값 가져오기
        factor1 = int(entry_factor1.get())
        factor2 = int(entry_factor2.get())
        
        # 인수분해 성공 여부 확인
        if factor1 * factor2 == a * c and factor1 + factor2 == b:
            result_label.config(text="정답입니다! 인수분해 성공!")
        else:
            result_label.config(text="틀렸습니다. 다시 시도하세요.")
    except ValueError:
        result_label.config(text="숫자를 입력해주세요!")

# 랜덤한 다항식을 생성
a, b, c, polynomial = generate_random_polynomial()

# GUI 생성
win = tk.Tk()
win.title("인수분해 연습 게임")
win.geometry("500x300")

# 다항식 표시 라벨
label = ttk.Label(win, text=f"다항식을 인수분해하세요: {polynomial}")
label.pack(pady=10)

# 빈칸 입력 필드 (첫 번째 인수와 두 번째 인수)
entry_factor1 = ttk.Entry(win, width=10)
entry_factor1.pack(pady=5)
entry_factor1.insert(0, "첫 번째 숫자")

entry_factor2 = ttk.Entry(win, width=10)
entry_factor2.pack(pady=5)
entry_factor2.insert(0, "두 번째 숫자")

# 확인 버튼
button = ttk.Button(win, text="확인", command=factorize)
button.pack(pady=10)

# 결과 출력 라벨
result_label = ttk.Label(win, text="")
result_label.pack(pady=20)

win.mainloop()
