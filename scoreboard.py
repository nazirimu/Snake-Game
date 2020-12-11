from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Comic Sans", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 275)
        self.write(f"SCORE: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write(f"GAME OVER!\nFINAL SCORE:{self.score}", move=False, align=ALIGNMENT,
                   font=("Comic Sans", 30, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE: {self.score}", move=False, align=ALIGNMENT, font=FONT)
