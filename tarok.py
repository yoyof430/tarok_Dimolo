## TAROK

from tkinter import *
from tkinter.font import Font
from winsound import *
from karte import *
from math import *
import random
from time import *

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
        self.pomozniSeznam = list()
        self.dx = int()
        self.dy = int()

        #Spremenljivke za rezultat
        self.prvi = ''
        self.pobraneIgralec =list()
        self.pobraneRac1 = list()
        self.pobraneRac2 = list()


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
        mozno.add_command(label="Nova_igra", command=self.nova_igra)

        meni.add_cascade(label="Možnosti", menu=mozno)

        frame = Frame(root, width=600, height=600)
        frame.pack()

    def nova_igra(self):
        '''ponastavi parametre za novo igro'''
        self.dx = 0
        self.dy = 0
        self.razdeli_karte()

    def razvrsti_karte(self,seznam):
        '''razvrsti karte po barvi in velikosti'''
        self.sl = {'križ':[],'srce':[],'pik':[],'karo':[],'tarok':[]}
        for el in seznam:
            self.sl[el.barva].append(el)


        return self.sl




    def prikazi_karte(self,sl):
        '''nariše igralčeve karte na platnu'''
        x = 200 + self.dx
        y = 600 - self.dy
        fi = 135
        #Če ostaneta dve karti na koncu
        for sez in sl.values():
            if len(self.karte_igralec) < 3:
                for el in sez:

                    id = self.canvas.create_image(x, y, image=el.slika)
                    self.slovarSlik[id] = (x, y, el.barva, el.moc)
                    x += 30
            else:
                dfi = 90 / (len(self.karte_igralec) - 2)
                sez.sort()
                for el in sez:
                    id = self.canvas.create_image(x, y, image=el.slika)
                    self.slovarSlik[id] = (x,y,el.barva, el.moc)
                    x += 60*sin(radians(fi))
                    y += 30*cos(radians(fi))
                    fi -= dfi
            #print(self.slovarSlik)

    def pocisti(self):
        '''pobriše do zdaj narisane karte, razen odigrane karte'''
        for i in self.slovarSlik.keys():
            if i == self.igranaKarta:
                pass
            else:
                self.canvas.delete(i)

    def nastavi(self):
        '''zbirše odigrano karto iz seznama in ponastavi raspored'''
        barva = self.slovarSlik[self.igranaKarta][2]
        moc = self.slovarSlik[self.igranaKarta][3]
        for i, e in enumerate(self.karte_igralec):
            if e.barva == str(barva) and e.moc == moc:
                break
        del self.karte_igralec[i]

    def premakni_karto(self, event):
        '''najde kliknjeno karto in jo premakne v vidno polje'''
        self.kliknjenaKarta = self.canvas.find_overlapping(event.x, event.y, event.x+2, event.y+2)[-1] #zadnji narisan element
        if self.kliknjenaKarta in self.slovarSlik.keys():
            x = self.slovarSlik[self.kliknjenaKarta][0]
            y = self.slovarSlik[self.kliknjenaKarta][1]
            self.canvas.coords(self.kliknjenaKarta, x-40,y-20)

    def vrni_karto_nazaj(self,event):
        '''vrne karto nazaj na svoje prvotno mesto'''
        #ID = self.canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)[-1]
        if self.kliknjenaKarta in self.slovarSlik.keys():
            x = self.slovarSlik[self.kliknjenaKarta][0]
            y = self.slovarSlik[self.kliknjenaKarta][1]
            self.canvas.coords(self.kliknjenaKarta, x, y)




    def igraj_karto(self,event):
        '''vrže karto na igralno površino'''
        self.igranaKarta = self.canvas.find_overlapping(event.x, event.y, event.x+2, event.y+2)[-1]
        if self.igranaKarta in self.slovarSlik.keys():
            barva = self.slovarSlik[self.igranaKarta][-2]
            moc = int(self.slovarSlik[self.igranaKarta][-1])
            self.sl[barva]
            self.canvas.coords(self.igranaKarta,600,200)
            self.nastavi()
            self.pocisti()
            self.dx += 30
            self.dy += 4
            self.prikazi_karte(self.razvrsti_karte(self.karte_igralec))
        # sleep(0.5)
        self.racunalnik1_vrze()
        # sleep(0.5)
        self.racunalnik2_vrze()
        self.runda()



    def racunalnik1_vrze(self):
        '''pogleda kaj je uporabnik igral in vrže adekvatno karto'''
        barva = self.slovarSlik[self.igranaKarta][-2]
        moc = int(self.slovarSlik[self.igranaKarta][-1])
        igranaKarta = str()
        if barva in self.karte_rac1.keys():  # pogledamo, če rač ima sploh barvo
            if self.karte_rac1[barva] != []:
                for karta in self.karte_rac1[barva]:
                    if karta.moc > moc:
                        igranaKarta = karta
                    else:
                        igranaKarta = self.karte_rac1[barva][0]
            else:
                igranaKarta = self.karte_rac1["tarok"][0]
        else:
            if 'tarok' in self.karte_rac1.keys():  # če še ima taroke
                igranaKarta = self.karte_rac1["tarok"][0]
            else:
                igranaKarta = self.karte_rac1[random.choice(list(self.karte_rac1.keys()))][0]
        #print(igranaKarta)
        self.igranaKartaRac1 = igranaKarta

        self.canvas.create_image(500, 150, image=igranaKarta.slika, tag='zadnja')
        self.karte_rac1[igranaKarta.barva].remove(igranaKarta)  # zbrišemo iz slovarja
        # Brišemo barvo, če je računalnik nima več
        if self.karte_rac1[igranaKarta.barva] == []:
            self.karte_rac1.pop(igranaKarta.barva, None)

    def racunalnik2_vrze(self):
        '''pogleda kaj je uporabnik igral in vrže adekvatno karto'''
        barva = self.slovarSlik[self.igranaKarta][-2]
        moc = int(self.slovarSlik[self.igranaKarta][-1])
        igranaKarta = str()
        if barva in self.karte_rac2.keys(): #pogledamo, če rač ima sploh barvo
            if self.karte_rac2[barva] != []:
                for karta in self.karte_rac2[barva]:
                    if karta.moc > moc:
                        igranaKarta = karta
                    else:
                        igranaKarta = self.karte_rac2[barva][0]
            else:
                igranaKarta = self.karte_rac2["tarok"][0]
        else:
            if 'tarok' in self.karte_rac2.keys(): #če še ima taroke
                igranaKarta = self.karte_rac2["tarok"][0]
            else:
                igranaKarta = self.karte_rac2[random.choice(list(self.karte_rac2.keys()))][0]
        self.igranaKartaRac2 = igranaKarta

        self.canvas.create_image(700, 150, image=igranaKarta.slika, tag='zadnja')
        self.karte_rac2[igranaKarta.barva].remove(igranaKarta) #zbrišemo iz slovarja
        #Brišemo barvo, če je računalnik nima več
        if self.karte_rac2[igranaKarta.barva] == []:
            self.karte_rac2.pop(igranaKarta.barva, None)

        #print(self.karte_rac2[random.choice(self.karte_rac2.keys())][0])

    def runda(self):
        print(self.igranaKartaIgralec,'\n', self.igranaKartaRac1, '\n', self.igranaKartaRac2)






    def razdeli_karte(self):
        #PlaySound('Slike/Zvok.wav', SND_ASYNC)
        self.karte_talon = ustvari_karte()
        self.karte_igralec=random.sample(self.karte_talon,16)
        self.karte_talon=self.karte_talon.difference(self.karte_igralec)
        self.karte_rac1 = random.sample(self.karte_talon, 16)
        self.karte_talon = self.karte_talon.difference(self.karte_rac1)
        self.karte_rac2 = random.sample(self.karte_talon, 16)
        self.karte_talon = self.karte_talon.difference(self.karte_rac2)

        self.pomozniSeznamIgralec = self.karte_igralec.copy()

        self.razvrsti_karte(self.pomozniSeznamIgralec)
        self.karte_rac1 = self.razvrsti_karte(self.karte_rac1)
        self.karte_rac2 = self.razvrsti_karte(self.karte_rac2)
        self.prikazi_karte(self.razvrsti_karte(self.karte_igralec))


        self.canvas.delete(self.gumb_window, 'napis') #pobriše gumb, potem ko je kliknjen


        #print(self.karte_igralec,'\n',self.karte_rac1,'\n',self.karte_rac2,'\n',self.karte_talon)





aplikacija = Cela_igra(root)
root.state('zoomed') #windowed
root.mainloop()