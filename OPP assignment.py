class Vehicle:
    def move(self):
        print("vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("driving")

class Plane(Vehicle):
    def move(self):
        print("flying")

class Bike(Vehicle):
    def move(self):
        print("pedaling")

c = Car()
p = Plane()
b = Bike()

c.move()
p.move()
b.move()