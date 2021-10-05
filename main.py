import turtle 
from paddle import Paddle
from ball import Ball
from bricks import Bricks

turtle.bgcolor("black")
turtle.tracer(False)

paddle = Paddle()
ball = Ball()
bricks = Bricks()

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
        ball.ball.setx(0)
        ball.ball.sety(0)
          

    turtle.update()

turtle.Screen().exitonclick()