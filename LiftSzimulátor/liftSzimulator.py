import fileManager
import rajz
import statisztika


ido = 0
kiszolgalt = []
felsoEmelet = 99
alsoEmelet = 0
    
class Szemely:
    def __init__(self, kg, erkezesIdo, honnan,  hova):
        self.kg = int(kg)
        self.erkezesIdo = int(erkezesIdo)
        self.honnan = int(honnan)
        self.hova = int(hova)
        self.varakozasIdo = 0
        self.utazasIdo = 0
        self.hivott = False

class Lift:
    def __init__(self, teherb, szint, irany):
        self.teherb = int(teherb)
        self.jelenlegiTeher = 0
        self.szint = int(szint)
        self.irany = int(irany)
        self.szemelyek = []
        self.celEmeletek = []
        self.felvett = 0


def melyikIrany(lift, honnan):
    '''Eldönti, hogy a megadott lift a honnan szint irányába mozog vagy onnan el'''
    return (lift.szint < honnan and lift.irany > 0) or (lift.szint > honnan and lift.irany < 0)

def dontes(lista1, lista2):
    '''Magalgoritmus: a két lift célEmeletek listáját összehasonlítva, eldönti melyik liftet mozgassuk (kevesebb elemszamút mozgatjuk)'''
    if len(lista1) > len(lista2): #döntünk a lista hosszát összehasonlítva, ha egyenlő a másodikat küldjük
        return 0
    return 1

def lifthezAdas(lista, ertek):
    '''Hozzáad a listához egy elemet, ha az, azt az elemet még nem tartalmazza'''
    if not ertek in lista:
        lista.append(ertek)

    return lista
            

def kiszallas(liftek, iv):
    '''A kiszállást lebonyolító függvény'''
    global ido
    kiszallt = False #flag a szinkronizáció miatt
    for p in range(0, 2):
        q = 0
        while q < len(liftek[p].szemelyek):
            if(liftek[p].szemelyek[q].hova == liftek[p].szint): #ha egy utasnak ki kell szállnia a jelenlegi szinten
                liftek[p].szemelyek[q].utazasIdo = ido - (liftek[p].szemelyek[q].erkezesIdo + liftek[p].szemelyek[q].varakozasIdo) #elmentjük az utazási időt
                kiszallt = True
                liftek[p].jelenlegiTeher -= liftek[p].szemelyek[q].kg #a súly levétele a lift jelenlegi teherjéből
                kiszolgalt.append(liftek[p].szemelyek[q]) #az utast feldolgoztuk
                liftek[p].szemelyek.pop(q) #eltávolítjuk az utast a liftből
                q -= 1
            q += 1

    if kiszallt:
        ido += 1 #növeljük az időt, hogy liftelhagyás történt
        iv = False

