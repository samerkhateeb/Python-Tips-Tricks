# method chaining = calling multiple methods sequentially
# each call performs an action on the same object and returns self

class Car:

    def turn_on(self):
        print('Turn Onnnnn')
        return self

    def brake(self):
        print('brake ... stoopp')
        return self

    def turn_off(self):
        print('turn off')
        return self

    def drive(self):
        print('start driving')
        return self


car = Car()

car.turn_off()\
    .brake()\
    .turn_on()\
    .drive()
