from tkinter import *
import datetime
import time
from playsound import playsound

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("Alarm set for date:",date)
        print(" and time: ", now)
        if now == set_alarm_timer:
            print("Wake up and Conquer!!")
            playsound('morning_alarm.mp3')
        break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()
clock.title("Alarm")
clock.grid()
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="purple",bg="white",font="Times").grid(column=2, row=0)
addTime = Label(clock,text = "Hour  Min   Sec:  ",font=60).grid(column=0, row=2)
setYourAlarm = Label(clock,text = "Set time",fg="blue",font=("Times",10,"bold")).grid(column=0, row=1)
# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()
#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).grid(column=1, row=2)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).grid(column=2, row=2)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).grid(column=3, row=2)
#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="black",width = 10,command = actual_time).grid(column=2, row=3)
clock.mainloop()