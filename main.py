import turtle
from random import random, randint

turtle.bgcolor("#fff")

t = turtle.Turtle()

t.speed(0)
t.shape("turtle")
t.color("black", "green")

t.penup()
#t.goto(-300, -300)
t.pendown()


t.speed(10)

turtles = [t]

#for i in range (20):
while (True):
	for i in turtles:
		a = 90 * random()
		
		if turtles.index(i) == 9:
			i.circle(a)
		else:
			i.left(a)
			i.forward(50)
		
		if a > 80 and len(turtles) < 10:
			p = i.clone()
			#color = "#%06x" % randint(0, 0xFFFFFF)
			color = '#{:02x}{:02x}{:02x}'.format(randint(0,150), 255, randint(0,100))
			p.color("black", color)
			turtles.append(p)
		#t.right(a)


#how to save to file
#ts = turtle.getscreen()
#ts.getcanvas().postscript(file="duck.eps")

#pause
z = input()