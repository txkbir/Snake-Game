from turtle import Turtle
from snake import HEIGHT
ALIGN = 'center'
FONT = ('PT Mono', 16, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.get_highscore()
        self.color('white')
        self.hideturtle()
        self.pu()
        self.sety(HEIGHT/2 - 30)
        self.write_score()

    def write_score(self) -> None:
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.highscore}', False, align=ALIGN, font=FONT)

    def increase_score(self) -> None:
        self.score += 1
        self.write_score()

    def reset(self) -> None:
        if self.score > self.highscore:
            self.highscore = self.score
            self.update_highscore()
        self.score = 0
        self.write_score()

    def get_highscore(self) -> int:
        try:
            with open('data.txt', 'r') as file:
                self.highscore = file.read()
                return int(self.highscore)
        except FileNotFoundError:
            self.highscore = 0  # Set an initial highscore if the file doesn't exist
            self.update_highscore()  # Create the file and write the initial highscore
            return 0  # Return the initial highscore

    def update_highscore(self) -> None:
        with open('data.txt', mode='w') as file:
            file.write(str(self.highscore))
