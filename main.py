import turtle as t
from snake import Snake, WIDTH, HEIGHT
from food import Food
from scoreboard import Scoreboard
from time import sleep

""" SET GAME DIFFICULTY BELOW (EASY/MEDIUM/HARD) """
EASY = 1
MEDIUM = 2
HARD = 3
DIFFICULTY = MEDIUM

# set up game
screen = t.Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

# create snake
snake = Snake()
# create food
food = Food()
# create scoreboard
scoreboard = Scoreboard()

# set up keybinds
screen.listen()
screen.onkeypress(snake.up, 'Up')
screen.onkeypress(snake.up, 'w')
screen.onkeypress(snake.down, 'Down')
screen.onkeypress(snake.down, 's')
screen.onkeypress(snake.left, 'Left')
screen.onkeypress(snake.left, 'a')
screen.onkeypress(snake.right, 'Right')
screen.onkeypress(snake.right, 'd')

game_on = True
while game_on:
    screen.update()
    sleep(0.1)

    snake.move()
    # detect eating food
    if snake.head.distance(food) < 15:
        food.refresh()
        for _ in range(DIFFICULTY):
            snake.grow()
        scoreboard.increase_score()

    # detect wall collision
    if (snake.head.ycor() > (HEIGHT/2) or snake.head.ycor() < (-HEIGHT/2 + 15)
            or snake.head.xcor() > (WIDTH/2 - 15) or snake.head.xcor() < (-WIDTH/2)):
        scoreboard.reset()
        snake.reset()

    # detect tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
