"""planets.py: Description of how planets work.

__author__ = "Lvjiawen"
__pkuid__  = "1600012173"
__email__  = "1600012173@pku.edu.cn"
"""


import turtle
import math



def orbit(x,y):
    """orbital function
    """
    global a
    x.goto(y*math.cos(100*a/y*math.pi/360),0.5*y*math.sin(100*a/y*math.pi/360))




planet_name=["Mer","Ven","Ear","Mars","Jup","Sat"]
planet_radius=[100,150,200,250,300,350]
planet_colors=[ 'yellow', 'blue', 'green', 'orange', 'purple',"black"]






sun=turtle.Turtle()
sun.shape("circle")
sun.setpos(-30,0)
sun.color("red")
sun.dot(50,"red")




Mer=turtle.Turtle()
Mer.shape("circle")
Mer.color(planet_colors[0])
Mer.pencolor(planet_colors[0])
Mer.pu()
Mer.goto(planet_radius[0],0)
Mer.pd()
Mer.speed(60/50**0.5)



Ven=turtle.Turtle()
Ven.shape("circle")
Ven.color(planet_colors[1])
Ven.pencolor(planet_colors[1])
Ven.pu()
Ven.goto(planet_radius[1],0)
Ven.pd()
Ven.speed(60/100**0.5)



Ear=turtle.Turtle()
Ear.shape("circle")
Ear.color(planet_colors[2])
Ear.pencolor(planet_colors[2])
Ear.pu()
Ear.goto(planet_radius[2],0)
Ear.pd()
Ear.speed(60/150**0.5)



Mars=turtle.Turtle()
Mars.shape("circle")
Mars.color(planet_colors[3])
Mars.pencolor(planet_colors[3])
Mars.pu()
Mars.goto(planet_radius[3],0)
Mars.pd()
Mars.speed(60/200**0.5)

Jup=turtle.Turtle()
Jup.shape("circle")
Jup.color(planet_colors[4])
Jup.pencolor(planet_colors[4])
Jup.pu()
Jup.goto(planet_radius[4],0)
Jup.pd()
Jup.speed(60/250**0.5)



Sat=turtle.Turtle()
Sat.shape("circle")
Sat.color(planet_colors[5])
Sat.pencolor(planet_colors[5])
Sat.pu()
Sat.goto(planet_radius[5],0)
Sat.pd()
Sat.speed(60/300**0.5)

"""main codes for the orbital parameter"""




a=0
while 1:
    """input the planet's name and orbit radius
    """
    orbit(Mer,100)
    orbit(Ven,150)
    orbit(Ear,200)
    orbit(Mars,250)
    orbit(Jup,300)
    orbit(Sat,350)
    a=a+1



if __name__ == '__main__':
    main()











