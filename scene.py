from turtle import*
import time

def sky ():
	pendown()
	pencolor("LightSkyBlue")
	fillcolor("LightSkyBlue")
	forward(711)
	left(90)
	forward(410)
	left(90)
	
def grass ():
	pencolor("green")
	fillcolor("green")
	pendown()
	forward(711)
	right(90)
	forward(300)
	right(90)
	
def houses(color):
	fillcolor(color)
	pendown()
	pencolor(color)
	forward(50)
	left(90)
	forward(60)
	left(45)
	forward(35)
	left(90)
	forward(35)
	left(45)
	forward(60)
	left(90)
	forward(50)

def body ():
	pendown()
	shape("turtle")
	shapesize(1,1,1)
	fillcolor("blue")
	time.sleep(1)

def mult ():
	stamp()
	right(45)
	forward(30)
	stamp()
	left(90)
	forward(30)
	


penup()
goto(-360, -50)
begin_fill()
speed(15)
for s in range(2):
	sky()
end_fill()

penup()
goto(-360,-50)
begin_fill()
speed(15)
for i in range(2):
	grass()
end_fill()

speed(15)
for j in range (5):
	begin_fill()
	houses("blue")
	end_fill()
	begin_fill()
	houses("firebrick")
	end_fill()
	begin_fill()
	houses("gold")
	end_fill()

penup()
goto(-50, -200)
speed(1)
begin_fill()
body()
end_fill()
penup()

for m in range (10):
	mult()



	
	