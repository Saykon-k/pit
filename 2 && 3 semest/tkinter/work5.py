import tkinter
from tkinter import *
from tkinter import messagebox as mb


class gui:

    def __init__(self):
        self.main_window = Tk()
       
        self.rd_btn_frame = Frame(self.main_window)
        self.entry_frame = Frame(self.main_window)
        self.cmn_btn_frame = Frame(self.main_window)


        self.radio_var = IntVar()
        self.radio_var.set(0)

        self.rd1_btn = Radiobutton(self.rd_btn_frame, text='Дневное время (6:00 - 17:59)',
                                           variable=self.radio_var, value=1)
        self.rd2_btn = Radiobutton(self.rd_btn_frame, text='Вечернее время (18:00 - 23:59)',
                                           variable=self.radio_var, value=2)
        self.rd3_btn = Radiobutton(self.rd_btn_frame, text='Непиковый период (00:00 - 5:59)',
                                           variable=self.radio_var, value=3)

        self.rd1_btn.pack()
        self.rd2_btn.pack()
        self.rd3_btn.pack()

        # 2 фрейм
        self.entry = Entry(self.entry_frame)
        self.entry_name = Label(self.entry_frame, text='Введите количество минут:')
        
        self.entry_name.pack(side=LEFT)
        self.entry.pack(side=RIGHT)

        # 3 фрейм

        self.run_btn = Button(self.cmn_btn_frame, text='Показать стоимость', command=self.show)
        self.quit_btn = Button(self.cmn_btn_frame, text='Выйти', command=self.main_window.destroy)

        self.run_btn.pack(side=RIGHT)
        self.quit_btn.pack(side=LEFT)

        self.rd_btn_frame.pack()
        self.entry_frame.pack()
        self.cmn_btn_frame.pack()

        mainloop()

    def show(self):
        values = {1: 10, 2: 12, 3: 5}
        if self.entry.get().isdigit() : 
            mb.showinfo('Общая стоимость', f'Ваши затраты = ${values[self.radio_var.get()] * int(self.entry.get()) * 0.01}')
        else:
            mb.showinfo('Сообщение об ошибке' , ' введены некорректные данные')
        

my_gui = gui()
