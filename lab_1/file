from tkinter import *
from datetime import datetime
from tkinter import messagebox as mb
import winsound
import time
class clock:
    def __init__(self):
        self.mode = 0
        self.time = 0
        self.wid = Tk()

        self.only_frame = Frame()
        self.neonly_frame = Frame()

        self.timM = StringVar()
        self.timM.set("-1")
        self.timH = StringVar()
        self.timH.set("0")
        self.saveM=""
        self.saveH=""
        
        self.label = Label(self.only_frame, textvariable = self.timM)
        self.label1 = Label(self.only_frame , textvariable = self.timH)

        self.butM = Button(self.neonly_frame, text = "M", command = self.incM)
        self.butH = Button(self.neonly_frame, text = "H", command = self.incH)
        self.butA = Button(self.neonly_frame, text = "A", command = self.incA)
        
        self.label.after_idle(self.inc)

        self.label1.pack(side= LEFT)
        self.label.pack(side=LEFT)
        self.only_frame.pack()

        self.butH.pack(side = LEFT)
        self.butM.pack(side = LEFT)
        self.butA.pack(side = LEFT)
        self.neonly_frame.pack()
        
        mainloop()

    def check(self,Mint,Hours):
        inc = Mint
        inc2 = Hours
        kost0 = ""
        kost00 = ""
        if inc == 60:
            inc = 0
            kost00 = "0"
            inc2 = int(self.timH.get()) + 1
        elif inc <= 9:
            kost00 = "0"
        if inc2 == 24:
                inc2 = 0
                kost0 = "0"
        elif inc2 <= 9:
            kost0 = "0"
        self.timM.set(kost00+str(inc))
        self.timH.set(kost0+str(inc2))
        self.match(self.mode)
    
    def inc(self):
        inc = int(self.timM.get())+1
        if self.mode == 0 :
            self.label.after(60000,self.inc)
            #vremy
        inc2 = int(self.timH.get())
        self.check(inc,inc2)
        self.match(self.mode)
        
    def incH(self):
        inc = int(self.timM.get())
        inc2 = int(self.timH.get())+1
        self.check(inc,inc2)
        self.match(self.mode)

    def incM(self):
         inc = int(self.timM.get())+1
         inc2 = int(self.timH.get())
         self.check(inc,inc2)
         self.match(self.mode)

    def incA(self):
            if self.mode==0:
                self.time = time.time()
                self.saveM = self.timM.get()
                self.saveH = self.timH.get()
                self.timM.set("00")
                self.timH.set("00")
                self.mode = 1 
            else:
                if self.saveM == self.timM.get() and self.saveH == self.timH.get():
                    mb.showerror("плохо","неидельное время для будильника")
                else:
                    savePromM = self.timM.get()
                    savePromH = self.timH.get()
                    self.fixTime()
                    self.timM.set(self.saveM)
                    self.timH.set(self.saveH)
                    self.saveM = savePromM
                    self.saveH = savePromH
                    self.mode = 0
                    self.label.after_idle(self.inc)
                    
    def match(self,moood):
                if self.saveH == self.timH.get() and self.saveM == self.timM.get() and moood == 0:
                    winsound.Beep(1000, 10000)
                    self.saveM=""
                    self.saveH=""
    def fixTime(self):
                if (int((time.time()-self.time)/60) + int(self.timM.get()))< 60:
                   self.timM.set(int((time.time()-self.time)/60) + int(self.timM.get()))
                else:
                    hours = int(int((time.time()-self.time)/60) + int(self.timM.get())/24)
                    self.timM.set(str(int(int((time.time()-self.time)/60) + int(self.timM.get())) - 60*hours))
                    self.timH.set(str(int(self.timM.get())+hours))
                    
                    
clock()
