#This is the part of the game that show the screen and captcher the keyboard input
from turtle import Screen, Turtle

screen_width = 300
screen_height = 400
main = Screen()
main.screensize(canvwidth=screen_width, canvheight= screen_height)
print(main.screensize())

main.bgcolor("black")
side_boundary = Turtle()
side_boundary.hideturtle()
side_boundary.pencolor("white")
main.tracer(0)

side_boundary.penup()
side_boundary.goto(0,screen_height)

dash_size = 10

side_boundary.right(90)

for i in range(int(screen_height/(dash_size))):
    side_boundary.pendown()
    side_boundary.forward(dash_size)
    side_boundary.penup()
    side_boundary.forward(dash_size)

main.update()




main.exitonclick()