def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 5, 6))


def calculate(**kwargs):
    print(kwargs)


calculate(add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)