from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Set up screen
screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)


# Create multiple paddles
r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))


# Create a ball at the center of the screen
ball = Ball()

# Create a scoreboard
scoreboard = Scoreboard()


# Movement of the paddles
screen.listen()
screen.onkeypress(r_paddle.move_up, 'Up')
screen.onkeypress(r_paddle.move_down, 'Down')
screen.onkeypress(l_paddle.move_up, 'w')
screen.onkeypress(l_paddle.move_down, 's')


# Create a counter variable
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()
