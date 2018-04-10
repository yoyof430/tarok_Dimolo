## TAROK

from tkinter import *
from tkinter.font import Font
from winsound import *
from karte import *
from math import *
import random

#print(type(karte))
root = Tk()



class Cela_igra():
    def __init__(self, master):
        self.master = master
        self.canvas = Canvas(master, width = 1200, height = 700)
        self.ozadje = PhotoImage(file = 'Slike/LesenoOzadje.png')
        self.napis = PhotoImage(file = 'Slike/ZnakFinal.png')
        self.canvas.create_image(600,350, image=self.ozadje)
        self.canvas.create_image(600,200, image = self.napis, tag = 'napis')
        self.font = Font(family='Western Normal', size = 16)
        self.slovarSlik = dict()
        self.kliknjenaKarta = tuple()
        self.igranaKarta = tuple()
        self.sl = dict()


        self.canvas.pack()
        self.točke_igralec=0
        self.točke_rac1= 0
        self.točke_rac2= 0
        self.karte_igralec =set()
        self.karte_rac1=set()
        self.karte_rac2=set()
        self.karte_talon=set()
        meni = Menu(self.master)
        self.master.config(menu=meni)
        self.gumb = Button(self.canvas, command = self.razdeli_karte)
        self.gumb.configure(width = 15, height = 5, text = 'START GAME', font = self.font, bg = '#994C00')
        self.gumb_window = self.canvas.create_window(600,500, window = self.gumb)
        self.canvas.bind('<Button-3>', self.premakni_karto)
        self.canvas.bind('<ButtonRelease-3>', self.vrni_karto_nazaj)
        self.canvas.bind('<Button-1>', self.igraj_karto)









        mozno = Menu(meni)
        mozno.add_command(label="Nova_igra", command=self.razdeli_karte)

        meni.add_cascade(label="Možnosti", menu=mozno)

        frame = Frame(root, width=600, height=600)
        frame.pack()

    def razvrsti_karte(self,seznam):
        '''razvrsti karte po barvi in velikosti'''
        self.sl = {'križ':[],'srce':[],'pik':[],'karo':[],'tarok':[]}
        for el in seznam:
            self.sl[el.barva].append(el)
        return self.sl

    def prikazi_karte(self,sl):
        '''nariše igralčeve karte na platnu'''
        x = 200
        y = 550
        fi = 135
        dfi = 90/(len(self.karte_igralec)-2)

        for sez in sl.values():
            sez.sort()
            for el in sez:
                id = self.canvas.create_image(x, y, image=el.slika)
                self.slovarSlik[id] = (x,y)
                x += 60*sin(radians(fi))
                y += 30*cos(radians(fi))
                fi -= dfi
        print(self.slovarSlik)

    def premakni_karto(self, event):
        '''najde kliknjeno karto in jo premakne v vidno polje'''
        self.kliknjenaKarta = self.canvas.find_overlapping(event.x, event.y, event.x+2, event.y+2)[-1] #zadnji narisan element
        if self.kliknjenaKarta >= 3:
            x = self.slovarSlik[self.kliknjenaKarta][0]
            y = self.slovarSlik[self.kliknjenaKarta][1]
            self.canvas.coords(self.kliknjenaKarta, x-40,y-20)

    def vrni_karto_nazaj(self,event):
        '''vrne karto nazaj na svoje prvotno mesto'''
        #ID = self.canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)[-1]
        x = self.slovarSlik[self.kliknjenaKarta][0]
        y = self.slovarSlik[self.kliknjenaKarta][1]
        self.canvas.coords(self.kliknjenaKarta, x, y)

    def igraj_karto(self,event):
        '''vrže karto na igralno površino'''
        self.igranaKarta = self.canvas.find_overlapping(event.x, event.y, event.x+2, event.y+2)[-1]
        if self.igranaKarta >= 3:
            self.canvas.coords(self.igranaKarta,600,200)

    #def ponastavi(self):


    def razdeli_karte(self):
        #PlaySound('Slike/Zvok.wav', SND_ASYNC)
        self.karte_talon = ustvari_karte()
        self.karte_igralec=random.sample(self.karte_talon,16)
        self.prikazi_karte(self.razvrsti_karte(self.karte_igralec))
        self.razvrsti_karte(self.karte_igralec)
        self.karte_talon=self.karte_talon.difference(self.karte_igralec)
        self.karte_rac1 = random.sample(self.karte_talon, 16)
        self.karte_talon = self.karte_talon.difference(self.karte_rac1)
        self.karte_rac2= random.sample(self.karte_talon, 16)
        self.karte_talon = self.karte_talon.difference(self.karte_rac2)
        self.canvas.delete(self.gumb_window, 'napis') #pobriše gumb, potem ko je kliknjen


        print(self.karte_igralec,'\n',self.karte_rac1,'\n',self.karte_rac2,'\n',self.karte_talon)





aplikacija = Cela_igra(root)
root.state('zoomed') #windowed
root.mainloop()