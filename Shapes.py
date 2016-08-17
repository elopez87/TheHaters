from turtle import *
def square (side_length):
	for i in range (4):
		pendown()
		forward(side_length)
		right(90)
def triangle (side):
	for j in range (3):
		pencolor("DarkBlue")
		pendown()
		forward(side)
		right(120)
def draw_circle(color):
	pendown()
	pencolor(color)
	circle(150)
penup()
goto(-200,200)
penup()
speed(5)	
square(300)
penup()
goto(-200,-110)
speed(4)
triangle(150)
penup()
goto(-50,-110)
triangle(150)
penup()
goto(-50,-100)
draw_circle("DarkBlue")

