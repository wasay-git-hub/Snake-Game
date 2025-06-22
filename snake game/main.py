import turtle
import snake
import food
import scoreboard
import time

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Python Snake Game")
screen.tracer(0)

snake = snake.Snake()
screen.listen()

turtle.onkey(snake.left, "Left")
turtle.onkey(snake.right, "Right")
turtle.onkey(snake.up, "Up")
turtle.onkey(snake.down, "Down")

food = food.Food()
scoreboard = scoreboard.Scoreboard()

game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.place_food()
        scoreboard.increase_score()
        snake.extend_snake()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()