import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()

scoreboard = Scoreboard()

screen.onkey(player.move, "Up")

game_is_on = True

x = 1

while game_is_on:
    time.sleep(0.1)
    screen.update()
    if x % 6 == 0:
        car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.at_finish():
        player.reset()
        car_manager.speed_up()
        scoreboard.add_level()
    x += 1

screen.exitonclick()
