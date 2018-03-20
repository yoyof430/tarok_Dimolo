## TAROK

from tkinter import *
import random

root = Tk()

T1='XT1'
T2='XT2'
T3='XT3'
T4='XT4'
T5='XT5'
T6='XT6'
T7='XT7'
T8='XT8'
T9='XT9'
T10='XT10'
T11='XT11'
T12='XT12'
T13='XT13'
T14='XT14'
T15='XT15'
T16='XT16'
T17='XT17'
T18='XT18'
T19='XT19'
T20='XT20'
T21='XT21'
T22='XT22'
S1='XS1'
S2='XS2'
S3='XS3'
S4='XS4'
S5='XS5'
S6='XS6'
S7='XS7'
S8='XS8'
H1='XH1'
H2='XH2'
H3='XH3'
H4='XH4'
H5='XH5'
H6='XH6'
H7='XH7'
H8='XH8'
D1='XD1'
D2='XD2'
D3='XD3'
D4='XD4'
D5='XD5'
D6='XD6'
D7='XD7'
D8='XD8'
C1='XC1'
C2='XC2'
C3='XC3'
C4='XC4'
C5='XC5'
C6='XC6'
C7='XC7'
C8='XC8'

karte = set([T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18,T19,T20,T21,T22,S1,S2,S3,S4,S5,S6,S7,S8,H1,H2,H3,H4,H5,H6,H7,H8,D1,D2,D3,D4,D5,D6,D7,D8,C1,C2,C3,C4,C5,C6,C7,C8])

class Cela_igra():
    def __init__(self, master):
        self.master = master
        self.canvas = Canvas(master, width = 1200, height = 700)
        self.ozdaje = PhotoImage(file = 'Ozadje.pbm')
        self.ozadjeGumba = PhotoImage(file = 'whiskey.png')
        self.canvas.create_image(600,350, image=self.ozdaje)

        self.klikGumba = False


        self.canvas.pack()
        self.točke_igralec=0
        self.točke_rac1= 0
        self.točke_rac2= 0
        self.karte_igralec =set()
        self.karte_rac1=set()
        self.karte_rac2=set()
        self.karte_talon=karte
        meni = Menu(self.master)
        self.master.config(menu=meni)
        self.gumb = Button(self.canvas, command = self.razdeli_karte)
        self.gumb.configure(width = 150, height = 150, text = 'ZAČNI IGRO', image = self.ozadjeGumba)
        self.gumb_window = self.canvas.create_window(600,350, window = self.gumb)





        mozno = Menu(meni)
        mozno.add_command(label="Nova_igra", command=self.razdeli_karte)

        meni.add_cascade(label="Možnosti", menu=mozno)

        frame = Frame(root, width=600, height=600)
        frame.pack()


    def razdeli_karte(self):
        self.karte_talon = karte
        self.karte_igralec=random.sample(self.karte_talon,16)
        self.karte_talon=self.karte_talon.difference(self.karte_igralec)
        self.karte_rac1 = random.sample(self.karte_talon, 16)
        self.karte_talon = self.karte_talon.difference(self.karte_rac1)
        self.karte_rac2= random.sample(self.karte_talon, 16)
        self.karte_talon = self.karte_talon.difference(self.karte_rac2)
        #self.canvas.delete(self.gumb_window) #pobriše gumb, potem ko je kliknjen
        print(self.karte_igralec,'\n',self.karte_rac1,'\n',self.karte_rac2,'\n',self.karte_talon)



    def nova_igra(self):
        self.rac = 0
        self.igralec = 0
        self.rezultat = ""
        self.pripravi_canvas()
        self.posodobi()

    def shrani(self):
        with open("lizard.txt", 'w') as a:
            print('{}\n{}'.format(self.igralec, self.rac), file=a)

    def nalozi(self):
        sez = []
        with open("lizard.txt", 'r') as b:
            for i in b:
                x = i.strip()
                sez.append(int(x))
            self.igralec = sez[0]
            self.rac = sez[1]
            self.rezultat = ""
        self.posodobi()
        self.pripravi_canvas()

    def posodobi(self):
        self.napis_rezultat.set(str(self.rezultat))
        self.napis_tock_igralec.set("igralec: %s" % str(self.igralec))
        self.napis_tock_rac.set("računalnik:%s" % str(self.rac))






aplikacija = Cela_igra(root)
root.mainloop()