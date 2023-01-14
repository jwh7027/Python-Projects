import random
from tkinter import *

def update(): #게임
    global num
    global try_count

    try_count += 1

    user_input = int(display.get())
    
    if (user_input > num):
       label["text"] = f"{user_input}보다 작습니다."
    elif(user_input < num):
       label["text"] = f"{user_input}보다 큽니다."
    else:
        label["text"] = f"{num}을 {try_count}번 만에 맞췄습니다."

def reset():
   global num
   global try_count
   label["text"] = f"1이상 100이하 자연수를 맞춰보세요."
   try_count = 0
   num = random.randint(1,101)
   display.delete(0,END)

##gui
num = random.randint(1,101)
try_count = 0

window = Tk()
window.title("Guess Number")

display = Entry (window, width= 5,justify=CENTER,font=("Arial",25))
button1 = Button(window, text="Enter", width=20,height=1,font=("Arial",10),command=update)
label = Label(window, text="1이상 100이하 자연수를 맞춰보세요",width=30,height=1,font=("System",20))
button2 = Button(window, text="다시하기", width=15,height=1,font=("Arial",10),command=reset)
button3 = Button(window, text="종료하기", width=15,height=1,font=("Arial",10),command=exit)
        
display.pack(fill=BOTH,expand=True)   
button1.pack()
label.pack(fill=BOTH,expand=True)
button2.pack(side=LEFT)
button3.pack(side=RIGHT)
##실행
window.mainloop()