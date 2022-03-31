from turtle import Turtle
from random import choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 5
Y_START = list(range(-280,280,20))
X_START = list(range(300,400))


class CarManager:

    def __init__(self):
        self.cars = []
        self.add_new_car()
        self.step = STARTING_MOVE_DISTANCE








    def create_random_car(self):
        random_car = Turtle()
        random_car.shape('square')
        random_car.penup()
        random_car.shapesize(stretch_wid=1, stretch_len=2)
        random_car.color(choice(COLORS))
        random_car.goto(choice(X_START), choice(Y_START))
        random_car.setheading(180)
        return random_car



    def add_new_car(self):
        self.cars.append(self.create_random_car())

    def move_cars(self):
        for car in self.cars:
            car.forward(self.step)

    def car_speed_up(self):
        self.step = self.step + MOVE_INCREMENT

    def detect_collision(self, turtle):
        collision = False
        y_turtle = turtle.ycor()
        for car in self.cars:
            if abs(car.ycor() - y_turtle) <= 20:
                if car.xcor() > - (self.step+10) and car.xcor() < -10:
                    # car.goto(0, car.ycor())
                    collision = True
                    # print(car.xcor(), car.ycor() - y_turtle, collision, car.ycor(), y_turtle)
                    return collision
        return collision

    def clear_cars(self):
        for car in self.cars:
            car.goto(-400, 0)
