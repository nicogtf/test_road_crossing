import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import choice

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

### create elements (turtle....)

player = Player()
car_fleet = CarManager()
level = Scoreboard()

#setup final message
final_message = Turtle()
final_message.ht()
final_message.color('black')
alignment = 'center'
font_settings = ('Courier', 30, 'bold')


# for i in range(4):
#     car_test.add_new_car()

### binding functions
screen.onkey(player.move, 'Up')


game_is_on = True
counter = 0
add_car_after = 10
new_car_odd = [0]*10

new_car_odd.append(1)
# print(new_car_odd)

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # if counter % add_car_after == 0:
    if choice(new_car_odd) == 1:
        car_fleet.add_new_car()
    counter +=1
    add_car_after = max(add_car_after-1, 2)

    car_fleet.move_cars()
    if car_fleet.detect_collision(player):
        game_is_on = False
        final_message.write(f"Game over!\nFinal Score: {level.score}", align=alignment, font=font_settings)

    if player.ycor() >= 280:
        player.back_to_start()
        level.score_up()
        car_fleet.clear_cars()
        car_fleet.car_speed_up()
        if len(new_car_odd) > 1:
            new_car_odd.pop(0)
            print(new_car_odd)







screen.exitonclick()