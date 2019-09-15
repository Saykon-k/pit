from tkinter import *
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title("work4")
        self.main_window.geometry("450x370")
         
        self.top_frame = Frame(self.main_window)
        self.bottom_frame = Frame(self.main_window)
        
        self.cb_var1 = IntVar()
        self.cb_var2 = IntVar()
        self.cb_var3 = IntVar()
        self.cb_var4 = IntVar()
        self.cb_var5 = IntVar()
        self.cb_var6 = IntVar()
        self.cb_var7 = IntVar()
        
        self.cb1 = Checkbutton(self.top_frame,
                                       text='Замена масла - $30.00',
                                       variable=self.cb_var1 ,
                                       selectcolor = 'red',
                                        relief=RAISED,
                                       padx="-15"
                                       )
        
        self.cb2 = Checkbutton(self.top_frame,
                                       text='Cмазочные работы - $20.00',
                                       variable=self.cb_var2,
                                       relief=SUNKEN 
                                       )
        
        self.cb3 = Checkbutton(self.top_frame,
                                       text='Промывка радиатора $40.00',
                                       variable=self.cb_var3,
                                       relief=GROOVE 
                                       )
        
        self.cb4 = Checkbutton(self.top_frame,
                                       text='Замена жидкости в трансмиссии $100.00',
                                       variable=self.cb_var4
                                       )
        
        self.cb5 = Checkbutton(self.top_frame,
                                       text='Осмотр $35.00',
                                       variable=self.cb_var5
                                       )
        self.cb6 = Checkbutton(self.top_frame,
                                       text='Замена глушителя выхлопа $200.00',
                                       variable=self.cb_var6
                                       )
        
        self.cb7 = Checkbutton(self.top_frame,
                                       text='Перестановка шин $20.00',
                                       variable=self.cb_var7
                                       )

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()

        self.ok_button = Button(self.bottom_frame,
                                        text='check this out',
                                        command=self.total,
                                         padx="5", pady="5"
                                        )
        self.quit_button = Button(self.bottom_frame,
                                          text='Выйти',
                                 command=self.main_window.destroy,
                                          padx="15", pady="6"
                                          )

        self.ok_button.pack(side=RIGHT) 

        self.quit_button.pack(side=LEFT)

      
        self.top_frame.pack()
        self.bottom_frame.pack()

       
        mainloop()

    def total(self):
        self.total = 0
      
        if self.cb_var1.get() == 1:
            self.total += 30
            
        if self.cb_var2.get() == 1:
            self.total += 20
            
        if self.cb_var3.get() == 1:
            self.total += 40
            
        if self.cb_var4.get() == 1:
            self.total += 100
            
        if self.cb_var5.get() == 1:
            self.total += 35
            
        if self.cb_var6.get() == 1:
            self.total += 200
            
        if self.cb_var7.get() == 1:
            self.total += 20

        self.message = 'Ваши затраты : $' + str(self.total)

        tkinter.messagebox.showinfo('Выбор', self.message)

my_gui = MyGUI()
