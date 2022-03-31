from turtle import Turtle
ALIGN = 'left'
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(-270, 270)
        self.pencolor('black')
        self.pendown()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Level: {self.score}', align=ALIGN, font=FONT)

    def score_up(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

