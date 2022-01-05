from turtle import  Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def generate_cars(self):
        DICE = random.randint(1,6)
        if DICE == 2:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.setheading(180)
            car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            car.goto(300,random_y)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.speed)
    def increase_speed(self):
        self.speed += MOVE_INCREMENT


