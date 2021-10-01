from turtle import Turtle

class Ball():
    def __init__(self):
        self.ball = Turtle()
        self.ball.penup()
        self.ball.shape("circle")
        self.ball.color("Purple")
        self.ball.shapesize(.75)
        self.angle = -90

    def move(self):
        self.ball.setheading(self.angle)
        self.ball.forward(5)

    def bounce(self):
        if self.angle == 0:
            self.angle = 180
        elif self.angle == 180:
            self.angle = 0
        else:
            self.angle *= -1
        self.ball.setheading(self.angle)
        self.ball.forward(5)