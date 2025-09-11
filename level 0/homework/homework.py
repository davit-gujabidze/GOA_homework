from turtle import *

width(4)
color("red")
backward(150)
left(90)
forward(150)
right(90)
forward(150)
right(90)
forward(150)
back(150)   #walls

color("green")
right(135)
forward(105)
left(90)
forward(109)  #roof

color("red")
left(45)
forward(147)
left(90)
forward(55)  #misc

color("orange")
left(90)
forward(70)
right(90)
forward(40)
right(90)
forward(70)  #door

back(70)
color("gray")
back(10)  #misc

color("blue")
back(40)
left(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
back(20)
right(90)
forward(40)
back(20)
right(90)
forward(20)
back(40)  #window 1

right(90)
forward(20)
color("white")
forward(10)
color("orange")
right(90)
forward(40)
right(90)
color("white")
forward(50)
left(90)
forward(40)  #misc

color("blue")
back(40)
left(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
back(20)
right(90)
forward(40)
back(20)
right(90)
forward(20)
back(40)  #window 2

exitonclick()