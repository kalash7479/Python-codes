from tkinter import *


class Window:

    def __init__(self):
        self.win = Tk()
        self.win.title("Calculator")
        self.win.geometry("700x250")

        self.txtbox1 = Entry(master=self.win, font=('consolas', 18, 'bold'), fg='sky blue')
        self.txtbox1.place(x=20, y=20, width=200, height=30)

        self.txtbox2 = Entry(master=self.win, font=('consolas', 18, 'bold'))
        self.txtbox2.place(x=240, y=20, width=200, height=30)

        self.txtbox3 = Entry(master=self.win, font=('consolas', 18, 'bold'))
        self.txtbox3.place(x=460, y=20, width=200, height=30)

        self.add = Button(master=self.win, text="+", font=('consolas', 18, 'bold'), command=self.Add)
        self.add.place(x=20, y=70, width=200, height=30)

        self.sub = Button(master=self.win, text="-",
                          font=('consolas', 18, 'bold'), command=self.Sub)
        self.sub.place(x=240, y=70, width=200, height=30)

        self.mul = Button(master=self.win, text="X",
                          font=('consolas', 18, 'bold'), command=self.Mul)
        self.mul.place(x=460, y=70, width=200, height=30)

        self.div = Button(master=self.win, text="/",
                          font=('consolas', 18, 'bold'), command=self.Div)
        self.div.place(x=20, y=120, width=200, height=30)

        self.moddiv = Button(master=self.win, text="//",
                          font=('consolas', 18, 'bold'), command=self.Moddiv)
        self.moddiv.place(x=240, y=120, width=200, height=30)

        self.mod = Button(master=self.win, text="%",
                          font=('consolas', 18, 'bold'), command=self.Mod)
        self.mod.place(x=460, y=120, width=200, height=30)

        self.clear = Button(master=self.win, text="Clear",
                          font=('consolas', 18, 'bold'), foreground='white', background="black", command =self.Clear)
        self.clear.place(x=240, y=170, width=150, height=30)

        self.win.mainloop()  # Hold the window

    def Clear(self):
        self.txtbox1.delete(0, 'end')
        self.txtbox2.delete(0, 'end')
        self.txtbox3.delete(0, 'end')

    def Add(self):
        n1 = int(self.txtbox1.get())
        n2 = int(self.txtbox2.get())
        n = n1+n2
        self.txtbox3.insert(0, n)

    def Sub(self):
        n1 = int(self.txtbox1.get())
        n2 = int(self.txtbox2.get())
        n = n1 - n2
        self.txtbox3.insert(0, n)

    def Mul(self):
         n1 = int(self.txtbox1.get())
         n2 = int(self.txtbox2.get())
         n = n1 * n2
         self.txtbox3.insert(0, n)

    def Div(self):
          n1 = int(self.txtbox1.get())
          n2 = int(self.txtbox2.get())
          n = n1 / n2
          self.txtbox3.insert(0, n)

    def Moddiv(self):
        n1 = int(self.txtbox1.get())
        n2 = int(self.txtbox2.get())
        n = n1 // n2
        self.txtbox3.insert(0, n)

    def Mod(self):
        n1 = int(self.txtbox1.get())
        n2 = int(self.txtbox2.get())
        n = n1 % n2
        self.txtbox3.insert(0, n)

if __name__ == '__main__':
            w = Window()