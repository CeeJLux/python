# Setting up a Simple Game with Turtle
import turtle

# Background
wn = turtle.Screen()
wn.bgcolor("Black")

# Player
player = turtle.Turtle()
player.color("green")
player.shape("square")
player.penup()

speeed = 1

while True:
    player.forward(speeed)





delay = input("Press Enter to Exit")