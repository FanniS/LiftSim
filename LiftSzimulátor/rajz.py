import turtle

kijelzoTurtle1 = turtle.Turtle()
kijelzoTurtle2 = turtle.Turtle()
kijelzoTurtle1.hideturtle()
kijelzoTurtle2.hideturtle()

def szamRajz(szam, kijelzoTurtle):
    '''Kirajzolja a kijelzőre a számokat'''
    zold = "#32ee00"
    kijelzoTurtle.color(zold)
    style = ("Bahnschrift SemiLight", 36, "normal")
    kijelzoTurtle.write(szam, False, align= "center", font=style)

def kijelzoRajz(emelet, lift):
    '''Meghívja a számrajzolást a megfelelő helyre'''
    if lift == 0:
        kijelzoTurtle1.clear()
        kijelzoTurtle1.up()
        kijelzoTurtle1.setposition(-250, 310)
        kijelzoTurtle1.down()
        szamRajz(emelet, kijelzoTurtle1)        
        
    else:
        kijelzoTurtle2.clear()
        kijelzoTurtle2.up()
        kijelzoTurtle2.setposition(250, 310)
        kijelzoTurtle2.down()
        szamRajz(emelet, kijelzoTurtle2)
    

def liftRajz(szelesseg, magassag, perem):
    '''Megrajzolja a liftet'''
    turtle.forward(szelesseg)
    turtle.left(90)
    turtle.forward(magassag)
    turtle.left(90)
    turtle.forward(szelesseg)
    turtle.left(90)
    turtle.forward(magassag)
    turtle.left(90)

    turtle.forward(perem)
    turtle.left(90)
    turtle.forward(magassag-perem)
    turtle.right(90)
    turtle.forward(szelesseg-2*perem)
    turtle.right(90)
    turtle.forward(magassag-perem)
    turtle.right(90)
    turtle.forward(szelesseg/2 - perem)
    turtle.right(90)
    turtle.forward(magassag-perem)
    turtle.right(90)

def gombRajz(szelesseg, magassag, x, y):
    '''Megrajzolja a gombokat'''
    turtle.forward(szelesseg)
    turtle.left(90)
    turtle.forward(magassag)
    turtle.left(90)
    turtle.forward(szelesseg)
    turtle.left(90)
    turtle.forward(magassag)
    turtle.left(90)

    turtle.up()
    turtle.setposition( x-10, y-5)
    turtle.down()
    
    for t in range(0,3):
        turtle.forward(szelesseg-(x+30))
        turtle.right(120)

    turtle.up()
    turtle.setposition( x-10, y+5)
    turtle.down()

    for t in range(0,3):
        turtle.forward(szelesseg-(x+30))
        turtle.left(120)       

def kijelzoKeretRajz(szelesseg, magassag):
    '''Megrajzolja a kijelző keretét'''
    turtle.forward(szelesseg)
    turtle.left(90)
    turtle.forward(magassag)
    turtle.left(90)
    turtle.forward(szelesseg)
    turtle.left(90)
    turtle.forward(magassag)
    turtle.left(90)

def teljesRajz():
    #Alapbeállítás
    ablak = turtle.Screen()
    ablak.title("Lift Szimulátor")
    ablak.setup(1200, 750)
    turtle.width(3)
    turtle.speed(0)

    #Talaj rajzolása
    turtle.up()
    turtle.setposition(-600, -300)
    turtle.down()
    turtle.forward(1200)

    #Liftek rajzolása
    turtle.up()
    turtle.setposition(-450, -300)
    turtle.down()

    liftRajz(400, 600, 50)

    turtle.up()
    turtle.setposition(50, -300)
    turtle.down()

    liftRajz(400, 600, 50)   

    #Nyomógomb rajzolása
    turtle.up()
    turtle.setposition( -25, -25)
    turtle.down()
    
    gombRajz(50, 50, 0, 0)

    #Kijelző rajzolása
    turtle.up()
    turtle.setposition(-290, 310)
    turtle.down()

    kijelzoKeretRajz(80,50)

    turtle.up()
    turtle.setposition(210, 310)
    turtle.down()

    kijelzoKeretRajz(80,50)
    turtle.hideturtle()
  

