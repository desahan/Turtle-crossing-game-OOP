from turtle import Turtle
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.write(f"LEVEL {self.level}", font=FONT)

    def add_level(self):
        self.level += 1
        self.clear()
        self.write(f"LEVEL {self.level}", font=FONT)

    def game_over(self):
        self.penup()
        self.goto(-100, 0)
        self.write("GAME OVER", font=FONT)
