from turtle import Turtle

class Bricks():
    def __init__(self):
        self.x = -280
        self.y = 250
        self.bricks1 = self.set_bricks()
        self.bricks2 = self.set_bricks()
        self.bricks3 = self.set_bricks()

    def add_brick(self):
        brick = Turtle()
        brick.penup()
        brick.shape("square")
        brick.color("white")
        brick.shapesize(stretch_len=4, stretch_wid=1)
        brick.setx(self.x)
        brick.sety(self.y)
        return brick

    def set_bricks(self):

        brick_lane = [self.add_brick()]

        while brick_lane[-1].xcor() <= 250:
            self.x += 90
            brick = self.add_brick()
            brick.setx(self.x)
            brick_lane.append(brick)

        self.x = -280
        self.y -= 30
                


        







