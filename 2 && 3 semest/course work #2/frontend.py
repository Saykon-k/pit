from tkinter import *
import numpy as np
import tkinter.messagebox as mb
import backend as kent

dct = {}
dct_pocva = {}
dct_pocva1 = {}
reds = []
vid = []
food_amount = []
geom = []

class fun():
    def __init__(self):
        self.Alpocva = []
        self.Alpole = []
        self.Alplants = []
        
        global mainz
        self.mainz = Tk()
        self.mainz.title('Размеры поля')
        self.mainz.geometry('300x250')

        frame_big = Frame(self.mainz)
        frame_big.place(relx=0,rely=0,relheight=1,relwidth=1)

        lab1 = Label(self.mainz, text='Введите размеры поля:',
                      font='georgia 14')
        lab1.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.2)

        labx = Label(self.mainz, text='x',
                      font='georgia 25')
        labx.place(relx=0.45,rely=0.4,relwidth=0.1,relheight=0.2)

        self.entryx = Entry(self.mainz,font=40)
        self.entryx.place(relx=0.1,rely=0.4,relwidth=0.3,relheight=0.2)

        self.entryy = Entry(self.mainz,font=40)
        self.entryy.place(relx=0.6,rely=0.4,relwidth=0.3,relheight=0.2)

        self.ok_button = Button(frame_big, text='ok',
                           font='georgia 14',command=lambda:self.func())
        self.ok_button.place(relx=0.2, rely=0.75,
                           relwidth=0.6, relheight=0.2)

        self.mainz.mainloop()

    def func(self):

        self.bul = 0
        
        self.root = Toplevel(self.mainz)
        self.root.title('Новая жизнь')

        geom = [int(self.entryx.get()),int(self.entryy.get())]

        canvas = Canvas(self.root, height=600,width=1000)
        canvas.pack()
        
        self.frame = Frame(self.root)
        self.frame.place(relx=0,rely=0,relwidth=0.6,relheight=1)

        frame_main = Frame(self.root)
        frame_main.place(relx=0.6,rely=0,relwidth=0.3,relheight=0.05)
                
        label = Label(frame_main, text='Введите параметры растений',
                      font='georgia 14')
        label.place(relwidth=1,relheight=1)
        
        frame_1 = Frame(self.root)
        frame_1.place(relx=0.6,rely=0.05,relwidth=0.15,relheight=0.6)

        frame_2 = Frame(self.root)
        frame_2.place(relx=0.75,rely=0.05,relwidth=0.15,relheight=0.6)

        frame_3 = Frame(self.root)
        frame_3.place(relx=0.6,rely=0.65,relwidth=0.3,relheight=0.35)


        frame_quit = Frame(self.root)
        frame_quit.place(relx=0.9,rely=0,relwidth=0.1,relheight=1)


        label_1 = Label(frame_1, text='Вид 1',font='georgia 14')
        label_1.place(rely=0.05,relwidth=1,relheight=0.1)

        label_2 = Label(frame_2, text='Вид 2',font='georgia 14')
        label_2.place(rely=0.05,relwidth=1,relheight=0.1)

        massa1 = Label(frame_1,text='Масса:',font='georgia 14')
        massa1.place(relx=0.05,rely=0.2)

        self.massa1e = Entry(frame_1,font=40)
        self.massa1e.place(relx=0.5,rely=0.2,relwidth=0.3,relheight=0.08)

        massa2 = Label(frame_2,text='Масса:',font='georgia 14')
        massa2.place(relx=0.05,rely=0.2)

        self.massa2e = Entry(frame_2,font=40)
        self.massa2e.place(relx=0.5,rely=0.2,relwidth=0.3,relheight=0.08)

        eat1 = Label(frame_1,text='Ест за ход:',font='georgia 14')
        eat1.place(relx=0.05,rely=0.35)

        self.eat1e = Entry(frame_1,font=40)
        self.eat1e.place(relx=0.72,rely=0.35,relwidth=0.23,relheight=0.08)

        eat2 = Label(frame_2,text='Ест за ход:',font='georgia 14')
        eat2.place(relx=0.05,rely=0.35)

        self.eat2e = Entry(frame_2,font=40)
        self.eat2e.place(relx=0.72,rely=0.35,relwidth=0.23,relheight=0.08)

        life1 = Label(frame_1,text='Здоровье:',font='georgia 14')
        life1.place(relx=0.05,rely=0.5)

        self.life1e = Entry(frame_1,font=40)
        self.life1e.place(relx=0.7,rely=0.5,relwidth=0.25,relheight=0.08)

        life2 = Label(frame_2,text='Здоровье:',font='georgia 14')
        life2.place(relx=0.05,rely=0.5)

        self.life2e = Entry(frame_2,font=40)
        self.life2e.place(relx=0.7,rely=0.5,relwidth=0.25,relheight=0.08)

        reprod11 = Label(frame_1,text='Размножается',font='georgia 13')
        reprod11.place(relx=0.05,rely=0.65)

        reprod12 = Label(frame_1,text='каждые',font='georgia 12')
        reprod12.place(relx=0.05,rely=0.75,relwidth=0.4)

        reprod13 = Label(frame_1,text='ходов',font='georgia 12')
        reprod13.place(relx=0.68,rely=0.75,relwidth=0.31)

        self.reprod1e = Entry(frame_1,font=40)
        self.reprod1e.place(relx=0.47,rely=0.75,relwidth=0.2,
                            relheight=0.08)

        reprod21 = Label(frame_2,text='Размножается',font='georgia 13')
        reprod21.place(relx=0.05,rely=0.65)

        reprod22 = Label(frame_2,text='каждые',font='georgia 12')
        reprod22.place(relx=0.05,rely=0.75,relwidth=0.4)

        reprod23 = Label(frame_2,text='ходов',font='georgia 12')
        reprod23.place(relx=0.68,rely=0.75,relwidth=0.31)

        self.reprod2e = Entry(frame_2,font=40)
        self.reprod2e.place(relx=0.47,rely=0.75,relwidth=0.2,
                            relheight=0.08)

        child1 = Label(frame_1,text='Число семян:',font='georgia 13')
        child1.place(relx=0.05,rely=0.9)

        self.child1e = Entry(frame_1,font=40)
        self.child1e.place(relx=0.77,rely=0.9,relwidth=0.2,
                           relheight=0.08)

        child2 = Label(frame_2,text='Число семян:',font='georgia 13')
        child2.place(relx=0.05,rely=0.9)

        self.child2e = Entry(frame_2,font=40)
        self.child2e.place(relx=0.77,rely=0.9,relwidth=0.2,
                           relheight=0.08)


        button2 = Button(frame_3, text='ПОДТВЕРДИТЬ', bg='#00adad',
                         font='georgia 14',command=self.confirm2)
        button2.place(relx=0.05,rely=0.1,relwidth=0.5,relheight=0.3)

        change = Button(frame_quit, text='Сменить\nрежим',
                        font='georgia 14',
                        command=lambda:self.change_mode())
        change.place(rely=0.5,relwidth=1,relheight=0.1)

        show_pole = Button(frame_quit, text='Перейти\nк полю\nресурсов',
                           font='georgia 14',command=lambda:self.pole())
        show_pole.place(rely=0.65,relwidth=1,relheight=0.2)

        start = Button(frame_3, text='СТАРТ',
                       font='georgia 14',
                       command=lambda:self.main(dct, vid, dct_pocva1,
                                                food_amount, geom))
        start.place(relx=0.05,rely=0.5,relwidth=0.9,relheight=0.4)

        steps = Button(frame_3, text='100',
                       font='georgia 14',command=lambda:self.step(vid))
        steps.place(relx=0.55,rely=0.1,relwidth=0.5,relheight=0.3)
      
        bquit = Button(frame_quit,text='выйти',
                         font='georgia 14',command=self.dstr)
        bquit.place(rely=0.9,relwidth=1,relheight=0.1)
      

        self.btn = [[0 for x in range(int(self.entryx.get()))]
                       for x in range(int(self.entryy.get()))]
        
        for y in range(int(self.entryy.get())):
             for x in range(int(self.entryx.get())):
                 self.btn[y][x] = Button(
                                     self.frame,
                                     command=lambda x1=x, y1=y:
                                     self.color_change(x1,y1))
                 self.btn[y][x].place(relx=x/int(self.entryx.get()),
                                      rely=y/int(self.entryy.get()),
                                      relwidth=1/int(self.entryx.get()),
                                      relheight=1/int(self.entryy.get()))
       

        self.mainz.withdraw()

        mb.showinfo('Добро пожаловать!',
                    'Сейчас вы находитесь в режиме "Симбиоз".'
                    + '\nДля изменений нажмите "Смена режима"')
        
    def step(self, vid):
        
        next_gen = []
        last_step = []
        
        for i in range(2):
            next_gen = kent.new_generation(self.Alplants, self.Alpole,
                                           vid, self.Alpocva)

            self.Alplants = next_gen[0]
            self.Alpocva = next_gen[2]
            self.Alpole = next_gen[1]
            
            if self.Alplants == []:
                break

        
        for i in range(len(next_gen[3])):
             if next_gen[3][i][2] == 0:
                self.lbl[next_gen[3][i][0]][next_gen[3][i][1]].config(
                                                      background="lime")
                    
             elif next_gen[3][i][2] == 1:
                self.lbl[next_gen[3][i][0]][next_gen[3][i][1]].config(
                                                      background="olive")
        
    def change_mode(self):
        if self.bul == 0:
            self.bul = 1
            mb.showinfo('Смена режима', 'Вы сменили режим на "Конкуренция"')
        else:
            self.bul = 0
            mb.showinfo('Смена режима', 'Вы сменили режим на "Симбиоз"')

    def confirm2(self):
        try:
            global vid
            if self.bul == 0:
                vid = [[int(self.massa1e.get
                            ()), int(self.eat1e.get
                            ()), int(self.life1e.get
                            ()), int(self.reprod1e.get
                            ()), int(self.child1e.get()), 0],
                            [int(self.massa2e.get
                            ()), int(self.eat2e.get
                            ()), int(self.life2e.get
                            ()), int(self.reprod2e.get
                            ()), int(self.child2e.get()), 1]]
            else:
                vid = [[int(self.massa1e.get
                            ()), int(self.eat1e.get
                            ()), int(self.life1e.get
                            ()), int(self.reprod1e.get
                            ()), int(self.child1e.get()), 1],
                            [int(self.massa2e.get
                            ()), int(self.eat2e.get
                            ()), int(self.life2e.get
                            ()), int(self.reprod2e.get
                            ()), int(self.child2e.get()), 1]]
            mb.showinfo('сумма2', vid)
        except:
            mb.showinfo('ошибка', 'введите корректные значения')


    def main(self, dct, vid, dct_pocva1, food_amount, geom):
        
        self.frame = Frame(self.root, bg='black')
        self.frame.place(relx=0, rely=0, relwidth=0.6, relheight=1)
        
        self.lbl = [[0 for x in range(int(self.entryx.get())+1)]
                       for x in range(int(self.entryy.get())+1)]
        
        for y in range(int(self.entryy.get())+1):
            for x in range(int(self.entryx.get())+1):
                self.lbl[y][x] = Label(self.frame,background="white")
                self.lbl[y][x].place(relx=x/(int(self.entryx.get())),
                                rely=y/(int(self.entryy.get())),
                                relwidth=1/(int(self.entryx.get())+1),
                                relheight=1/(int(self.entryy.get())+1))
                
        pole = np.zeros((geom[1],geom[0]))
        pole_pocva = np.zeros((geom[1],geom[0]))
     
        real_dates = kent.conver_data(dct, dct_pocva1, pole, pole_pocva,
                                      food_amount, vid)

        plants = real_dates[0]
        pole_pocva = real_dates[1]
        pole = real_dates[2]

        dct = {}
        
        for i in range(2):
            next_gen = kent.new_generation(plants, pole, vid, pole_pocva)

            plants = next_gen[0]
            pole_pocva = next_gen[2]
            pole = next_gen[1]

            if plants == []:
                break
                            
        dct = {}
            
        for i in range(len(next_gen[3])):
             if next_gen[3][i][2] == 0:
                self.lbl[next_gen[3][i][0]][next_gen[3][i][1]].config(
                                                       background="lime")
                    
             elif next_gen[3][i][2] == 1:
                self.lbl[next_gen[3][i][0]][next_gen[3][i][1]].config(
                                                       background="olive")
                
        self.Alplants = plants
        self.Alpocva = pole_pocva
        self.Alpole = pole
        

    def dstr(self):
        self.root.destroy()
        self.mainz.destroy()
        
