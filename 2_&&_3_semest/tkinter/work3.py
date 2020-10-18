import tkinter
from tkinter import *
class totalgui:

    def __init__(self):


        self.main_window = Tk()
        self.main_window.title("work3")
        self.main_window.geometry("450x200")

        
        self.fist_frame = Frame()
        self.second_frame = Frame()
        self.third_frame = Frame()
        self.bottom_frame = Frame()

          
        self.gallon_label = Label(self.fist_frame, text='Введите количество галлонов:')
        self.gallon_entry = Entry(self.fist_frame, width=16)

        self.gallon_label.pack(side='left')
        self.gallon_entry.pack(side='right')


        self.mile_label = Label(self.second_frame, text='Введите количество миль:')
        self.mile_entry = Entry(self.second_frame, width=16)
        
        self.mile_label.pack(side='left')
        self.mile_entry.pack(side='right')
        
        
        self.miles_label = Label(self.third_frame, text='Мили на галлон (MPG) =')
        self.value = StringVar()
        self.ans_label = Label(self.third_frame, textvariable=self.value)
        
        self.miles_label.pack(side='left')
        self.ans_label.pack(side='right')

        
        self.calc_button = Button(self.bottom_frame, text='Вычислить MPG', command=self.convert)
        self.quit_button = Button(self.bottom_frame, text='Выйти', command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='right')


        self.fist_frame.pack()
        self.second_frame.pack()
        self.third_frame.pack()
        self.bottom_frame.pack()


        mainloop()

        
    def convert(self):
        if self.gallon_entry.get().isdigit() and self.mile_entry.get().isdigit() :
            
            gallons = float(self.gallon_entry.get())
            miles = float(self.mile_entry.get())

            self.value.set(miles / gallons)
            
        else :
            
            self.value.set('неверные исходные данные')


conv = totalgui()
