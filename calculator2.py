from tkinter import *
from tkinter import ttk
import tkinter


HEIGHTBTN = 50
WIDTHBTN = 68

class CalcButton(ttk.Frame):
    def __init__(self, parent, text, command, wbtn=1, hbtn=1):
        ttk.Frame.__init__(self, parent, width=wbtn*WIDTHBTN, height=hbtn*HEIGHTBTN)

        self.pack_propagate(0)
        '''
        st = ttk.Style()
        st.theme_use('alt')
        st.configure('my.TButton', font='Helvetica 16', background="red")
        '''
        self.__btn = ttk.Button(self, text=text, command = command)
        self.__btn.pack(fill=BOTH, expand=True)
        
class Display(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=4*WIDTHBTN, height=HEIGHTBTN)
        
        self.pack_propagate(0)

        s = ttk.Style()
        s.theme_use('alt')
        s.configure('my.TLabel', font='Helvetica 24')

        self.__lbl = ttk.Label(self, text="_", style='my.TLabel', anchor=E, background='black', foreground='white')
        self.__lbl.pack(side=TOP, fill=BOTH, expand=True)



class Selector(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        self.pack_propagate(0)

        self.__lblA = ttk.Radiobutton(self, text="A", value=1, command=None)
        self.__lblA.pack(side=TOP, fill=BOTH, expand=True)

        self.__lblR = ttk.Radiobutton(self, text="R", value=1, command=None)
        self.__lblR.pack(side=TOP, fill=BOTH, expand=True)

class Calculator(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        self.display = Display(self)
        self.display.grid(column=0, row=0, columnspan=5)

        self.buttonAC = CalcButton(self, text="AC", command=None, wbtn=3)
        self.buttonAC.grid(column=0, row=1, columnspan=3)
        self.buttonDiv = CalcButton(self, text="÷", command=None)
        self.buttonDiv.grid(column=3, row=1)
        
        self.buttonC = CalcButton(self, text="C", command=None)
        self.buttonC.grid(column=0, row=2,)
        self.buttonD = CalcButton(self, text="D", command=None)
        self.buttonD.grid(column=1, row=2,)
        self.buttonM = CalcButton(self, text="M", command=None, hbtn=3)
        self.buttonM.grid(column=2, row=2, rowspan=3)
        self.buttonMul = CalcButton(self, text="x", command=None)
        self.buttonMul.grid(column=3, row=2)
        
        self.buttonX = CalcButton(self, text="X", command=None)
        self.buttonX.grid(column=0, row=3)
        self.buttonL = CalcButton(self, text="L", command=None)
        self.buttonL.grid(column=1, row=3)
        self.buttonSub = CalcButton(self, text="-", command=None)
        self.buttonSub.grid(column=3, row=3)
        
        self.buttonI = CalcButton(self, text="I", command=None)
        self.buttonI.grid(column=0, row=4)
        self.buttonV = CalcButton(self, text="V", command=None)
        self.buttonV.grid(column=1, row=4)
        self.buttonAdd = CalcButton(self, text="+", command=None)
        self.buttonAdd.grid(column=3, row=4)
        
        self.buttonEqu = CalcButton(self, text="=", command=None, wbtn=2)
        self.buttonEqu.grid(column=2, row=5, columnspan=2)
        
        self.selector = Selector(self)
        self.selector.grid(column=0, row=5)