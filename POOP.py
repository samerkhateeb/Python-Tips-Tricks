# Class name should be Capital

class Car:

    def __init__(self, model, name, year):
        self.model = model
        self.name = name
        self.year = year

    def drive(self):
        print('Car {} is driving'.format(self.name))

    def stop(self):
        print('car {} is stopped'.format(self.name))


car1 = Car("SUV", "Mercedes", 2011)
car1.drive()
car1.stop()


car2 = Car("SUV", "Opel", 2018)
car2.drive()
car2.stop()
