import random

class Szemely:
    def __init__(self, kg, erkezesIdo, honnan,  hova, felvett):
        self.kg = int(kg)
        self.erkezesIdo = int(erkezesIdo)
        self.honnan = int(honnan)
        self.hova = int(hova)
        self.felvett = felvett

def endfloor(kezdo):
    val = random.randint(0,12)
    if val == kezdo:
        val = endfloor(kezdo)
    return val


def randomizer():
    with open("szimulacio.txt", "a") as f:
        for i in range(0, 1001):
            kezdo = random.randint(0,12)
            veg = endfloor(kezdo)
            uj = "{0};{1};{2};{3}".format(random.randint(50,200), random.randint(0,17000), kezdo, veg)
            f.write(uj + "\n")

randomizer()
