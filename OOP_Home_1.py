class Auto:
    brand = 'Porsche'
    age = 1983
    cоlor = 'Red'
    mark = 'Panamera'
    weight = 12

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        self.age += 1

run_auto = Auto