from tkinter import *
from math import*



def plus():
    entry.insert(END,"+")
def equl():
    entry.insert(END, f"= {eval(entry.get())}")
def put10():
    entry.insert(END,"10")
def put100():
    entry.insert(END,"100")
    


def makeButton():
    button10 = Button(window, text= "10", command = put10, width=20, height=2  ).grid(row=1, column = 0, sticky = W, pady = 10)
    button100 = Button(window, text= "100", command = put100, width=20, height=2 ).grid(row=2, column = 0, sticky = W, pady = 10)
    buttonPlus = Button(window, text= "+", command = plus, width=20, height=2 ).grid(row=1, column = 1,  pady = 10)
    buttonEqul = Button(window, text= "=", command = equl, width=20, height=2 ).grid(row=2, column = 1,  pady = 10)
    

if __name__ == "__main__":
    window= Tk()
    entry = Entry(window, bg= "yellow")
    entry.grid(row = 0, columnspan=2 )
    makeButton()
    window.mainloop()
    
    
    
