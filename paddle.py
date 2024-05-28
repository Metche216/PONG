from turtle import Turtle

class Paddle (Turtle):
    def __init__(self, xpos):
        super().__init__()
        
        self.shape('square')
        self.resizemode('user')
        self.shapesize(5,1)
        self.goto(x=xpos, y=0)
        self.penup()
        self.color('white')
        
        
    def up(self):
        if self.ycor() < 250:
            self.goto(x= self.xcor(), y= self.ycor()+20)
        
    def down(self):
        if self.ycor() > -230:
            self.goto(x= self.xcor(), y= self.ycor()-20)