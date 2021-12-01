from tkinter import *
import time
from tkinter.font import Font
import generateOTP

root = Tk()
root.title("OTP Generator")
root.geometry("400x300+500+500") # 가로x세로 +좌표

root.resizable(False, True) # 크기, 위치 변경여부

otpText = "Press Button to generate OTP"
running = False
counter = 30

fontStyle = Font(family="consolas", size=15)
otpLabel = Label(root, padx=50, pady=60,text=otpText, font=fontStyle)
otpLabel.pack()

def renewOTP():
    # OTP 새로고침 함수
    global counter
    counter = 31
    otpLabel.config(text=generateOTP.getOTP())
    #print("수정필요, OTP 새로고침")

generateButton = Button(root, padx=100, pady=20, text="Generate OTP", command=renewOTP)
generateButton.pack()


label1 = Label(root, text="30초간 유효합니다.")
label1.pack()

def count():
    global counter

    if counter <= 0:
        counter = 30
        renewOTP
    else:
        counter -= 1
    label1.config(text=str(counter)+"초간 유효합니다.")
    label1.after(1000, count)

count()

root.mainloop()