# отдельное окно ресурсов
    def pole(self):

        self.window = Toplevel(self.root)
        self.window.title('Поле ресурсов')
        
        canvas = Canvas(self.window, height=600,width=900)
        canvas.pack()

        frame = Frame(self.window)
        frame.place(relx=0,rely=0,relwidth=0.67,relheight=1)

        frame1 = Frame(self.window)
        frame1.place(relx=0.67,rely=0,relwidth=0.33,relheight=0.55)

        frame2 = Frame(self.window)
        frame2.place(relx=0.67,rely=0.55,relwidth=0.165,relheight=0.05)

        frame3 = Frame(self.window)
        frame3.place(relx=0.835,rely=0.55,relwidth=0.165,relheight=0.05)

        frame_pole = Frame(self.window)
        frame_pole.place(relx=0.67,rely=0.6,relwidth=0.33,relheight=0.1)

        frame_pole1 = Frame(self.window)
        frame_pole1.place(relx=0.67,rely=0.7,relwidth=0.165,relheight=0.2)

        frame_pole2 = Frame(self.window)
        frame_pole2.place(relx=0.835,rely=0.7,relwidth=0.165,relheight=0.2)

        frame_quit = Frame(self.window)
        frame_quit.place(relx=0.67,rely=0.9,relwidth=0.33,relheight=0.1)

        self.btn2 = [[0 for x in range(int(self.entryy.get()))]
                        for x in range(int(self.entryx.get()))] 
        for x in range(int(self.entryx.get())):
            for y in range(int(self.entryy.get())):
                self.btn2[x][y] = Button(frame,
                                         command=lambda x2=x, y2=y:
                                         self.color_change2(x2,y2))
                self.btn2[x][y].place(relx=x/int(self.entryx.get()),
                                      rely=y/int(self.entryy.get()),
                                      relwidth=1/int(self.entryx.get()),
                                      relheight=1/int(self.entryy.get()))

        lab = Label(frame1, text='Выберите две или три\nточки на поле, чтобы:',
                    font='georgia 14')
        lab.place(relx=0.1,rely=0.05,relheight=0.2)

        lab1 = Label(frame1,
                     text='После выделения области\nвыберите номер вида:',
                     font='georgia 14')
        lab1.place(relx=0.1,rely=0.8,relheight=0.2)

        but1 = Button(frame1,text='построить\nпрямоугольную область',
                         font='georgia 14',command=lambda:self.oblast())
        but1.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.2)

        but2 = Button(frame1,text='построить\nтреугольную область',
                         font='georgia 14',command=lambda:self.oblast3())
        but2.place(relx=0.1,rely=0.55,relwidth=0.8,relheight=0.2)

        b_vid1 = Button(frame2,text='вид 1',
                         font='georgia 14',command=lambda: self.vid1())
        b_vid1.place(relx=0.1,relwidth=0.8,relheight=1)

        b_pole = Label(frame_pole,text='Количество ресурса',
                         font='georgia 14')
        b_pole.place(relx=0.1,rely=0.5,relwidth=0.8,relheight=0.49)

        b_pole1 = Label(frame_pole1,text='вида 1:',
                         font='georgia 14')
        b_pole1.place(relx=0.1,rely=0,relwidth=0.5,relheight=0.2)

        b_pole2 = Label(frame_pole2,text='вида 2:',
                         font='georgia 14')
        b_pole2.place(relx=0.1,rely=0,relwidth=0.5,relheight=0.2)

        self.b_pole1e = Entry(frame_pole1)
        self.b_pole1e.place(relx=0.65,rely=0,relwidth=0.3,relheight=0.2)

        self.b_pole2e = Entry(frame_pole2)
        self.b_pole2e.place(relx=0.65,rely=0,relwidth=0.3,relheight=0.2)

        b_vid2 = Button(frame3,text='вид 2',
                         font='georgia 14',command=lambda: self.vid2())
        b_vid2.place(relx=0.1,relwidth=0.8,relheight=1)
    
        bquit = Button(frame_quit,text='закончить правку поля\nи выйти',
                         font='georgia 14',command=lambda: self.vixod())
        bquit.place(relx=0.2,relwidth=0.8,relheight=1)

    def vixod(self):
        global food_amount
        food_amount = [int(self.b_pole1e.get()),int(self.b_pole2e.get())]        
        self.window.destroy()

    def vid1(self):
        global dct_pocva
        for i in dct_pocva:
            dct_pocva[str(i)] = 0
            dct_pocva1[str(i)] = dct_pocva[str(i)]
        dct_pocva = {}

    def vid2(self):
        global dct_pocva
        for i in dct_pocva:
            dct_pocva[str(i)] = 1
            dct_pocva1[str(i)] = dct_pocva[str(i)]
        dct_pocva = {}

    def color_change2(self,x,y):
        self.btn2[x][y].config(bg="lime")
        reds.append([y,x])
        dct_pocva[str([y,x])] = -1


    def oblast(self):
        global reds
        for i in range(min([item[0] for item in reds[len(reds)-2:]]),
                       max([item[0] for item in reds[len(reds)-2:]])+1):
            for j in range(min([item[1] for item in reds[len(reds)-2:]]),
                           max([item[1] for item in reds[len(reds)-2:]])+1):
                self.btn2[j][i].config(bg="yellow")
                dct_pocva[str([i,j])] = -1
        reds = []

    def oblast3(self):
        global reds
        for i in range(min([item[0] for item in reds]),
                        max([item[0] for item in reds])+1):
            for j in range(min([item[1] for item in reds]),
                            max([item[1] for item in reds])+1):
                if ((reds[0][0] - i)*(reds[1][1]
                        - reds[0][1]) - (reds[1][0]
                        - reds[0][0])*(reds[0][1] - j)) > 0 and ((reds[1][0]
                        - i)*(reds[2][1] - reds[1][1]) - (reds[2][0]
                        - reds[1][0])*(reds[1][1] - j)) > 0 and ((reds[2][0]
                        - i)*(reds[0][1] - reds[2][1]) - (reds[0][0]
                        - reds[2][0])*(reds[2][1] - j)) > 0 or ((reds[0][0]
                        - i)*(reds[1][1]
                        - reds[0][1]) - (reds[1][0]
                        - reds[0][0])*(reds[0][1] - j)) < 0 and ((reds[1][0]
                        - i)*(reds[2][1] - reds[1][1]) - (reds[2][0]
                        - reds[1][0])*(reds[1][1] - j)) < 0 and ((reds[2][0]
                        - i)*(reds[0][1] - reds[2][1]) - (reds[0][0]
                        - reds[2][0])*(reds[2][1] - j)) < 0 or ((reds[0][0]
                        - i)*(reds[1][1]
                        - reds[0][1]) - (reds[1][0]
                        - reds[0][0])*(reds[0][1] - j)) == 0 or ((reds[1][0]
                        - i)*(reds[2][1] - reds[1][1]) - (reds[2][0]
                        - reds[1][0])*(reds[1][1] - j)) == 0 or ((reds[2][0]
                        - i)*(reds[0][1] - reds[2][1]) - (reds[0][0]
                        - reds[2][0])*(reds[2][1] - j)) == 0:
                    self.btn2[j][i].config(bg='blue')
                    dct_pocva[str([j,i])] = -1
        reds = []

# изменение цвета клеток основного поля
    def color_change(self,x,y):
        if str([y,x]) not in dct:
            dct[str([y,x])] = 2            
        if str([y,x]) in dct:
            if dct[str([y,x])] == 2:
                dct[str([y,x])] = 0
                self.btn[y][x].config(bg="lime")
            elif dct[str([y,x])] == 0:
                dct[str([y,x])] = 1
                self.btn[y][x].config(bg="olive")
            elif dct[str([y,x])] == 1:
                del dct[str([y,x])]
                self.btn[y][x].config(bg='SystemButtonFace')
fun()
