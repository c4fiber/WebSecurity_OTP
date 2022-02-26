from tkinter import *
import time
from tkinter.font import Font
from typing import Sized
import generateOTP

# 초기 변수
name = 'victim'
serial = 'absde2kj32d1'

# tkinter 초기화 & 변수
root = Tk()
root.title("OTP Generator")
root.geometry("400x300+500+500") # 가로x세로 +좌표
root.resizable(False, True) # 크기, 위치 변경여부

otpText = "Press Button to generate OTP"
running = False
releaseTime = 60
counter = 0

fontStyle = Font(family="consolas", size=15)
otpLabel = Label(root, padx=50, pady=60,text=otpText, font=fontStyle)
otpLabel.pack()

e = Entry(root, width=15)
e.insert(0,serial)

f = Entry(root, width=15)
f.insert(0,name)

def renewOTP():
    global serial
    global name
    global counter
    global releaseTime
    global e
    global f

    serial = e.get()
    name = f.get()
    counter = releaseTime
    otpLabel.config(text=generateOTP.getOTP(serial, name, True, -1))


generateButton = Button(root, padx=100, pady=20, text="Generate OTP", command=renewOTP)
generateButton.pack()


label1 = Label(root, text=str(releaseTime)+"초간 유효합니다.")
label1.pack()

def countDown():
    global counter
    global releaseTime

    if counter <= 0:
        counter = releaseTime
        renewOTP()
    else:
        counter -= 1
    label1.config(text=str(counter)+"초간 유효합니다.")
    label1.after(1000, countDown)


e.pack()
f.pack()

countDown()

root.mainloop()
