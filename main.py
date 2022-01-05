import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
car_manager = CarManager()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("gray")
screen.tracer(0)
player = Player()
score = Scoreboard()
game_is_on = True
screen.listen()
screen.onkeypress(fun=player.move , key="Up")


while game_is_on:

    time.sleep(0.1)
    screen.update()
    car_manager.generate_cars()
    car_manager.move()
    for car in car_manager.cars:
        if player.distance(car) <= 20:
            game_is_on = False
            score.gameover()
    if player.ycor() >= 300:
        score.passed()
        score.increasing_level()
        player.goto(y = -280 , x = 0)
        car_manager.increase_speed()



screen.exitonclick()