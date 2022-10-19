# Setting up a Simple Game with Turtle
import turtle
import math
import random

# Background
wn = turtle.Screen()
wn.bgcolor("gray")

#Border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

# Player
player = turtle.Turtle()
player.color("darkgreen")
player.shape("classic")
player.penup()
player.speed(0)

#goal
goal = turtle.Turtle()
goal.color("navy")
goal.shape("circle")
goal.penup()
goal.speed(0)
goal.setposition(-300, 300)

speed = 1
#controls
def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increasespeed():
    global speed
    speed += 1

def reducespeed():
    global speed
    speed -= 1

def Collission(t1, t2):
    d = math.sqrt(math.pow(player.xcor()-goal.xcor(),2) + math.pow(player.ycor()-goal.ycor(),2))
    if d < 20:
        return True
    else:
        return False

#keyboard linking
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")
turtle.onkey(reducespeed, "Down")

while True:
    player.forward(speed)

     #Border Checking
    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)

    if player.ycor() > 300 or player.ycor() < -300:
        player.right(180)

    #Collission

    if Collission(player, goal):
        goal.setposition(random.randint(-300, 300), random.randint(-300, 300))


delay = input("Press Enter to Exit")