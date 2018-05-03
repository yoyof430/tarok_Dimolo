from tkinter import *
class Karte():
    def __init__(self,slika, barva, vrednost, moc):
        self.barva = barva
        self.vrednost = vrednost
        self.moc = moc
        self.slika = PhotoImage(file = slika)
    def __lt__(self, other):
        return self.moc<other.moc

    def __repr__(self):
        return str(self.barva)+' '+str(self.moc)+' '+str(self.vrednost)

def pobere(list):
    '''pogleda katere od kart v seznamu je najmočnejša'''
    if max(list).moc>10:
        pob=max(list)
    else:
        pob=list[0]
        if list[1].barva==list[0].barva and list[1]>pob:
            pob=list[1]
        if list[2].barva==list[0].barva and list[2]>pob:
            pob=list[2]
    return list.index(pob)


def ustvari_karte():
    '''ustvari karte'''
    T1=Karte('./Slike/Karte/T1.png', barva = 'tarok', vrednost= 5, moc = 11)
    T2=Karte('./Slike/Karte/T2.png', barva = 'tarok', vrednost= 1, moc = 12)
    T3=Karte('./Slike/Karte/T3.png', barva = 'tarok', vrednost= 1, moc = 13)
    T4=Karte('./Slike/Karte/T4.png', barva = 'tarok', vrednost= 1, moc = 14)
    T5=Karte('./Slike/Karte/T5.png', barva = 'tarok', vrednost= 1, moc = 15)
    T6=Karte('./Slike/Karte/T6.png', barva = 'tarok', vrednost= 1, moc = 16)
    T7=Karte('./Slike/Karte/T7.png', barva = 'tarok', vrednost= 1, moc = 17)
    T8=Karte('./Slike/Karte/T8.png', barva = 'tarok', vrednost= 1, moc = 18)
    T9=Karte('./Slike/Karte/T9.png', barva = 'tarok', vrednost= 1, moc = 19)
    T10=Karte('./Slike/Karte/T10.png', barva = 'tarok', vrednost= 1, moc = 20)
    T11=Karte('./Slike/Karte/T11.png', barva = 'tarok', vrednost= 1, moc = 21)
    T12=Karte('./Slike/Karte/T12.png', barva = 'tarok', vrednost= 1, moc = 22)
    T13=Karte('./Slike/Karte/T13.png', barva = 'tarok', vrednost= 1, moc = 23)
    T14=Karte('./Slike/Karte/T14.png', barva = 'tarok', vrednost= 1, moc = 24)
    T15=Karte('./Slike/Karte/T15.png', barva = 'tarok', vrednost= 1, moc = 25)
    T16=Karte('./Slike/Karte/T16.png', barva = 'tarok', vrednost= 1, moc = 26)
    T17=Karte('./Slike/Karte/T17.png', barva = 'tarok', vrednost= 1, moc = 27)
    T18=Karte('./Slike/Karte/T18.png', barva = 'tarok', vrednost= 1, moc = 28)
    T19=Karte('./Slike/Karte/T19.png', barva = 'tarok', vrednost= 1, moc = 29)
    T20=Karte('./Slike/Karte/T20.png', barva = 'tarok', vrednost= 1, moc = 30)
    T21=Karte('./Slike/Karte/T21.png', barva = 'tarok', vrednost= 5, moc = 31)
    T22=Karte('./Slike/Karte/T22.png', barva = 'tarok', vrednost= 5, moc = 32)
    S1=Karte('./Slike/Karte/S1.png', barva = 'pik', vrednost= 1, moc = 1)
    S2=Karte('./Slike/Karte/S2.png', barva = 'pik', vrednost= 1, moc = 2)
    S3=Karte('./Slike/Karte/S3.png', barva = 'pik', vrednost= 1, moc = 3)
    S4=Karte('./Slike/Karte/S4.png', barva = 'pik', vrednost= 1, moc = 4)
    S5=Karte('./Slike/Karte/S5.png', barva = 'pik', vrednost= 2, moc = 5)
    S6=Karte('./Slike/Karte/S6.png', barva = 'pik', vrednost= 3, moc = 6)
    S7=Karte('./Slike/Karte/S7.png', barva = 'pik', vrednost= 4, moc = 7)
    S8=Karte('./Slike/Karte/S8.png', barva = 'pik', vrednost= 5, moc = 8)
    H1=Karte('./Slike/Karte/H1.png', barva = 'srce', vrednost= 1, moc = 1)
    H2=Karte('./Slike/Karte/H2.png', barva = 'srce', vrednost= 1, moc = 2)
    H3=Karte('./Slike/Karte/H3.png', barva = 'srce', vrednost= 1, moc = 3)
    H4=Karte('./Slike/Karte/H4.png', barva = 'srce', vrednost= 1, moc = 4)
    H5=Karte('./Slike/Karte/H5.png', barva = 'srce', vrednost= 2, moc = 5)
    H6=Karte('./Slike/Karte/H6.png', barva = 'srce', vrednost= 3, moc = 6)
    H7=Karte('./Slike/Karte/H7.png', barva = 'srce', vrednost= 4, moc = 7)
    H8=Karte('./Slike/Karte/H8.png', barva = 'srce', vrednost= 5, moc = 8)
    D1=Karte('./Slike/Karte/D1.png', barva = 'karo', vrednost= 1, moc = 1)
    D2=Karte('./Slike/Karte/D2.png', barva = 'karo', vrednost= 1, moc = 2)
    D3=Karte('./Slike/Karte/D3.png', barva = 'karo', vrednost= 1, moc = 3)
    D4=Karte('./Slike/Karte/D4.png', barva = 'karo', vrednost= 1, moc = 4)
    D5=Karte('./Slike/Karte/D5.png', barva = 'karo', vrednost= 2, moc = 5)
    D6=Karte('./Slike/Karte/D6.png', barva = 'karo', vrednost= 3, moc = 6)
    D7=Karte('./Slike/Karte/D7.png', barva = 'karo', vrednost= 4, moc = 7)
    D8=Karte('./Slike/Karte/D8.png', barva = 'karo', vrednost= 5, moc = 8)
    C1=Karte('./Slike/Karte/C1.png', barva = 'križ', vrednost= 1, moc = 1)
    C2=Karte('./Slike/Karte/C2.png', barva = 'križ', vrednost= 1, moc = 2)
    C3=Karte('./Slike/Karte/C3.png', barva = 'križ', vrednost= 1, moc = 3)
    C4=Karte('./Slike/Karte/C4.png', barva = 'križ', vrednost= 1, moc = 4)
    C5=Karte('./Slike/Karte/C5.png', barva = 'križ', vrednost= 2, moc = 5)
    C6=Karte('./Slike/Karte/C6.png', barva = 'križ', vrednost= 3, moc = 6)
    C7=Karte('./Slike/Karte/C7.png', barva = 'križ', vrednost= 4, moc = 7)
    C8=Karte('./Slike/Karte/C8.png', barva = 'križ', vrednost= 5, moc = 8)
    return{S1,S2,S3,S4,S5,S6,S7,S8,H1,H2,H3,H4,H5,H6,H7,H8,D1,D2,D3,D4,D5,D6,D7,D8,C1,C2,C3,C4,C5,C6,C7,C8,T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18,T19,T20,T21,T22}

#print(type(C8))