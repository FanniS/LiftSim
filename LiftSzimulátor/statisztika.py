def mentes(fajlnev, sor):
    '''Megírja a sort a fájlba'''
    with open((fajlnev), "a") as f:
        f.write(sor + "\n")
    
def szerkesztes(kiszolgaltak, felvett0, felvett1):
    '''Megfelelő formátumra alakírja az írni kívánt sort'''
    v=0
    u=0
    kiszolgaltak = sorted(kiszolgaltak, key = lambda szemely: szemely.erkezesIdo)
    maximumVarakozas = kiszolgaltak[0].varakozasIdo
    maximumUtazas = kiszolgaltak[0].utazasIdo
    for s in kiszolgaltak:
        if maximumVarakozas < s.varakozasIdo:
            maximumVarakozas = s.varakozasIdo
        if maximumUtazas < s.utazasIdo:
            maximumUtazas = s.utazasIdo
        ora = s.erkezesIdo//720
        perc = (s.erkezesIdo-(ora*720))//12
        s.erkezesIdo = "{0:02}:{1:02}".format(ora, perc)
        v += s.varakozasIdo*5
        u += s.utazasIdo*5
        uj = "{0}-kor, várakozási ideje: {1} mp, utazási ideje: {2} mp, {3}.szintről a {4}.szintre".format(s.erkezesIdo, s.varakozasIdo*5, s.utazasIdo*5, s.honnan, s.hova)
        mentes("statisztika.txt", uj)
        
    lift0 = "A 0. indexű lift {0} db utast vett fel".format(felvett0)
    mentes("statisztika.txt", lift0)
    lift1 = "A 1. indexű lift {0} db utast vett fel".format(felvett1)
    mentes("statisztika.txt", lift1)
    
    atlagVarakozas = v/len(kiszolgaltak)
    atlagUtazas = u/len(kiszolgaltak)
    atlagok = "Az átlag várakozási idő {0:.2f} mp, maximum várakozas {1} mp, az átlag utazási idő {2:.2f} mp, maximum utazás {3} mp".format(atlagVarakozas, maximumVarakozas*5, atlagUtazas, maximumUtazas*5)
    mentes("statisztika.txt", atlagok)

    
