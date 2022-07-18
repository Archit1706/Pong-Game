from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Mr. Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
# ball.move()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
# paddle.move_user()

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.ball_speed)

    # Detect collision with wall and bounce
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect when ball misses the right paddle
    if ball.xcor() >= 400:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when ball misses the left paddle
    if ball.xcor() <= -400:
        ball.reset_position()
        scoreboard.r_point()

    # Detect collision with both paddles
    if (ball.distance(l_paddle) < 50 and ball.xcor() < -320) or (ball.distance(r_paddle) < 50 and ball.xcor() > 320):
        ball.bounce_x()


screen.exitonclick()
