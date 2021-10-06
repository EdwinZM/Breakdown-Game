import turtle 
import time
from paddle import Paddle
from ball import Ball
from bricks import Bricks

turtle.bgcolor("black")
turtle.tracer(False)

paddle = Paddle()
ball = Ball()
bricks = Bricks()

turtle.update()

turtle.listen()

turtle.onkey(paddle.left, "Left")
turtle.onkey(paddle.right, "Right")
turtle.onkey(paddle.left, "a")
turtle.onkey(paddle.right, "d")
      

is_on = True


while is_on:
    ball.move()

    if round(ball.ball.ycor()) == round(paddle.paddle.ycor()) + 15 and (round(ball.ball.xcor()) >= round(paddle.paddle.xcor()) - 60 and round(ball.ball.xcor()) <= round(paddle.paddle.xcor()) + 70):
        ball.bounce_y()
        
    elif ball.ball.ycor() == 300:
        ball.bounce_y()
    elif ball.ball.xcor() == -300 or ball.ball.xcor() == 300:
        ball.bounce_x()
    elif ball.ball.ycor() < -300:
        is_on = False

    brick_groups = [bricks.bricks1, bricks.bricks2, bricks.bricks3]

    finished_groups = 0
    
    for group in brick_groups:
        for brick in group:
            # if round(ball.ball.ycor()) == round(brick.ycor()) and (round(ball.ball.xcor()) >= round(brick.xcor()) - 50 and round(ball.ball.xcor()) <= round(brick.xcor()) + 50):
            if ball.ball.ycor() >= brick.ycor() -25:
                if ball.ball.xcor() >= brick.xcor() -25:
                    if ball.ball.xcor() <= brick.xcor() +25:
                        ball.bounce_y()
                        bricks.hit(brick)
                        break
            
        if len(group) <= 0:
            finished_groups += 1

    if finished_groups == 3:
        is_on = False


    turtle.update()

turtle.Screen().exitonclick()