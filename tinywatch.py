# #!//Users/mahmood/Documents/projects/python-projects/apps/stopwatch/venv/bin/python
from tkinter import *
import time

root = Tk()
root.title('tinywatch')
root.iconbitmap('icon.ico')
root.geometry('180x80')

def update():
    label.config(text='New')

def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S") 
    month = time.strftime("%m")
    day = time.strftime("%d")
    year = time.strftime("%Y")
    weekday = time.strftime("%a")
    label.config(text=hour + ":" + minute + 
            ":" + second) 

    date.config(text=weekday + " " + 
            day + "/" + month 
            + "/" + year)


    label.after(1000, clock)

label = Label(root, text="", font=("Avenir", 24), fg='Black')
label.pack(pady=5)

date = Label(root, text="", font=("Avenir", 16), fg='Salmon')
date.pack()



clock()

root.mainloop()


