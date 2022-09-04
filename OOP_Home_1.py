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


# run_auto_1 = Auto('Mazda', '323f', 2002)
# print(run_auto_1)
# run_auto_2 = Auto('Mazda', '626', 2012)
# print(run_auto_2)
# run_auto_3 = Auto('Mazda', '3', 2008)
# print(run_auto_3)