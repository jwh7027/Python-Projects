from tkinter import *
import tkinter as tk


#GUI
window = tk.Tk()
window.title = ("Calculator")
display = Entry (window,font=("Arial", 25),justify=RIGHT,width = 19 ,bg = "white")
display.insert(END,"0")
display.grid(row= 0 , column= 0 , columnspan= 4)

button_texts = [
    ["^","C","CE","/"],
    ["7","8","9","*"],
    ["4","5","6","-"],
    ["1","2","3","+"],
    ["+/-","0",".","="],
]

for r , row in enumerate(button_texts):
    for c , btn in enumerate(row):
        Button(
            window,
            text=btn,
            font=("Arial", 25),
            width=4,
            height=1,
            command= lambda key = btn : button_click(key),
        ).grid(row= r + 1,column= c, columnspan=1)


#버튼 이벤트
def button_click(key):
    if key == "=":
        try:
            result = eval(display.get())
            s = str(result)
            display.delete(0,END)
        except:
            display.delete(0,END)
            display.insert(END,"ERROR")    
        else:
            display.insert(END,s)    

    elif key == "C": #clear
        display.delete(0,END)
    elif display.get() in ("0","ERROR"):
        display.delete(0,END)
        display.insert(END,key)
    elif key == "CE": #clear entry
        ce = display.get()
        x = ""
        for i in range(len(ce)-1):
            x += ce[i] 
        display.delete(0,END)
        display.insert(END,x) 
    elif key == "+/-": #change sign 
        chs = display.get()
        cs = int(chs) * -1
        display.delete(0,END)
        display.insert(END,cs)
    elif key == "^":
        key = "**"
        display.insert(END,key)         
    else:
        display.insert(END,key)


#메인루프 실행
window.mainloop()