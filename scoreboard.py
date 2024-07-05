from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.level = 0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.goto(-220,250)
        self.write(f"LEVEL: {self.level}", align="center", font=("Courier", 24, "normal"))
    def player_point(self):
        self.level += 1
        self.update_scoreboard()
