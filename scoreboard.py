from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.level = 0
        self.goto(x=-260, y=260)
        self.write(f"Level = {self.level}", move=False, font=FONT)
    def passed(self):
        self.goto(x=0, y=0)
        self.write("succeed!", move=False, font=FONT)
    def gameover(self):
        self.goto(x=-60, y=0)
        self.write("GameOver", move=False, font=FONT)
    def increasing_level(self):
        self.clear()
        self.goto(x = -260 , y = 260)
        self.level += 1
        self.write(f"Level = {self.level}", move=False, font=FONT)







