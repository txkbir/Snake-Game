from turtle import Turtle
from snake import WIDTH, HEIGHT
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape('circle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color('red')
        self.speed('fastest')
        self.refresh()

    def refresh(self) -> None:
        rand_x = random.randint(-WIDTH/2 + 20, WIDTH/2 - 20)
        rand_y = random.randint(-HEIGHT/2 + 20, HEIGHT/2 - 20)
        self.goto(rand_x, rand_y)
