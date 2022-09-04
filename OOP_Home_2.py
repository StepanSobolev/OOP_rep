import time
from OOP_Home_1 import Auto

class Truck(Auto):
    max_load = None

    def __init__(self, brand, mark, age, max_load):
        super().__init__(brand, mark, age)
        self.max_load = max_load

    def move(self):
        print('attention')
        super().move()

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):
    max_speed = None

    def __init__(self, brand, mark, age, max_speed):
        super().__init__(brand, mark, age)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'Max speed is {self.max_speed}')


run_auto_Truck = Truck('Man', '252', 2016, 54)
run_auto_Truck.move()

print('-' * 30)

run_auto_Car = Car('BMV', '323', 2003, 250)
run_auto_Car.move()
