# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 22:07:59 2024

@author: nada
"""

#učitavanje radnih mesta iz fajla
def loadRadnaMesta():
    for line in open('radnaMesta.txt', 'r').readlines():
        if len(line) > 1:
            rm = str2rm(line)
            radnaMesta.append(rm)


#upisuje radna mesta nazad u fajl
#mada ovde nema promena
def saveRadnaMesta():
    fajl = open('radnaMesta.txt', 'w')
    for rm in radnaMesta:
        fajl.write(rm2str(rm))
        fajl.write('\n')
    fajl.close()
    
    
#pretvaranje linije iz fajla u rečnik    
def str2rm(line):
    id, naziv = line.strip().split("|")
    rm = {'id': id,
            'naziv': naziv}
    return rm


#priprema string za upisivanje u fajl
def rm2str(rad):   
    return '|'.join([rad['id'], rad['naziv']])
    

#trazi radno mesto po nazivu
def findRadnoMesto(naziv): 
    for rm in radnaMesta:
        if rm['naziv'] == naziv:
            return True
    return False


print(__name__)  
radnaMesta = []
loadRadnaMesta() 
