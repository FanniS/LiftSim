def ujSzemely():
    '''Új személy adatainak felvitele'''
    kg = int(input("Adja meg a személy súlyát!"))
    if kg < 0 or kg > 200:
        raise ValueError
    ido = input("Adja meg a lifthez érkezés idejét!")
    try:
        ido = ido.split(':') #5 mp-s időközökkel dolgozom, ezért kell a 720
        if int(ido[0]) < 0 or int(ido[0]) > 24 or int(ido[1]) < 0 or int(ido[1]) > 60:
            raise ValueError
        erkezesIdo = int(ido[0]) * 720 + int(ido[1]) * 12
    except:
        raise ValueError
    honnan = int(input("Adja meg a kezdő emeletet!"))
    if honnan < 0 or honnan > 99:
        raise ValueError
    hova = int(input("Adja meg az elérni kívánt emeletet!"))
    if hova < 0 or hova > 99:
        raise ValueError
    
    uj = "{0};{1};{2};{3}".format(kg, str(erkezesIdo), honnan, hova)
    return uj

def mentes(uj):
    with open(("szimulacio.txt"), "a") as f:
        f.write(uj + "\n")

def menu():
    '''Menü megjelenítése'''
    print("--Menu--")
    print("1 - Új személy létrehozása")
    print("2 - Mentés és szimuláció kezdése")
    valasztas = int(input())
    return valasztas

def main():
    while menu() != 2:
        try:
            uj = ujSzemely()
            mentes(uj)
        except:
            print("Hibás bemenet!")
        
    

main()
