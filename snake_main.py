from turtle import Screen
from snake import Snake
from food import Food
from scorebored import Score
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")


game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extendsegements()
        score.increasecore()

    # detect collision with wall
    if snake.head.xcor() > 395 or snake.head.xcor() < -395 or snake.head.ycor() > 390 or snake.head.ycor() < -390:
        # trigger game_over sequence
        score.game_continue()
        game_on = screen.textinput(title="Game Over", prompt="Do you want to Continue? Y/N ").lower()
        if game_on == "y":
            score.reset_score()
            snake.reset_snake()
        else:
            exit("See you later!!!")

    # detect collision with tail
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) <= 10:  # if head collides with any segment
            # trigger game_over sequence
            score.game_continue()
            game_on = screen.textinput(title="Game Over", prompt="Do you want to Continue? Y/N ").lower()
            if game_on == "y":
                score.reset_score()
                snake.reset_snake()
            else:
                exit("See you later!!!")

screen.exitonclick()
