from sympy import Symbol, Derivative
from tkinter import *
# x+(3*y*z)
x=Symbol('x')
y=Symbol('y')
z=Symbol('z')
class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Expression')
        self.lbl2=Label(win,text='Levels')
        self.lbl3=Label(win, text='Result')
        self.t1=Entry(bd=3)
        self.t2=Entry(bd=3)
        self.t3=Text(win, height = 5,width = 25,bg = "light cyan")
        self.btn2=Button(win, text='Result')
        self.lbl1.place(x=100, y=50)
        self.lbl2.place(x=100, y=100)
        self.t1.place(x=200, y=50,width=300)
        self.t2.place(x=200, y=100,width=300)
        self.b2=Button(win, text='Result')
        self.b2.bind('<Button-1>', self.calculate)
        self.b2.place(x=200, y=150)
        self.lbl3.place(x=100, y=250)
        self.t3.place(x=200, y=200,width=300,height=200)

    def calculate(self, event):
        self.t3.delete('1.0', 'end')
        expression=str(self.t1.get())
        # print("level :0 "+str(expression.split(' ')))
        self.t3.insert(END, "level :0 "+str(expression.split(' '))+'\n')
        list=expression.split('+')
        # print("level :1 "+str(list))
        self.t3.insert(END,"level :1 "+str(list)+ '\n')
        sample=[]
        levels=int(self.t2.get())
        for j in range(1,levels):
            sample=[]
            for i in list:
                dfx= Derivative(i, x).doit()
                dfy= Derivative(i, y).doit()
                dfz= Derivative(i, z).doit()
                if dfx!=0:
                    sample.append(dfx)
                if dfy!=0:
                    sample.append(dfy)
                if dfz!=0:
                    sample.append(dfz)
            # print("level :"+str(j+1) +" "+str(sample))
            list=sample
            self.t3.insert(END,"level :"+str(j+1)+" "+str(sample)+'\n')
        
window=Tk()
mywin=MyWindow(window)
window.title('Calculator')
window.geometry("700x500+10+10")
window.mainloop()