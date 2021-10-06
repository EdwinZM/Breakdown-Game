from turtle import Turtle

class Ball():
    def __init__(self):
        self.ball = Turtle()
        self.ball.penup()
        self.ball.shape("circle")
        self.ball.color("Purple")
        self.ball.shapesize(.75)
        self.x = 1.5
        self.y = -3

    def move(self):
        x = self.ball.xcor() + self.x
        y = self.ball.ycor() + self.y
        self.ball.setx(x)
        self.ball.sety(y)

    def bounce_x(self):
        self.x *= -1

    def bounce_y(self):
        self.y *= -1
        