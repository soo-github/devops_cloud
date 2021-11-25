from tkinter import *
from tkinter import messagebox


# 버튼을 사용하여 알림 창 띄우기
def clickButtion() :
    messagebox.showinfo('버튼 클릭', '버튼을 클릭했습니다.')  # (messagebox 타이틀, messagebox 내용)

window = Tk()
window.title("버튼 이벤트 연습")
window.geometry("200x200")

button1 = Button(window, text='요기 눌러요1', command=clickButtion)
button2 = Button(window, text='요기 눌러요2', command=clickButtion)
button3 = Button(window, text='요기 눌러요3', command=clickButtion)

button1.pack(side=TOP, padx=10, pady=10)  # 여백이나 배치 관련된 것들은 pack에서 하면 됨.
button2.pack(side=TOP, padx=10, pady=10)
button3.pack(side=TOP, padx=10, pady=10)

window.mainloop()