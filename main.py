from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

my_snake = []

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    scoreboard.show_score()

    # Comerse la fruta
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    # Chocar con los bordes
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        scoreboard.reset()
        scoreboard.save_high_score()
        snake.reset()

    # Chocar con culebra
    for segment in snake.my_snake[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            scoreboard.save_high_score()
            snake.reset()

screen.exitonclick()