def beszallas(liftek, szemelyek, iv):
    '''A beszállást lebonyolító függvény'''
    global ido
    kozelibb = 0
    beszallt = False
    
    for sz in szemelyek:
        if(sz != 0): #ha egy valódi utas(nem volt még eltávolítva a szemelyek listából)                      
            #egy utas érkezik, de nincs olyan lift ami kész lenne felvenni
            if sz.erkezesIdo <= ido and sz.hivott == False:

                #megnézzük a legközelebi liftet
                kul1 = abs(sz.honnan - liftek[0].szint)
                kul2 = abs(sz.honnan - liftek[1].szint)
                
                #ha egyik lift sem mozog, a közelibbet mozgatjuk
                if(liftek[0].irany == 0) and (liftek[1].irany == 0):
                    if (kul1 < kul2):
                        kozelibb = 0
                    elif (kul1 > kul2):
                        kozelibb = 1
                    else: #ha ugyanakkora távolságra vannak a 0. indexűt mozgatjuk
                        kozelibb = 0
                
                #mindkét lift mozog
                elif (liftek[0].irany != 0) and (liftek[1].irany != 0):
                    if (kul1 < kul2) and melyikIrany(liftek[0], sz.honnan): #ha az első közelebb van és az ő irányába mozog
                        kozelibb = 0
                    elif (kul1 < kul2) and not melyikIrany(liftek[0], sz.honnan):# ha az első közelebb van de tőle el mozog
                        if melyikIrany(liftek[1], sz.honnan):   #ha a másik lift az ő irányába mozog
                            kozelibb = 1                    
                        else: #ha mindkettő tőle el mozog
                            kozelibb = dontes(liftek[0].celEmeletek, liftek[1].celEmeletek) #a kevesebb cél emelettel rendelkezőt mozgatjuk
                    elif (kul1 > kul2) and melyikIrany(liftek[1], sz.honnan): #ha a második közelebb van és az ő irányába mozog
                        kozelibb = 1
                    elif (kul1 > kul2) and not melyikIrany(liftek[1], sz.honnan): # ha a második közelebb van de tőle el mozog
                        if melyikIrany(liftek[0], sz.honnan):# ha a másik lift az ő irányába mozog
                            kozelibb = 0
                        else: #ha mindkettő tőle el mozog
                            kozelibb = dontes(liftek[0].celEmeletek, liftek[1].celEmeletek)
                    elif kul1 == kul2: #ha ugyanakkora távolságra vannak
                        if melyikIrany(liftek[0], sz.honnan): #ha az első az ő irányába mozog
                            kozelibb = 0
                        elif melyikIrany(liftek[1], sz.honnan): #ha a második az ő irányába mozog
                            kozelibb = 1
                        else: #ha mindkettő tőle el mozog
                            kozelibb = dontes(liftek[0].celEmeletek, liftek[1].celEmeletek)
                            
                #egyik lift sem mozog
                elif ((liftek[0].irany != 0) and (liftek[1].irany == 0)) or ((liftek[0].irany == 0) and (liftek[1].irany != 0)):
                    if liftek[0].irany == 0:
                        kozelibb = 0
                    else:
                        kozelibb = 1

                liftek[kozelibb].celEmeletek = lifthezAdas(liftek[kozelibb].celEmeletek, sz.honnan)#itt hívjuk a liftet, hozzáadjuk az utas kezdőszintjét a cél emelethez
                sz.hivott = True


            #az utas beszáll a liftbe           
            if (sz.erkezesIdo <= ido) and (((len(liftek[0].celEmeletek) != 0) and ((liftek[0].szint == sz.honnan) and (liftek[0].celEmeletek[0] == liftek[0].szint))) or ((len(liftek[1].celEmeletek) != 0) and ((liftek[1].szint == sz.honnan) and (liftek[1].celEmeletek[0] == liftek[1].szint)))):
                if (liftek[0].szint == sz.honnan):
                    valasztott = 0
                elif (liftek[1].szint == sz.honnan):
                    valasztott = 1
                beszallt = True
                sz.varakozasIdo = ido - sz.erkezesIdo #várakozási idő számolása               
                liftek[valasztott].jelenlegiTeher += sz.kg  #hozzáadjuk a súlyt
                if liftek[valasztott].jelenlegiTeher < liftek[valasztott].teherb: #megnézzük hogy nem túlsúlyos
                    liftek[valasztott].szemelyek.append(sz) #hozzáadjuk az utast a lift listájához
                    liftek[valasztott].celEmeletek = lifthezAdas(liftek[valasztott].celEmeletek, sz.hova)#hozzáadjuk a cél emeletek közé a végső szintet
                    liftek[valasztott].felvett += 1
                    szemelyek[szemelyek.index(sz)] = 0 #eltávolítjuk az utast a szemelyek listából
                else:#ha túlsúlyos, az utas újrahívja a liftet
                    liftek[valasztott].jelenlegiTeher -= sz.kg #visszaveszzük a súlyt
                    sz.hivott = False
                    
                
    if beszallt:
        ido += 1 #növeljük az időt, hogy liftbe szállás történt
        iv = False

