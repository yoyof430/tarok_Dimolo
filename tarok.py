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

        self.gumb = Button(self.canvas, command = self.izberi_igro)
        self.gumb.configure(width = 15, height = 5, text = 'START GAME', font = self.font, bg = '#994C00')
        self.gumb_window = self.canvas.create_window(600,500, window = self.gumb)

        self.canvas.bind('<Button-3>', self.premakni_karto)
        self.canvas.bind('<ButtonRelease-3>', self.vrni_karto_nazaj)
        self.canvas.bind('<Button-1>', self.igraj_karto)
        self.canvas.bind('<Control-1>', self.zalozi)
        self.canvas.bind('<Control-3>', self.zalozi_in_zacni)


        mozno = Menu(meni)
        mozno.add_command(label="Nova_igra", command=self.nova_igra)
        mozno.add_command(label="Nova_runda", command=self.runda)

        meni.add_cascade(label="Možnosti", menu=mozno)

        frame = Frame(root, width=600, height=600)
        frame.pack()

    def nova_igra(self):
        '''ponastavi parametre za novo igro'''
        self.dx = 0
        self.dy = 0
        self.razdeli_karte()

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
        self.Klop = Button(self.canvas, text='Klop', command=self.klop)
        self.Klop.configure(width=10, height=4, font=self.font, bg='#994C00')
        self.Tri_window = self.canvas.create_window(600, 220, window=self.Tri)
        self.Dva_window = self.canvas.create_window(600, 320, window=self.Dva)
        self.Ena_window = self.canvas.create_window(600, 420, window=self.Ena)
        self.Klop_window = self.canvas.create_window(600, 520, window=self.Klop)




        self.canvas.delete(self.gumb_window, 'napis') #zbriše gumb 'Začni igro'

    def razdeli_talon3(self):
        'razdeli talon na 2 dela po tri karte'
        self.canvas.delete(self.Tri_window, self.Dva_window, self.Ena_window, self.label_window, self.Klop_window)
        self.razdeli_karte()
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
        self.razdeli_karte()
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
        self.razdeli_karte()
        self.ena = True
        x = 350
        y = 100
        for el in self.karte_talon:
            id = self.canvas.create_image(x,y, image = el.slika)
            self.slovarSlikTalon[id] = (x, y, el)
            x += 120

    def klop(self):
        '''če igralec izbere igro klop'''
        self.canvas.delete(self.Tri_window, self.Dva_window, self.Ena_window, self.label_window, self.Klop_window)
        self.klop = True
        self.razdeli_karte()

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
            print(j)
            self.canvas.delete(j)

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
            barva = self.slovarSlik[self.igranaKarta][-1].barva
            moc = self.slovarSlik[self.igranaKarta][-1].moc
            self.igranaKartaIgralec = self.slovarSlik[self.igranaKarta][-1]
            self.canvas.coords(self.igranaKarta,600,200)
            self.nastavi()
            self.pocisti()
            self.dx += 30
            self.dy += 4
            self.prikazi_karte(self.razvrsti_karte(self.karte_igralec))
        # sleep(0.5)
        #self.racunalnik1_vrze()
        # sleep(0.5)
        #self.racunalnik2_vrze()


    def racunalnik1_igra_prvi(self):
        igranaKarta = self.karte_rac1[random.choice(list(self.karte_rac1.keys()))][-1]
        self.igranaKartaRac1 = igranaKarta

        self.canvas.create_image(500, 150, image=igranaKarta.slika, tag='zadnja')
        self.karte_rac1[igranaKarta.barva].remove(igranaKarta)  # zbrišemo iz slovarja
        # Brišemo barvo, če je računalnik nima več
        if self.karte_rac1[igranaKarta.barva] == []:
            self.karte_rac1.pop(igranaKarta.barva, None)

    def racunalnik1_igra_prvi(self):
        igranaKarta = self.karte_rac2[random.choice(list(self.karte_rac2.keys()))][-1]
        self.igranaKartaRac2 = igranaKarta

        self.canvas.create_image(700, 150, image=igranaKarta.slika, tag='zadnja')
        self.karte_rac2[igranaKarta.barva].remove(igranaKarta)  # zbrišemo iz slovarja
        # Brišemo barvo, če je računalnik nima več
        if self.karte_rac2[igranaKarta.barva] == []:
            self.karte_rac2.pop(igranaKarta.barva, None)


    def racunalnik1_vrze(self):
        '''pogleda kaj je uporabnik igral in vrže adekvatno karto'''
        barva = self.slovarSlik[self.igranaKarta][-1].barva
        moc = self.slovarSlik[self.igranaKarta][-1].moc
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
        barva = self.slovarSlik[self.igranaKarta][-1].barva
        moc = self.slovarSlik[self.igranaKarta][-1].moc
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
        igralci=['igralec','rac1','rac2','igralec','rac1']
        if self.prvi == 'igralec':
            prva=self.igranaKartaIgralec
            druga=self.igranaKartaRac1
            tretja=self.igranaKartaRac2
            karte=[prva,druga,tretja]
            self.prvi=igralci[igralci.index(pobere(karte))]
            if self.prvi=='igralec':
                self.pobraneIgralec.append(karte)
            if self.prvi=='rac1':
                self.pobraneRac1.append(karte)
            if self.prvi=='rac2':
                self.pobraneRac2.append(karte)
        elif self.prvi == 'rac1':
            prva=self.igraj_karto()
            druga=self.racunalnik1_vrze()
            tretja=self.racunalnik2_vrze()
            karte=[prva,druga,tretja]
            self.prvi=igralci[igralci.index(pobere(karte))]
            if self.prvi=='igralec':
                self.pobraneIgralec.append(karte)
            if self.prvi=='rac1':
                self.pobraneRac1.append(karte)
            if self.prvi=='rac2':
                self.pobraneRac2.append(karte)
        elif self.prvi == 'rac2':
            prva=self.igraj_karto()
            druga=self.racunalnik1_vrze()
            tretja=self.racunalnik2_vrze()
            karte=[prva,druga,tretja]
            self.prvi=igralci[igralci.index(pobere(karte))]
            if self.prvi=='igralec':
                self.pobraneIgralec.append(karte)
            if self.prvi=='rac1':
                self.pobraneRac1.append(karte)
            if self.prvi=='rac2':
                self.pobraneRac2.append(karte)
        #print(self.prvi)
        #     sezIg=['igralec','rac1','rac2']
        #     #self.igraj_karto()
        #     self.racunalnik1_vrze()
        #     self.racunalnik2_vrze()
        #     seznamVrzenihBarva = [self.igranaKartaIgralec.barva, self.igranaKartaRac1.barva, self.igranaKartaRac2.barva]
        #     seznamVrzenihMoc = [self.igranaKartaIgralec.moc, self.igranaKartaRac1.moc, self.igranaKartaRac2.moc]
        #     seznamVrzenihVrednost = [self.igranaKartaIgralec.vrednost, self.igranaKartaRac1.vrednost, self.igranaKartaRac2.vrednost]
        #     if 'tarok' in seznamVrzenihBarva:
        #         najvecji = seznamVrzenihMoc.index(max(seznamVrzenihMoc))
        #         self.prvi = sezIg[najvecji]
        #         if najvecji == 0:
        #             self.pobraneIgralec.append(seznamVrzenihVrednost)
        #         elif najvecji == 1:
        #             self.pobraneRac1.append(seznamVrzenihVrednost)
        #         else:
        #             self.pobraneRac2.append(seznamVrzenihVrednost)
        # print(self.pobraneIgralec)







    def razdeli_karte(self):
        #PlaySound('Slike/Zvok.wav', SND_ASYNC)
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

        ##############################da vidmo če deluje pobiranje
        #primerjanje = list(random.sample(self.karte_igralec, 3))
        #print(primerjanje)
        #print(pobere(primerjanje))

        #self.racunalnik1_igra_prvi()

         #pobriše gumb, potem ko je kliknjen


        #print(self.karte_igralec,'\n',self.karte_rac1,'\n',self.karte_rac2,'\n',self.karte_talon)


aplikacija = Cela_igra(root)
root.state('zoomed') #windowed
root.mainloop()

