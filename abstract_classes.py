# Prevents a user from creating ah object of that class
# compels a user to override abstract methods in a child class
# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation.

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car (Vehicle):
    def go(self):
        print("You drive the car")

    def stop(self):
        return super().stop()


class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        return super().stop()


# vehicle = Vehicle()
# vehicle.go()

car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go()