def mozgatas(liftek, iv):
    '''A mozgatást lebonyolító függvény'''
    global ido            
    for r in range(0, 2): 
        if len(liftek[r].celEmeletek) != 0:#megnézzük hogy van-e célemelet
            if liftek[r].celEmeletek[0] == liftek[r].szint: #ha a célemelet első eleme megegyezik az adott szinttel
                liftek[r].celEmeletek.pop(0) #pop az első cél emeletet

        if len(liftek[r].celEmeletek) != 0:
            #sort figyelembe véve a lift irányát
            if liftek[r].irany == 1:
                kisebbek = []
                e = 0
                while e < len(liftek[r].celEmeletek):
                    if liftek[r].celEmeletek[e] < liftek[r].szint:
                        kisebbek.append(liftek[r].celEmeletek[e])
                        liftek[r].celEmeletek.pop(e)
                        e -= 1
                    e += 1
                liftek[r].celEmeletek.sort()
                for k in kisebbek:
                    liftek[r].celEmeletek.append(k)
            elif liftek[r].irany == -1:
                nagyobbak = []
                e = 0
                while e < len(liftek[r].celEmeletek):
                    if liftek[r].celEmeletek[e] > liftek[r].szint:
                        nagyobbak.append(liftek[r].celEmeletek[e])
                        liftek[r].celEmeletek.pop(e)
                        e -= 1
                    e += 1
                liftek[r].celEmeletek.sort(reverse = True)
                for n in nagyobbak:
                    liftek[r].celEmeletek.append(n)

            if liftek[r].celEmeletek[0] > liftek[r].szint: #ha maradt elem a cél emeletekben akkor újrakonfiguráljuk az irányt
                liftek[r].irany = 1
            elif liftek[r].celEmeletek[0] < liftek[r].szint:
                liftek[r].irany = -1
        else:
            liftek[r].irany = 0 #ha nincs több emelet megállítjuk a liftet
        
        liftek[r].szint += liftek[r].irany #mozgatjuk a lifteket

        if (liftek[0].irany != 0) or (liftek[1].irany != 0):
                rajz.kijelzoRajz(liftek[r].szint, r) #rajzolás

        #hibakezelés        
        if liftek[r].szint > felsoEmelet :
            liftek[r].szint = felsoEmelet
            raise ValueError
        elif  liftek[r].szint < alsoEmelet:
            print(liftek[r].szint)
            liftek[r].szint = alsoEmelet
            raise ValueError      
            
    if iv:
        ido += 1

def main():
    rajz.teljesRajz()
    rajz.kijelzoRajz(0, 0)
    rajz.kijelzoRajz(0, 1)
    szemelyek = []
    idoValtozas = True

    #fájl olvasás
    try:
        with open("szimulacio.txt") as f:
            for line in f:
                line = line.split(';')
                uj = Szemely(line[0], line[1], line[2], line[3])
                szemelyek.append(uj)               
    except FileNotFoundError:
        print("A fájl nem található, a szimuláció nem futtatható!")

    liftek = [Lift(500, 0, 0), Lift(500, 0, 0)]
    szemelyek = sorted(szemelyek, key=lambda szemely: szemely.erkezesIdo)
    print("Fájl feldolgozás sikeres!")
    print("Szimuláció folyamatban...")
    
    while len(szemelyek) != len(kiszolgalt) and ido < 18000: #17280 = 24 órában 17280 db 5 mp van
        idoValtozas = True

        #megnézzük az összes utast a lidtben, ki kell-e szállniuk
        kiszallas(liftek, idoValtozas)

        #megnézzük az összes utast a lidtben, be kell-e szállniuk és döntünk hogy mozgassuk a lifteket
        beszallas(liftek, szemelyek, idoValtozas)

        #ténylegesen mozgatjuk a lifteket vagy hagyjuk hogy teljen az idő
        try:
            mozgatas(liftek, idoValtozas)
        except ValueError:
            print("A lift nem létező emeleten van!")
            
    print("Statisztika készítése...")
    statisztika.szerkesztes(kiszolgalt, liftek[0].felvett, liftek[1].felvett) #statisztika készítése
    print("Befejezve. Szimuláció lefuttatva.")
    print("A kilépéshez nyomj Enter-t...")
    input()

main()
