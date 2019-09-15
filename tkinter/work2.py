import tkinter
from tkinter import *

class gui:

    def __init__(self):

        self.main_window = Tk()
        self.main_window.title("work2")
        self.main_window.geometry("450x370")
        
        
        self.top_frame = Frame()
        self.bottom_frame = Frame()
        self.quit_frame = Frame()
        
        
        self.side = StringVar()
        self.side_label = Label(self.top_frame, textvariable=self.side)
        self.side_label.pack()
        
        
        self.btn1 = Button(self.bottom_frame, text='sinister', command= self.fun1)
        self.btn2 = Button(self.bottom_frame, text='dexter', command= self.fun2)
        self.btn3 = Button(self.bottom_frame, text='medium', command= self.fun3)
        self.quit = Button(self.quit_frame, text='exit', command=self.main_window.destroy)
        
        self.btn1.pack(side='left')
        self.btn2.pack(side='left')
        self.btn3.pack(side='left')
        self.quit.pack(side='left')
        
        self.top_frame.pack()
        self.quit_frame.pack()
        self.bottom_frame.pack()

        
        mainloop()
        
    def fun1(self):
        self.side.set('зловещий')
    def fun2(self):
        self.side.set('правый')
    def fun3(self):
        self.side.set('средний')

my_gui = gui()
