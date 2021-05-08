from tkinter import *
import user_data as us
import copy
import backend_kurse_work as bk
class Service(object):
    global user
    def __init__(self):

        self.window_for_input_data_connection = Tk()
        self.window_for_input_data_connection.title("Добро пожаловать в приложение PythonRu")
        self.window_for_input_data_connection.geometry('800x600')
        self.lg_connection = Label(self.window_for_input_data_connection,
                                   text="Введите номера,\n которые связаны с новой работой через запятую\n(если работа несвязана ни с чем, то введите '-1'")
        self.lg_connection.grid(column=0, row=0)
        self.txt_connection = Entry(self.window_for_input_data_connection, width=50)
        self.txt_connection.grid(column=1, row=0)

        self.lg_connection_work_time_normal = Label(self.window_for_input_data_connection,
                                                    text="Введите обычное время работы.")
        self.lg_connection_work_time_normal.grid(column=0, row=1)
        self.txt_connection_work_time_normal = Entry(self.window_for_input_data_connection, width=50)
        self.txt_connection_work_time_normal.grid(column=1, row=1)

        self.lg_connection_work_time_speed = Label(self.window_for_input_data_connection,
                                                   text="Введите минимальное время работы.")
        self.lg_connection_work_time_speed.grid(column=0, row=2)
        self.txt_connection_work_time_speed = Entry(self.window_for_input_data_connection, width=50)
        self.txt_connection_work_time_speed.grid(column=1, row=2)

        self.lg_connection_alfa = Label(self.window_for_input_data_connection,
                                        text="Введите коэффицент замедления/ускорения.")
        self.lg_connection_alfa.grid(column=0, row=3)
        self.txt_lg_connection_alfa = Entry(self.window_for_input_data_connection, width=50)
        self.txt_lg_connection_alfa.grid(column=1, row=3)

        self.btn_for_input_data_connection = Button(self.window_for_input_data_connection, text="Ввести данные.",
                                                    command=self.get_data_for_user_add_work)
        self.btn_for_input_data_connection.grid(column=0, row=4)
        # window_for_input_data_connection.mainloop()

    def get_data_for_user_add_work(self):
        if self.txt_connection.get() != '' and self.txt_connection_work_time_normal.get() != '' \
                and self.txt_connection_work_time_speed.get() != '' and self.txt_lg_connection_alfa.get() != '':
            self.add_to_main_to_main_user_connection()
            self.add_to_main_user_time_normal()
            self.add_to_main_user_time_faster()
            self.add_to_main_user_alfas_for_work()
            print(user.connections)
            print(user.time_normal)
            print(user.time_faster)
            print(user.alfas_for_work)
            self.window_for_input_data_connection.destroy()

        else:
            print('нет')


    def add_to_main_to_main_user_connection(self):

        prom = []
        if self.txt_connection.get()[0] != '-':
            for i in self.txt_connection.get().split(','):
                prom.append(int(i))
        else:
            prom.append(-1)
        user.connections.append(copy.deepcopy(prom))

    def add_to_main_user_time_normal(self):
        user.time_normal.append(int(self.txt_connection_work_time_normal.get()))

    def add_to_main_user_time_faster(self):
        user.time_faster.append(int(self.txt_connection_work_time_speed.get()))

    def add_to_main_user_alfas_for_work(self):
        user.alfas_for_work.append(float(self.txt_lg_connection_alfa.get()))


def clicked():
    global connection_window
    connection_window = Service()

def get_all_data_for_test():
    bk.main(user.connections,user.time_normal,user.time_faster,user.alfas_for_work,
            int(lg_money_data.get()),
            int(lg_max_work_data.get()),
            int(lg_min_work_data.get()),lg_file_data.get())


global connection_window
global user

user = us.user_data()
window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('1000x650')

btn = Button(window, text="Добавить новую работу.", command=clicked)
btn.grid(column=0, row=0)

lg_min_work = Label(window, text="Введите минимальное время работы.")
lg_min_work.grid(column=0, row=1)
lg_min_work_data = Entry(window, width=25)
lg_min_work_data.grid(column=1, row=1)

lg_max_work = Label(window, text="Введите максимальное время работы.")
lg_max_work.grid(column=0, row=2)
lg_max_work_data = Entry(window, width=25)
lg_max_work_data.grid(column=1, row=2)

lg_money = Label(window, text="Введите количество средств, которыми располагаете.")
lg_money.grid(column=0, row=3)
lg_money_data = Entry(window, width=25)
lg_money_data.grid(column=1, row=3)

lg_file = Label(window, text="Напишите название файла")
lg_file.grid(column=0, row=4)
lg_file_data = Entry(window, width=25)
lg_file_data.grid(column=1, row=4)

btn_for_input_data_connection = Button(window, text="Ввести данные.",
                                                    command=get_all_data_for_test)
btn_for_input_data_connection.grid(column=0, row=4)


window.mainloop()