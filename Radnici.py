# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 23:44:43 2024

@author: nada
"""

from datetime import date, datetime


#učitavanje radnika iz fajla
def loadRadniks():
    for line in open('radnici.txt', 'r').readlines():
        if len(line) > 1:
            rad = str2Radnik(line)
            radnici.append(rad)


#upisuje novog radnika u fajl
def saveRadniks():
    fajl = open('radnici.txt', 'w')
    for rad in radnici:
        fajl.write(radnik2str(rad))
        fajl.write('\n')
    fajl.close()
    

#trazi radnika po id broju
def findRadnik(indeks): 
    for rad in radnici:
        if rad['id'] == indeks:
            return rad
    return None
    

#traži radnike po prezimenu  #field ce bitit prezime da je po mestu onda bi fail bilo mesto  
#pošto više radnika može imati isto prezime, vrća listu radnika   
def searchRadniks(field, value): 
    result = []
    for rad in radnici:
        if rad[field].upper() == value.upper():
            result.append(rad)
    return result

#dodaje novog radnika u listu
def addRadnik(rad): 
    radnici.append(rad)
    
#menja podatke konkretnog radnika (ovde menja radno mesto)
def updateRadnik(index, rad): 
    radnici[index] = rad


#cita liniju iz fajla i 'pretvara' je u Radnika (kljucevima u recniku dodeljuje vrednosti)
def str2Radnik(line):
    id, ime, prezime, datumRodjenja, datumRodjenja, email, plata, radnoMesto = line.strip().split("|")
    rad = {'id': id,
            'ime': ime,
            'prezime': prezime,
            'datumRodjenja': datumRodjenja,
            'datumZaposlenja': datumRodjenja,
            'email': email,
            'plata': plata,
            'radnoMesto': radnoMesto}
    return rad

#priprema string za upisivanje u fajl
def radnik2str(rad):    
    return '|'.join([rad['id'], rad['ime'], rad['prezime'], 
                     rad['datumRodjenja'], rad['datumZaposlenja'], 
                     rad['email'], str(rad['plata']), rad['radnoMesto']])
     
#traži sledeći slobodan id broj
def maxId():
    return len(radnici) + 1

#header za ispisivanje podataka o radnicima
def formatHeader():
    return \
      "Id  |Ime     |Prezime     |Datum rodj.|Datum rodj.|Email           |Plata        |Radno mesto\n" \
      "---+--------+------------+-----------+-----------+----------------+-------------+-----------"

def formatRadnik(rad):
    return u"{0:3}|{1:<7}|{2:10}|{3:10}|{4:10}|{5:20}|{6:>6}|{7:>10}".format(
      rad['id'],
      rad['ime'],
      rad['prezime'],
      rad['datumRodjenja'],
      rad['datumZaposlenja'],
      rad['email'],
      rad['plata'],
      rad['radnoMesto'])

#za svakog Radnika ispisuje po jedan red ispod headera
def formatRadniks(radList): #treba da moze da formatira bilo oju listu oju joj prosledim
    return "\n".join(map(formatRadnik, radList))

#ovo ispisivanje može i jednostavnije, ostalo mi iz prethodnog projekta
def formatAllRadniks():
    return formatRadniks(radnici)


def sviRadnici():
    return radnici    

    
def sortirajRadnike(key):
    return sorted(radnici, key = lambda x: x[key])
    
print(__name__)  
radnici = []
loadRadniks() 
