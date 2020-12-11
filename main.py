from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Setting up the screen of the game along with a title
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
# tracer helps run the animation of the snake smoothly

snake = Snake()
food = Food()
scoreboard= Scoreboard()

# for OOP, the snake and food class have to be called


# These commands makes the screen listen for the keyboard strokes listed and calls upon the snake class to carry it out
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Runs until the user loses
game_on = True
while game_on:
    snake.move()
    screen.update()
    time.sleep(0.05)

    # Detecting snake's head collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detecting snake's collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    # Detecting snake's collision with its tail
    for segment in snake.snake_segment[1:]:
        if snake.head.distance(segment) < 15:
            game_on = False
            scoreboard.game_over()


screen.exitonclick()
