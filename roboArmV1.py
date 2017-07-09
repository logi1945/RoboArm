__author__ = 'Artur_G'

import serial
import time
import Tkinter
import tkMessageBox
from Tkinter import *

usbport = 'COM3'

ser = serial.Serial(usbport, 9600, timeout=1)
currPositions = [90, 90, 90, 35]

root = Tk()
root.geometry("794x220")
root.resizable(width=False, height=False)

A1 = Button(root, text="FORWARD ", width=10, height=2, command=lambda: moveIncrement(2, 1))
A3 = Label(root, text="SERVO 0 L/R", width=12, height=2)
A4 = middleServo = Tkinter.Label(None, text=currPositions[0], font=('Times', '12'), fg='blue')
A5 = Button(root, text="JUMP TO:", width=10, height=2, command=lambda: moveButton(A6, 0))
A6 = Entry(root, width=10)
A6.insert(END, "90")
A7 = Label(root, text="CLAWN ->", width=10, height=2)
A8 = Button(root, text="CLOSE 1", width=10, height=2, command=lambda: moveIncrement(3, 1))
A9 = Button(root, text="CLOSE 10", width=10, height=2, command=lambda: moveIncrementX10(3, 1))

B0 = Button(root, text="LEFT", width=10, height=2, command=lambda: moveIncrement(0, 1))
B2 = Button(root, text="RIGHT", width=10, height=2, command=lambda: moveIncrement(0, 0))
B3 = Label(root, text="SERVO 1 U/D", width=12, height=2)
B4 = leftServo = Tkinter.Label(None, text=currPositions[1], font=('Times', '12'), fg='blue')
B5 = Button(root, text="JUMP TO:", width=10, height=2, command=lambda: moveButton(B6, 1))
B6 = Entry(root, width=10)
B6.insert(END, "90")
B8 = Button(root, text="OPEN 1", width=10, height=2, command=lambda: moveIncrement(3, 0))
B9 = Button(root, text="OPEN 10", width=10, height=2, command=lambda: moveIncrementX10(3, 0))

C1 = Button(root, text="BACKWARDS", width=10, height=2, command=lambda: moveIncrement(2, 0))
C3 = Label(root, text="SERVO 2 F/B", width=12, height=2)
C4 = rightServo = Tkinter.Label(None, text=currPositions[2], font=('Times', '12'), fg='blue')
C5 = Button(root, text="JUMP TO:", width=10, height=2, command=lambda: moveButton(C6, 2))
C6 = Entry(root, width=10)
C6.insert(END, "90")
C7 = Label(root, text="ARM ->", width=10, height=2)
C8 = Button(root, text="UP 1", width=10, height=2, command=lambda: moveIncrement(1, 1))
C9 = Button(root, text="UP 10", width=10, height=2, command=lambda: moveIncrementX10(1, 1))

D3 = Label(root, text="SERVO 3 O/C", width=12, height=2)
D4 = clawServo = Tkinter.Label(None, text=currPositions[3], font=('Times', '12'), fg='blue')
D5 = Button(root, text="JUMP TO:", width=10, height=2, command=lambda: moveButton(D6, 3))
D6 = Entry(root, width=10)
D6.insert(END, "35")
D8 = Button(root, text="DOWN 1", width=10, height=2, command=lambda: moveIncrement(1, 0))
D9 = Button(root, text="DOWN 10", width=10, height=2, command=lambda: moveIncrementX10(1, 0))

E0 = Label(root, text="ALL SERV", width=10, height=2)
E1 = Button(root, text="RESTART", width=10, height=2, command=lambda: resetButtonAllServ(0, 1, 2, 3, 1, 1, 1, 1))
E4 = Label(root, text="L / R   F / B", width=10, height=2)
E5 = Button(root, text="RESTART", width=10, height=2, command=lambda: resetButtonLRFB(0, 2, 1, 1))
E7 = Label(root, text="UP / DOWN", width=10, height=2)
E8 = Button(root, text="RESTART", width=10, height=2, command=lambda: resetButtonUpDown(1, 1))

A1.grid(row=0, column=1)
A3.grid(row=0, column=3)
A4.grid(row=0, column=4)
A5.grid(row=0, column=5)
A6.grid(row=0, column=6)
A7.grid(row=0, column=7)
A8.grid(row=0, column=8)
A9.grid(row=0, column=9)

B0.grid(row=1, column=0)
B2.grid(row=1, column=2)
B3.grid(row=1, column=3)
B4.grid(row=1, column=4)
B5.grid(row=1, column=5)
B6.grid(row=1, column=6)
B8.grid(row=1, column=8)
B9.grid(row=1, column=9)

C1.grid(row=2, column=1)
C3.grid(row=2, column=3)
C4.grid(row=2, column=4)
C5.grid(row=2, column=5)
C6.grid(row=2, column=6)
C7.grid(row=2, column=7)
C8.grid(row=2, column=8)
C9.grid(row=2, column=9)

D3.grid(row=3, column=3)
D4.grid(row=3, column=4)
D5.grid(row=3, column=5)
D6.grid(row=3, column=6)
D8.grid(row=3, column=8)
D9.grid(row=3, column=9)

E0.grid(row=4, column=0)
E1.grid(row=4, column=1)
E4.grid(row=4, column=4)
E5.grid(row=4, column=5)
E7.grid(row=4, column=7)
E8.grid(row=4, column=8)

def moveIncrement(servo, direction):
    if direction == 1:
        angle = currPositions[servo] + 1
    else:
        angle = currPositions[servo] - 1
    move(servo, angle)


def moveIncrementX10(servo, direction):
    if direction == 1:
        angle = currPositions[servo] + 10
    else:
        angle = currPositions[servo] - 10
    move(servo, angle)

def refreshLabels():
    middleServo.config(text=currPositions[0])
    leftServo.config(text=currPositions[1])
    rightServo.config(text=currPositions[2])
    clawServo.config(text=currPositions[3])

def move(servo, angle):
    if (0 <= angle <= 180):
        ser.write(chr(servo))
        ser.write(chr(angle))
        currPositions[servo] = angle
        refreshLabels()
    else:
        print(angle, ": Servo angle must be an integer between 0 and 180.\n")

def moveButton(x, servo):
    move(servo, int(x.get()))

def resetButtonAllServ (servo0, servo1, servo2, servo3, direction0, direction1, direction2, direction3):
    if direction0 == 1:
        angleA = 90
        move(servo0, angleA)
    if direction1 == 1:
        angleB = 90
        move(servo1, angleB)
    if direction2 == 1:
        angleC = 90
        move(servo2, angleC)
    if direction3 == 1:
        angleD = 35
        move(servo3, angleD)

def resetButtonLRFB (servo0, servo1, direction0, direction1):
    if direction0 == 1:
        angleA = 90
        move(servo0, angleA)
    if direction1 == 1:
        angleB = 90
        move(servo1, angleB)

def resetButtonUpDown (servo0, direction0):
    if direction0 == 1:
        angleA = 90
        move(servo0, angleA)



root.mainloop()
