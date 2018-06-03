## TAROK

from tkinter import *
from tkinter.font import Font
from threading import Timer
from winsound import *
from karte import *
from math import *
import random
import time

root = Tk()



class Cela_igra():
    def __init__(self, master):
        self.master = master
        #Spremenljivke za user interface
        self.canvas = Canvas(master, width = 1200, height = 700)
        self.ozadje = PhotoImage(file = 'Slike/LesenoOzadje.png')
        self.napis = PhotoImage(file = 'Slike/ZnakFinal.png')
        self.canvas.create_image(600,350, image=self.ozadje)
        self.canvas.create_image(600,200, image = self.napis, tag = 'napis')
        self.font = Font(family='Western Normal', size = 16)

        #Spremenljivke za karte
        self.slovarSlik = dict()
        self.kliknjenaKarta = tuple()
        self.igranaKarta = tuple()
        self.prvaKarta=tuple()
        self.sl = dict()
        self.pomozniSeznam = list()
        self.dx = int()
        self.dy = int()

        #Spremenljivke za talon
        self.slovarSlikTalon = dict()
        self.stevecKlikov = 0
        self.preveri = False
        self.izbrano = False
        self.premakniVx = 0
        self.tri = False
        self.dva = False
        self.ena = False
        self.klop = False
        self.seznamZalozenih = list()

        #Spremenljivke za rezultat
        self.prvi = 'igralec'
        self.pobraneIgralec =list()
        self.pobraneRac1 = list()
        self.pobraneRac2 = list()
        self.id_rac1 = int()
        self.id_rac2 = int()
        self.id_karta_klopa = int()

        #Spremenljivke za določanje vrstnega reda
        self.pobereIgralec = False
        self.pobereRac1 = False
        self.pobereRac2 = False
        self.rac1_igral=False
        self.rac2_igral=False


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

        self.gumb = Button(self.canvas, command = self.nova_igra)
        self.gumb.configure(width = 15, height = 5, text = 'START GAME', font = self.font, bg = '#994C00')
        self.gumb_window = self.canvas.create_window(600,500, window = self.gumb)

        self.canvas.bind('<Button-3>', self.premakni_karto)
        self.canvas.bind('<ButtonRelease-3>', self.vrni_karto_nazaj)
        self.canvas.bind('<Button-1>', self.igraj_karto)
        self.canvas.bind('<Control-1>', self.zalozi)
        self.canvas.bind('<Control-3>', self.zalozi_in_zacni)

    def nova_igra(self):
        '''ponastavi parametre za novo igro'''
        #resetira spremelnjivke
        self.točke_igralec = 0
        self.točke_rac1 = 0
        self.točke_rac2 = 0
        self.karte_igralec = set()
        self.karte_rac1 = set()
        self.karte_rac2 = set()
        self.karte_talon = set()
        self.prvi = 'igralec'
        self.pobraneIgralec = list()
        self.pobraneRac1 = list()
        self.pobraneRac2 = list()
        self.slovarSlikTalon = dict()
        self.stevecKlikov = 0
        self.preveri = False
        self.izbrano = False
        self.premakniVx = 0
        self.tri = False
        self.dva = False
        self.ena = False
        self.klop = False
        self.seznamZalozenih = list()
        self.rac1_igral = False
        self.rac2_igral = False

        self.dx = 0
        self.dy = 0
        self.izberi_igro()


    def izberi_igro(self):
        '''funkcija določi kateri igro bo igralec igral'''
        self.label = Label(self.master, text = 'Izberi igro')
        self.label.configure(width = 15, height = 4, font = self.font, bg = '#994C00')
        self.label_window = self.canvas.create_window(600,100, window = self.label)
        self.Tri = Button(self.canvas, text = 'Tri', command = self.razdeli_talon3)
        self.Tri.configure(width=10, height=4, font=self.font, bg='#994C00')
        self.Dva = Button(self.canvas, text='Dva', command = self.razdeli_talon2)
        self.Dva.configure(width=10, height=4, font=self.font, bg='#994C00')
        self.Ena = Button(self.canvas, text='Ena', command = self.razdeli_talon1)
        self.Ena.configure(width=10, height=4, font=self.font, bg='#994C00')
        self.Klop = Button(self.canvas, text='Klop', command=self.igraj_klop)
        self.Klop.configure(width=10, height=4, font=self.font, bg='#994C00')
        self.Tri_window = self.canvas.create_window(400, 300, window=self.Tri)
        self.Dva_window = self.canvas.create_window(520, 300, window=self.Dva)
        self.Ena_window = self.canvas.create_window(640, 300, window=self.Ena)
        self.Klop_window = self.canvas.create_window(760, 300, window=self.Klop)
        self.razdeli_karte()

        self.canvas.delete(self.gumb_window, 'napis') #zbriše gumb 'Začni igro'

    def razdeli_talon3(self):
        'razdeli talon na 2 dela po tri karte'
        self.canvas.delete(self.Tri_window, self.Dva_window, self.Ena_window, self.label_window, self.Klop_window)
        self.tri = True
        x = 350
        y = 100
        dx = 0
        for el in self.karte_talon[0:3]:
            id = self.canvas.create_image(x+dx, y, image=el.slika)
            self.slovarSlikTalon[id] = (x, y, el)
            dx +=50
        x = 650
        dx = 0
        for el in self.karte_talon[3:6]:
            id = self.canvas.create_image(x + dx, y, image=el.slika)
            self.slovarSlikTalon[id] = (x, y, el)
            dx += 50

    def razdeli_talon2(self):
        'razdeli talon na 3 dela po dve karti'
        self.canvas.delete(self.Tri_window, self.Dva_window, self.Ena_window, self.label_window, self.Klop_window)
        self.dva = True
        x = 350
        y = 100
        dx = 0
        for el in self.karte_talon:
            if self.karte_talon.index(el) <= 1:
                id = self.canvas.create_image(x + dx, y, image=el.slika)
                self.slovarSlikTalon[id] = (x,y,el)
                dx += 50
            elif self.karte_talon.index(el) <= 3:
                x = 550
                id = self.canvas.create_image(x + dx, y, image=el.slika)
                self.slovarSlikTalon[id] = (x, y, el)
                dx += 50
            else:
                x = 750
                id = self.canvas.create_image(x + dx, y, image=el.slika)
                self.slovarSlikTalon[id] = (x, y, el)
                dx += 50

    def razdeli_talon1(self):
        '''razdeli talon na 6 delov po eno karto'''
        self.canvas.delete(self.Tri_window, self.Dva_window, self.Ena_window, self.label_window, self.Klop_window)
        self.ena = True
        x = 350
        y = 100
        for el in self.karte_talon:
            id = self.canvas.create_image(x,y, image = el.slika)
            self.slovarSlikTalon[id] = (x, y, el)
            x += 120

    def igraj_klop(self):
        '''če igralec izbere igro klop'''
        self.canvas.delete(self.Tri_window, self.Dva_window, self.Ena_window, self.label_window, self.Klop_window)
        self.klop = True

    def karte_klop(self):
        '''nariše na platno prvo karto iz seznama talona'''
        if self.karte_talon != []:
            self.id_karta_klopa = self.canvas.create_image(300, 200, image = self.karte_talon[0].slika)
            self.karte_talon = self.karte_talon[1:]
        else:
            self.klop = False

    def zalozi_in_zacni(self,event):
        '''Igralec izbere katere karte bo vzel iz talona in začne igro'''
        if self.preveri == False and self.izbrano == True:
            if self.ena == True:
                self.kliknjenKupcek = self.canvas.find_overlapping(event.x, event.y, event.x + 2, event.y + 2)[-1]
                karta = self.slovarSlikTalon[self.kliknjenKupcek][-1]
                self.karte_igralec.append(karta)
            else:
                self.kliknjenKupcek = self.canvas.find_overlapping(event.x-100, event.y, event.x + 100, event.y + 2)[1:]
                for el in self.kliknjenKupcek:
                    karta = self.slovarSlikTalon[el][-1]
                    self.karte_igralec.append(karta)
            self.pocisti()
            self.prikazi_karte(self.razvrsti_karte(self.karte_igralec))
        self.preveri = True

    def zalozi(self, event):
        '''Igralec izbere katere karte bo založil'''
        self.kliknjenaKartaTalon = self.canvas.find_overlapping(event.x, event.y, event.x + 2, event.y + 2)[-1]  # zadnji narisan element
        if self.kliknjenaKartaTalon in self.slovarSlik.keys():
            if self.tri == True and self.stevecKlikov <= 2:
                self.premakniVx += 100
                self.stevecKlikov += 1
                self.canvas.coords(self.kliknjenaKartaTalon, 350+self.premakniVx,300)
                self.seznamZalozenih.append(self.slovarSlik[self.kliknjenaKartaTalon][-1])
                self.karte_igralec.remove(self.slovarSlik[self.kliknjenaKartaTalon][-1])
            elif self.dva == True and self.stevecKlikov <= 1:
                self.premakniVx += 100
                self.stevecKlikov += 1
                self.canvas.coords(self.kliknjenaKartaTalon, 350+self.premakniVx,300)
                self.seznamZalozenih.append(self.slovarSlik[self.kliknjenaKartaTalon][-1])
                self.karte_igralec.remove(self.slovarSlik[self.kliknjenaKartaTalon][-1])
            elif self.ena == True and self.stevecKlikov <=0:
                self.premakniVx += 100
                self.stevecKlikov += 1
                self.canvas.coords(self.kliknjenaKartaTalon, 350 + self.premakniVx, 300)
                self.seznamZalozenih.append(self.slovarSlik[self.kliknjenaKartaTalon][-1])
                self.karte_igralec.remove(self.slovarSlik[self.kliknjenaKartaTalon][-1])
            self.izbrano = True

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
                    self.slovarSlik[id] = (x, y, el)
                    x += 30
            else:
                dfi = 90 / (len(self.karte_igralec) - 2)
                sez.sort()
                for el in sez:
                    id = self.canvas.create_image(x, y, image=el.slika)
                    self.slovarSlik[id] = (x,y,el)
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
        for j in self.slovarSlikTalon:
            self.canvas.delete(j)

    def pocisti_odigrano(self):
        for i in self.slovarSlik.keys():
            if i == self.igranaKarta:
                self.canvas.delete(i)
        self.canvas.delete(self.id_rac1)
        self.canvas.delete(self.id_rac2)
        if self.klop == True:
            self.canvas.delete(self.id_karta_klopa)

    def nastavi(self):
        '''zbirše odigrano karto iz seznama in ponastavi raspored'''
        barva = self.slovarSlik[self.igranaKarta][-1].barva
        moc =  self.slovarSlik[self.igranaKarta][-1].moc
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

    def preveriKarto(self, barva):
        '''če je uporabnik izbral karto, ki ni iste barve kot vržena/vržene karte'''
        seznamBarv = list()
        for karta in self.karte_igralec:
            seznamBarv.append(karta.barva)
        if self.prvi == 'rac1':
            if barva != self.igranaKartaRac1.barva:
                self.test = False
                if self.igranaKartaRac1.barva not in seznamBarv and barva != 'tarok':
                    self.test = False

        elif self.prvi == 'rac2':
            if barva != self.igranaKartaRac2.barva:
                self.test = False
                if self.igranaKartaRac2.barva not in seznamBarv and barva != 'tarok':
                    self.test = False
        print(seznamBarv)
        #print(self.test)





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
        self.test = True;
        self.preveriKarto(self.slovarSlik[self.igranaKarta][-1].barva)
        #print(self.prvi)
        if self.igranaKarta in self.slovarSlik.keys():
            if self.test:
                barva = self.slovarSlik[self.igranaKarta][-1].barva
                moc = self.slovarSlik[self.igranaKarta][-1].moc
                self.igranaKartaIgralec = self.slovarSlik[self.igranaKarta][-1]
                self.canvas.coords(self.igranaKarta,600,200)
                self.nastavi()
                self.pocisti()
                self.dx += 30
                self.dy += 4
                self.prikazi_karte(self.razvrsti_karte(self.karte_igralec))
                if self.prvi == 'igralec':
                    #print(self.igranaKartaIgralec)
                    self.prvaKarta=self.igranaKartaIgralec
                    self.racunalnik1_vrze()
                    self.racunalnik2_vrze()
                elif self.prvi == 'rac2':
                    self.racunalnik1_vrze()
                self.sestej_in_zacni()


    def racunalnik1_igra_prvi(self):
        #print('igra rac1')
        time.sleep(1)
        self.pocisti()
        self.prikazi_karte(self.razvrsti_karte(self.karte_igralec))
        igranaKarta = self.karte_rac1[random.choice(list(self.karte_rac1.keys()))][-1]
        self.igranaKartaRac1 = igranaKarta

        self.id_rac1 = self.canvas.create_image(500, 150, image=igranaKarta.slika, tag='zadnja')
        self.karte_rac1[igranaKarta.barva].remove(igranaKarta)  # zbrišemo iz slovarja
        # Brišemo barvo, če je računalnik nima več
        if self.karte_rac1[igranaKarta.barva] == []:
            self.karte_rac1.pop(igranaKarta.barva, None)
        self.rac1_igral=True
        self.rac2_igral=True
        self.prvaKarta=self.igranaKartaRac1
        t = Timer(2, self.racunalnik2_vrze)
        t.start()

    def racunalnik2_igra_prvi(self):
        #print('igra rac2')
        time.sleep(1)
        self.pocisti()
        self.prikazi_karte(self.razvrsti_karte(self.karte_igralec))
        igranaKarta = self.karte_rac2[random.choice(list(self.karte_rac2.keys()))][-1]
        self.igranaKartaRac2 = igranaKarta

        self.id_rac2 = self.canvas.create_image(700, 150, image=igranaKarta.slika, tag='zadnja')
        self.karte_rac2[igranaKarta.barva].remove(igranaKarta)  # zbrišemo iz slovarja
        # Brišemo barvo, če je računalnik nima več
        if self.karte_rac2[igranaKarta.barva] == []:
            self.karte_rac2.pop(igranaKarta.barva, None)
        self.rac2_igral = True
        self.prvaKarta=self.igranaKartaRac2

    def racunalnik1_vrze(self):
        '''pogleda kaj je uporabnik igral in vrže adekvatno karto'''
        barva = self.prvaKarta.barva
        moc = self.prvaKarta.moc
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

        self.id_rac1 = self.canvas.create_image(500, 150, image=igranaKarta.slika, tag='zadnja')
        self.karte_rac1[igranaKarta.barva].remove(igranaKarta)  # zbrišemo iz slovarja
        # Brišemo barvo, če je računalnik nima več
        if self.karte_rac1[igranaKarta.barva] == []:
            self.karte_rac1.pop(igranaKarta.barva, None)

    def racunalnik2_vrze(self):
        '''pogleda kaj je uporabnik igral in vrže adekvatno karto'''
        #print('rac2 vrze')
        #barva = self.slovarSlik[self.igranaKarta][-1].barva
        #moc = self.slovarSlik[self.igranaKarta][-1].moc
        barva=self.prvaKarta.barva
        moc=self.prvaKarta.moc
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

        self.id_rac2 = self.canvas.create_image(700, 150, image=igranaKarta.slika, tag='zadnja')
        self.karte_rac2[igranaKarta.barva].remove(igranaKarta) #zbrišemo iz slovarja
        #Brišemo barvo, če je računalnik nima več
        if self.karte_rac2[igranaKarta.barva] == []:
            self.karte_rac2.pop(igranaKarta.barva, None)

    def sestej_in_zacni(self):
        '''sešteje točke in doloći kdo začne naslednjo rundo'''
        #print(self.karte_rac1)
        #print(self.karte_rac2)
        igralci=['igralec','rac1','rac2','igralec','rac1']
        if self.prvi == 'igralec':
            prva=self.igranaKartaIgralec
            druga=self.igranaKartaRac1
            tretja=self.igranaKartaRac2
            karte=[prva,druga,tretja]
            #print(karte)
            self.prvi=igralci[pobere(karte)]
            if self.prvi=='igralec':
                self.pobereIgralec = True
                self.pobraneIgralec+= karte
            elif self.prvi=='rac1':
                self.pobereRac1 = True
                self.pobraneRac1+= karte
            elif self.prvi=='rac2':
                self.pobereRac2 = True
                self.pobraneRac2+= karte

        elif self.prvi == 'rac1':
            prva=self.igranaKartaRac1
            druga=self.igranaKartaRac2
            tretja=self.igranaKartaIgralec
            karte=[prva,druga,tretja]
            #print(karte)
            self.prvi=igralci[pobere(karte)+1]
            if self.prvi=='igralec':
                self.pobereIgralec = True
                self.pobraneIgralec+= karte
            if self.prvi=='rac1':
                self.pobereRac1 = True
                self.pobraneRac1+= karte
            if self.prvi=='rac2':
                self.pobereRac2 = True
                self.pobraneRac2+= karte
        elif self.prvi == 'rac2':
            prva=self.igranaKartaRac2
            druga=self.igranaKartaIgralec
            tretja=self.igranaKartaRac1
            karte=[prva,druga,tretja]
            #print(karte)
            self.prvi=igralci[pobere(karte)+2]
            if self.prvi=='igralec':
                self.pobereIgralec = True
                self.pobraneIgralec+=karte
            elif self.prvi=='rac1':
                self.pobereRac1 = True
                self.pobraneRac1+= karte
            elif self.prvi=='rac2':
                self.pobereRac2 = True
                self.pobraneRac2+= karte
        if self.klop == True:
            if self.prvi == 'igralec' and self.karte_talon != []:
                self.pobraneIgralec.append(self.karte_talon[0])
            elif self.prvi == 'rac1' and self.karte_talon != []:
                self.pobraneRac1.append(self.karte_talon[0])
            elif self.prvi == 'rac2' and self.karte_talon != []:
                self.pobraneRac2.append(self.karte_talon[0])
        if self.klop == True:
            self.karte_klop()
        if self.karte_igralec == [] and self.karte_rac2 == {} and self.karte_rac1 == {}:
            self.doloci_zmagovalca()
        t = Timer(3, self.igra_naslednji)
        t.start()

    def doloci_zmagovalca(self):
        '''določi kdo je zmagal'''
        tocke = 0
        tockeRac1 = 0
        tockeRac2 = 0
        sporocilo = ''
        for karta in self.pobraneIgralec:
            tocke += karta.vrednost
        tocke = tocke - 2/3*(len(self.pobraneIgralec))
        if self.tri or self.dva or self.ena:
            if tocke >= 35:
                sporocilo = ('------------'+'\n'+
                             'ZMAGAL SI!'+'\n'+
                             '------------')
            else:
                sporocilo = ('------------'+'\n'+
                             'IZGUBIL SI!'+'\n'+
                             '------------')
        else:
            for karta in self.pobraneRac1:
                tockeRac1 += karta.vrednost
            for karta in self.pobraneRac2:
                tockeRac2 += karta.vrednost

        if max(tocke, tockeRac1, tockeRac2) == tocke:
            sporocilo = ('------------------------------------'+'\n'+
                            'Tvoje število tock: '+str(tocke)+'\n'+
                            'Število točk računalnika 1: '+str(tockeRac1)+'\n'+
                            'Število točk računalnika 2: '+str(tockeRac2)+'\n'+
                            '------------------------------------'+'\n'+
                            'IZGUBIL SI!')
        elif min(tocke, tockeRac1, tockeRac2) == tocke:
            sporocilo = ('------------------------------------'+'\n'+
                            'Tvoje število tock: '+str(tocke)+'\n'+
                            'Število točk računalnika 1: '+str(tockeRac1)+'\n'+
                            'Število točk računalnika 2: '+str(tockeRac2)+'\n'+
                            '------------------------------------'+'\n'+
                            'ZMAGAL SI!')
        okno = Tk()
        okno.wm_title("IZID IGRE")
        okno.configure(width = 100, height = 100, background = '#994C00')
        oznaka = Label(okno, text = sporocilo, font = self.font)
        oznaka.configure(background = '#994C00')
        oznaka.pack(side = 'top', fill = 'x', pady = 100)
        gumb = Button(okno, text = 'Nova Igra?', font = self.font, command = lambda:[self.nova_igra(),okno.destroy()])
        gumb.configure(font = self.font, background = '#994C00')
        gumb.pack()

    def igra_naslednji(self):
        '''pokliče naslednjega igralca'''
        self.pocisti_odigrano()
        if self.pobereRac1 == True:
            t = Timer(2, self.racunalnik1_igra_prvi)
            t.start()
        elif self.pobereRac2 == True:
            t = Timer(2,self.racunalnik2_igra_prvi)
            t.start()
        self.pobereIgralec = False
        self.pobereRac1 = False
        self.pobereRac2 = False


    def razdeli_karte(self):
        '''razdeli karte'''
        PlaySound('Slike/Zvok.wav', SND_ASYNC)
        self.karte_talon = ustvari_karte()
        self.karte_igralec=random.sample(self.karte_talon,16)
        self.karte_talon=self.karte_talon.difference(self.karte_igralec)
        self.karte_rac1 = random.sample(self.karte_talon, 16)
        self.karte_talon = self.karte_talon.difference(self.karte_rac1)
        self.karte_rac2 = random.sample(self.karte_talon, 16)
        self.karte_talon = list(self.karte_talon.difference(self.karte_rac2))

        self.pomozniSeznamIgralec = self.karte_igralec.copy()

        self.razvrsti_karte(self.pomozniSeznamIgralec)
        self.karte_rac1 = self.razvrsti_karte(self.karte_rac1)
        self.karte_rac2 = self.razvrsti_karte(self.karte_rac2)
        self.prikazi_karte(self.razvrsti_karte(self.karte_igralec))

aplikacija = Cela_igra(root)
root.state('zoomed') #windowed
root.mainloop()