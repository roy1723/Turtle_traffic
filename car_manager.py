import random
from random import Random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.color(random.choice(COLORS))
            new_car.goto(295, random_y)
            self.all_cars.append(new_car)
        else:
            pass
    def car_move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT


