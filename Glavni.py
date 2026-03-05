# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 21:46:17 2024

@author: nada
"""

import Korisnici
import Radnici
import RadnaMesta
import matplotlib.pyplot as plt
from dateutil.relativedelta import relativedelta
import statistics
from datetime import datetime

#radna mesta samo kao šifarnik

def main():
    print()
    print( "Evidencija radnika")
    print( "====================")
    print()
    if not login():
        print( "\nNiste uneli postojece ime i lozinku!")
        return
    komanda = '0'
    while komanda != 'X':
        komanda = menu()
        if komanda == '1':
            findRadnik()
        elif komanda == '2':
            searchRadniks()
        elif komanda == '3':
            listRadniks()
        elif komanda == '4':
            updateRadnik()
        elif komanda == '5':
            addRadnik()
        elif komanda == '6':
            prosecnaPlata()
        elif komanda == '7':
            plateRadnika()
        elif komanda == '8':
            povecanjePlate()
        elif komanda == '9':
            duzinaZaposlenja()
    print( "Dovidjenja.")

def menu():
    printMenu()
    command = input(">> ")
    while command.upper() not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', 'X'):
        print( "\nUneli ste pogresnu komandu.\n")
        printMenu()
        command = input(">> ")
    return command.upper()

def printMenu():
    print( "\nIzaberite opciju:")
    print( "  1 - pronalazenje radnika")
    print( "  2 - pretrazivanje radnika")
    print( "  3 - pregled svih radnika")
    print( "  4 - izmena podataka o radniku")
    print( "  5 - dodavanje novog radnika")
    print( "  6 - prosecna plata")
    print( "  7 - plate radnika")
    print( "  8 - povecanje plate")
    print( "  9 - duzina zaposlenja")
    print( "  x - izlaz iz programa")

def login():
    username = input("Korisnicko ime >> ")
    password = input("Lozinka >> ")
    return Korisnici.login(username, password)

# id broj je jedinstven (trebalo bi da bude), 
# pa se tako pronalazi samo jedan radnik
def findRadnik():
    print( "[1] Pronalazenje radnika\n")
    id = input("Unesite id broj: ")
    rad = Radnici.findRadnik(id)
    if rad != None:
        print(Radnici.formatHeader())
        print(Radnici.formatRadnik(rad))
    else:
        print("Ne postoji radnik sa id brojem", id)
    
#više radnika može imati isto prezime, pa je rezultat lista
def searchRadniks():
    print( "[2] Pretrazivanje radnika\n")
    prezime = input("Unesite prezime: ")
    radList = Radnici.searchRadniks('prezime', prezime)
    if len(radList) == 0:
        print("Ne postoje takvi radnici.")
    else:
        print(Radnici.formatHeader())
        print(Radnici.formatRadniks(radList))
    
#prikazivanje svih radnika
def listRadniks():
    print( "[3] Pregled svih studenata sortiranih po prezimenu\n")
    #Studenti.sortStudents('prezime')
    Radnici.sortirajRadnike('prezime')
    print(Radnici.formatHeader())
    print(Radnici.formatAllRadniks())

#promena radnog mesta radniku
#proverava se da li uneto radno mesto postoji    
def updateRadnik():
    print( "[4] Izmena podataka o studentu\n")
    id = input("Unesite broj indeksa >> ")
    rad = Radnici.findRadnik(id)
    if rad == None:
        print ("Ne postoji radnik sa datim brojem indeksa.")
    else:
        print( Radnici.formatHeader())
        print( Radnici.formatRadnik(rad)) 
        radnoMesto = input("Unesite novo radno mesto: ")
        while not(RadnaMesta.findRadnoMesto(radnoMesto)):
            radnoMesto = input("Unesite novo radno mesto: ")
        rad['radnoMesto'] = radnoMesto
        Radnici.saveRadniks()
        

#dodavanje novog radnika
#za id radnika uzima se sledeći slobodan broj
def addRadnik():
    print( "[5] Upis novog studenta\n")
    rad = {}
    id = Radnici.maxId()
    rad['id'] = str(id)
    rad['ime'] = input("Unesite ime: ")
    rad['prezime'] = input("Unesite prezime: ")
    rad['datumRodjenja'] = input("Unesite datum rodjenja: ")
    rad['datumZaposlenja'] = input("Unesite datum zaposlenja: ")
    rad['email'] = input("Unesite email: ")
    rad['plata'] = input("Unesite platu: ")
    radnoMesto = input("Unesite radno mesto: ")
    if not(RadnaMesta.findRadnoMesto(radnoMesto)):
        radnoMesto = ''
    rad['radnoMesto'] = radnoMesto
    Radnici.addRadnik(rad)
    Radnici.saveRadniks()
    
#prosečna plata svih radnika
def prosecnaPlata():
    print( "[6] Prosecna plata\n")
    radnici = Radnici.sviRadnici()
    plate = []
    for r in radnici:
        plate.append(float(r['plata']))
    prosek = statistics.mean(plate)
    print('Prosecna plata je:', prosek)

#prikazivanje plata radnika na stubičastom grafikonu
def plateRadnika():
    print( "[7] Plate radnika\n")
    radnici = Radnici.sviRadnici()
    imenaPrezimena = []
    plate = []
    for r in radnici:
        imenaPrezimena.append(r['ime'] + ' ' + r['prezime'])
        plate.append(float(r['plata']))
    plt.bar(imenaPrezimena, plate)
    plt.xticks(rotation=30)
    plt.show()
    
#povećanje plate za 10% radnicima koji rade duže od godinu dana   
def povecanjePlate():
    print( "[8] Povecanje plate\n")
    radnici = Radnici.sviRadnici()
    danasnja_godina=datetime.today().year
    danasnji_mesec=datetime.today().month
    for r in radnici:
        delovi_datuma=r['datumZaposlenja'].split("-")
        godina_Z=int(delovi_datuma[0])
        mesecZ=int(delovi_datuma[1])
        staz_u_mesecima=(danasnja_godina-godina_Z)*12+(danasnji_mesec-mesecZ)
        if staz_u_mesecima>=12:
            nova_plata=float(r['plata'])*1.1
            r['plata']= str(round(nova_plata,2))
        Radnici.saveRadniks()

#dužina zaposlenja u godinama        
def duzinaZaposlenja():
    print( "[9] Duzina zaposlenja\n")
    radnici = Radnici.sviRadnici()
    danasnja_godina=datetime.today().year
    imena = []
    godineStaza = []
    for r in radnici:
        godinaZ=int(r['datumZaposlenja'].split("-")[0])
        staz=danasnja_godina-godinaZ
        imena.append(r['ime']+" "+r['prezime'])
        godineStaza.append(staz)
        
    plt.bar(imena, godineStaza)
    plt.xticks(rotation=30)
    plt.show()
    

print(__name__)    
if __name__ == '__main__':
    main()