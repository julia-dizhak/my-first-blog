class Car(object):
    def __init__(self, wheels, seats):
        self.wheels = wheels
        self.seats = seats

    def drive(self):
        print("Uuuujikkk ujjjiiik")

    @classmethod
    def build(cls, wheels, seats):
        return cls(wheels, seats)

    def __str__(self):
        return "Car with {} wheels and {} seats".format(self.wheels, self.seats)
