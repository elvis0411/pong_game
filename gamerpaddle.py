# this is the part that control the player's paddle

from turtle import Turtle

class Gamerpaddle():
        
    def __init__(self,screen_width,screen_height):        
        from_the_bondary = 10
        self.height = screen_height
        self.paddle_height = 2
        self.paddle = Turtle("square")
        self.paddle.color("white")
        self.paddle.shapesize(self.paddle_height,0.1)
        self.paddle.penup()
        self.paddle.setposition(-screen_width+from_the_bondary,0)
    def move_up(self):    
        print("move up")   
        xcor = self.paddle.xcor()
        ycor = self.paddle.ycor()
        print(ycor)
        if ycor < (self.height - self.paddle_height*10):
            self.paddle.goto(xcor,ycor+self.paddle_height*10)
    
    def move_down(self): 
        print("move down")      
        xcor = self.paddle.xcor()
        ycor = self.paddle.ycor()
        print(ycor)
        if ycor > (-self.height+ self.paddle_height*10):
            self.paddle.goto(xcor,ycor-10)