import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(player.move_up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.car_move()
    screen.update()
    if player.ycor() > 270:
        scoreboard.player_point()
        car_manager.increase_speed()
        player.restart()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False



screen.exitonclick()
