from turtle import Turtle
import random

class Ball:
    
    def __init__(self,screen_height,screen_width):
        angle = random.randint(0,360)
        self.stepsize = 20
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.ball = Turtle("circle")
        self.ball.color("white")
        self.ball.shapesize(0.5,0.5)
        self.ball.penup()
        self.ball.setheading(angle)
        self.ball.speed(3)
        print(angle)

    
    def move(self):
        xcor = self.ball.xcor()
        ycor = self.ball.ycor()
        from_the_wall = 0
        print("move")
        if ycor < self.screen_height-from_the_wall and ycor > -self.screen_height+from_the_wall:
            if xcor < self.screen_width-from_the_wall and xcor > -self.screen_width+from_the_wall:
                self.ball.forward(self.stepsize)
            else:                
                print("-----")
                print(self.ball.position())
                print(self.ball.heading())
                print("turn")
                self.turn()
                print(self.ball.position())
                print("-----")

        else:
            print("-----")
            print(self.ball.position())
            print(self.ball.heading())           
            print("turn")
            self.turn()
            print(self.ball.position())
            print("-----")

    
    def turn(self):
        current_heading = self.ball.heading()
        
        if current_heading in range(0,90) or current_heading in range(180,270):
            new_angle = 180 - current_heading
        elif current_heading in range(90,180) or current_heading in range(270,360):
            new_angle = 360 - current_heading
        
        self.ball.setheading(new_angle)
        print(self.ball.heading())
        self.ball.forward(self.stepsize)
        
    def isover(self):
        pass
    #def if_hit_something(self,boudary):   
     #   for i in boudary:
            
