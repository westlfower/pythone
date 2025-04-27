import tkinter as tk
from tkinter import scrolledtext, messagebox
import os
import sys
import subprocess

desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
APP_NAME = "MyScheduleApp"

# pywin32 설치 여부 확인
try:
    import win32con
    import win32api
    WIN32_AVAILABLE = True
except ImportError:
    WIN32_AVAILABLE = False

class ScheduleApp:
    def __init__(self, root):
        self.root = root
        self.root.title('일정 기록 앱')
        self.root.geometry('400x430')

        # 텍스트 영역
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # 저장 버튼
        tk.Button(root, text='저장', command=self.save_schedule).pack(pady=5)

        # 자동 실행 UI (조건부 생성)
        if WIN32_AVAILABLE:
            self.setup_autorun_ui()
        else:
            self.setup_fallback_ui()

    def save_schedule(self):
        file_path = os.path.join(desktop_path, 'schedule.txt')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(self.text_area.get(1.0, tk.END))
        messagebox.showinfo('성공', f'일정 저장 완료:\n{file_path}')

    def setup_autorun_ui(self):
        """pywin32 사용 가능 시 체크박스 UI 생성"""
        self.autorun_var = tk.BooleanVar()
        self.autorun_check = tk.Checkbutton(
            self.root, 
            text='컴퓨터 시작 시 자동 실행',
            variable=self.autorun_var,
            command=self.toggle_autorun
        )
        self.autorun_check.pack(pady=5)
        self.check_current_autorun()

    def setup_fallback_ui(self):
        """pywin32 없을 때 대체 UI 생성"""
        tk.Button(
            self.root, 
            text='자동 실행 설정 방법 보기',
            command=self.show_fallback_guide
        ).pack(pady=5)

    def toggle_autorun(self):
        """레지스트리 기반 자동 실행 전환"""
        if self.autorun_var.get():
            self.add_to_startup()
        else:
            self.remove_from_startup()

    def add_to_startup(self):
        try:
            key = win32api.RegOpenKey(
                win32con.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Run",
                0, win32con.KEY_SET_VALUE
            )
            win32api.RegSetValueEx(
                key, APP_NAME, 0, win32con.REG_SZ,
                f'"{sys.executable}" "{os.path.abspath(sys.argv[0])}"'
            )
            win32api.RegCloseKey(key)
            messagebox.showinfo('성공', '자동 실행이 활성화되었습니다')
        except Exception as e:
            messagebox.showerror('오류', f'설정 실패: {str(e)}')

    def remove_from_startup(self):
        try:
            key = win32api.RegOpenKey(
                win32con.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Run",
                0, win32con.KEY_SET_VALUE
            )
            win32api.RegDeleteValue(key, APP_NAME)
            win32api.RegCloseKey(key)
            messagebox.showinfo('성공', '자동 실행이 비활성화되었습니다')
        except Exception as e:
            messagebox.showerror('오류', f'해제 실패: {str(e)}')

    def check_current_autorun(self):
        """현재 자동 실행 상태 확인"""
        try:
            key = win32api.RegOpenKey(
                win32con.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Run",
                0, win32con.KEY_READ
            )
            try:
                win32api.RegQueryValueEx(key, APP_NAME)
                self.autorun_var.set(True)
            except FileNotFoundError:
                self.autorun_var.set(False)
            win32api.RegCloseKey(key)
        except Exception:
            pass

    def show_fallback_guide(self):
        """대체 안내 메시지"""
        guide = (
            "1. [Win+R] 키 누르고 'shell:startup' 입력 후 실행\n"
            "2. 열린 폴더에 이 프로그램의 바로가기를 추가\n"
            "3. pywin32 설치 시 자동 설정 가능:\n"
            "   pip install pywin32"
        )
        messagebox.showinfo('자동 실행 설정 방법', guide)

if __name__ == '__main__':
    root = tk.Tk()
    ScheduleApp(root)
    root.mainloop()
