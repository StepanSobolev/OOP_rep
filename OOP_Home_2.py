import time
class Auto:
    brand = None
    age = None
    color = 'Red'
    mark = None
    weight = 12

    def __init__(self, brand, mark, age):
        self.brand = brand
        self.age = age
        self.mark = mark

    def __str__(self):
        return f'Now - {self.brand} {self.mark} {self.age}'

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        self.age += 1

class Truck(Auto):
    max_load = None

    def move(self):
        print('attention move')

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):
    max_speed = None

    def move(self):
        print(f'move max speed is {self.max_speed}')



run_auto_Truck = Truck('Man', '252', 2016)
print(run_auto_Truck)