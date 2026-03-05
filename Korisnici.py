# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 21:42:52 2024

@author: nada
"""

#provera da li postoji korisnik sa unetim korisničkim imenom i šifrom
def login(username, password):
    for k in korisnici:
        if k['username']==username and k['lozinka']==password:
            return True
    return False

#ucitati korisnike iz fajla    
def loadUsers(): 
    for line in open("korisnici.txt", "r").readlines():
        if len(line)>1:
            k=str2user(line)
            korisnici.append(k)
    pass

#liniju iz fajla konvertovati u jednog korisnika (rečnik)
def str2user(line): 
    id, ime, prezime, username, lozinka, uloga=line.strip().split("|")
    m={"id": id, "ime": ime, "prezime": prezime, "username":username, "lozinka":
       lozinka, "uloga":uloga}
    return m

#referenta (rečnik) zapisati kao string sa | između
def user2str(k): 
    return "|".join(k['id'], k['ime'], k['prezime'], k['username'], k['lozinka'])

print(__name__)      
korisnici = []
loadUsers()
