def __init__(self, parent, text, command, wbtn=1, hbtn=1):
        ttk.Frame.__init__(self, parent, width=wbtn*WIDTHBTN, height=hbtn*HEIGHTBTN)

        self.pack_propagate(0)

        self.__btn = ttk.Button(self)
        self.__btn.pack(side=TOP, fill=BOTH, expand=True)