from turtle import Turtle

class Paddle():
    def __init__(self):
        self.x = -40
        self.paddle = Turtle()
        self.paddle.penup()
        self.paddle.color("white")
        self.paddle.shape("square")
        self.paddle.sety(-180)
        self.paddle.shapesize(stretch_len=6, stretch_wid=1)


    def left(self):
        self.paddle.setheading(180)
        self.paddle.forward(20)
        
    def right(self):
        self.paddle.setheading(0)
        self.paddle.forward(20)
