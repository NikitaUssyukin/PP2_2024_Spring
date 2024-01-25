class Car:
    speed = 50
    color = "Black"
    make = "Toyota"

    def __init__(self, speed, color, make) -> None:
        self.speed = speed
        self.color = color
        self.make = make

    def increaseSpeed(self, inc):
        self.speed += inc

Mustang = Car(150, "Red", "Ford")
print(Mustang.speed, Mustang.color, Mustang.make)

Mustang.increaseSpeed(20)
print(Mustang.speed)

