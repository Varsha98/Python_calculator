from tkinter import *

#app=Tk()

def calci(source,side):
    obj = Frame(source,borderwidth=1,bd=4,bg="sky blue")
    obj.pack(side=side,expand=YES,fill=BOTH)
    return obj

def button (source,side,text,command=None):
    obj = Button(source, text=text,command=command)
    obj.pack(side=side, expand=YES, fill=BOTH)
    return obj

class app (Frame):
    def __init__(self):
        super(app, self).__init__()
        #Frame.__init(self)
        self.option_add('%font','arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Calculator')

        display = StringVar()
        Entry(self,relief=RIDGE,
              textvariable=display,justify='right',bd=30,
              bg="light blue").pack(side=TOP,expand=YES,fill=BOTH)
        for clearBut in (["CE"],["C"]):
            erase=calci(self,TOP)
            for ichar in clearBut:
                button(erase,LEFT,ichar,
                       lambda obj=display,
                              q=ichar:obj.set(''))
        for NumBut in ("789/", "456+", "123-", "0.+"):
            FunctionNum = calci(self,TOP)
            for iEquals in NumBut:
                button(FunctionNum, LEFT, iEquals,
                lambda  obj=display,q=iEquals:
                obj.set(obj.get()+q))
        EqualsButton=calci(self,TOP)
        for iEquals in '=':
            if iEquals=='=':
                btniEquals=button(EqualsButton,LEFT,iEquals)
                btniEquals.bind('<ButtonRelease-1>',
                lambda e, s=self,obj=display: s.cal(obj))

            else:
                btniEquals=button(EqualsButton,LEFT,iEquals,
                lambda obj=display,s='%s'%iEquals:obj.set(obj.get()+s))
    def cal(self,val):
        val.set(eval(val.get()))
if __name__ == '__main__':
    app().mainloop()

