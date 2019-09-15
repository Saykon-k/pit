import tkinter
from tkinter import *

class gui:

    def __init__(self):
        self.check = 1 

        self.main_window = Tk()
        self.main_window.title("work1")
        self.main_window.geometry("450x370")
        
        
        
        self.only_frame = Frame()
        self.bottom_frame = Frame()
        
        self.only_frame.pack()

        self.data = StringVar()
        self.info_label = Label(self.only_frame,textvariable=self.data, justify='left')
        self.info_label.pack(side='left')
        
        
        self.show_button = Button(self.bottom_frame, text='Показать данные', command=self.show)
        self.quit_button = Button(self.bottom_frame, text='Выход', command=self.main_window.destroy)
 
        self.quit_button.pack(side='left')
        self.show_button.pack(side='right')
        
      
        self.bottom_frame.pack()
        
        
        tkinter.mainloop()
    
    
    def show(self):
        if self.check == 1 : 
            self.data.set('Стивен Маркус\n274 Бейли\nУэйнзвилль, Северная Каролина 2799999')
            self.check=0
        else:
            self.data.set('')
            self.check=1
        

my_gui = gui()
