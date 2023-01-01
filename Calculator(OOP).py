#OOP구조
from tkinter import *


class Calculator(Tk):

    button_texts = [
    ["^","C","CE","/"],
    ["7","8","9","*"],
    ["4","5","6","-"],
    ["1","2","3","+"],
    ["+/-","0",".","="],
]

    def __init__(self):
        super().__init__()

        self.title = ("Calculator")
        self.display = Entry (self,font=("Arial", 25),justify=RIGHT,width = 19 ,bg = "white")
        self.display.insert(END,"0")
        self.display.grid(row= 0 , column= 0 , columnspan= 4)

        for r , row in enumerate(Calculator.button_texts):
            for c , btn in enumerate(row):
                Button(
                    self,
                    text=btn,
                    font=("Arial", 25),
                    width=4,
                    height=1,
                    command= lambda key = btn : self.button_click(key),
                ).grid(row= r + 1,column= c, columnspan=1)
    
    def button_click(self,key):
        if key == "=":
            try:
                result = eval(self.display.get())
                s = str(result)
                self.display.delete(0,END)
            except:
                self.display.delete(0,END)
                self.display.insert(END,"ERROR")    
            else:
                self.display.insert(END,s)    

        elif key == "C": #clear
            self.display.delete(0,END)
        elif self.display.get() in ("0","ERROR"):
            self.display.delete(0,END)
            self.display.insert(END,key)
        elif key == "CE": #clear entry
            ce = self.display.get()
            x = ""
            for i in range(len(ce)-1):
                x += ce[i] 
            self.display.delete(0,END)
            self.display.insert(END,x) 
        elif key == "+/-": #change sign 
            chs = self.display.get()
            cs = int(chs) * -1
            self.display.delete(0,END)
            self.display.insert(END,cs)
        elif key == "^":
            key = "**"
            self.display.insert(END,key)         
        else:
            self.display.insert(END,key)




def main():
    Calculator().mainloop()

if __name__ == "__main__":
    main()