from tkinter import *
import time
import serial

def cronometro(a):
    if a==1:
        start=0.0
        elapsedtime=0.0
        x = ser.readline()
        print("Inicio!=" + str(x))

        start = time.time()-elapsedtime

        x = ser.readline(1)
        print("Final!=" + str(x))
        elapsedtime = time.time()-start
        minutes = int(elapsedtime/60)
        seconds = int(elapsedtime- minutes*60)
        hseconds = int((elapsedtime - minutes*60.0 - seconds)*100)

        miLabel2 = Label(miFrame,text=str(minutes)+":"+str(seconds)+":"+str(hseconds),bg="black",fg="white",font=("Helvetica", 100))
        miLabel2.place(x=300,y=300)


ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM3'
ser.open()

root=Tk()

miFrame=Frame(root,width=960,height=540)
miFrame.pack()

Imagen = PhotoImage(file="./images/hack.png")
miLabelImage = Label(miFrame,image=Imagen)
miLabelImage.pack()

miLabel1 = Label(miFrame,text="UDENAR\n IEEE",bg="black",fg="white",font=("Helvetica", 60))
miLabel1.place(x=320,y=20)

Button(root, text='Start', command=cronometro(1)).pack(side=LEFT)
root.mainloop()
