"""
First, create a class named RaceCar. In the __init__ for the class, take arguments for color and fuel_remaining. 
Be sure to set these as attributes on the instance.
Also, use setattr to take any other keyword arguments that come in.

OK, now let's add a method named run_lap. It'll take a length argument. 
It should reduce the fuel_remaining attribute by length multiplied by 0.125.
Oh, and add a laps attribute to the class, set to 0, and increment it each time the run_lap method is called.
"""


class RaceCar:

    def __init__(self, color, fuel_remaining, laps=0, **kwargs):
        self.color = color
        self.fuel_remaining = fuel_remaining
        self.laps = laps

        for key, value in kwargs.items():
            setattr(self, key, value)

    def run_lap(self, length):
        self.fuel_remaining -= length * 0.125
        self.laps += 1


red_car = RaceCar("red", 100, 0, driver="Marcus")
red_car.run_lap(10)
red_car.run_lap(11)
print(red_car.color, red_car.fuel_remaining, red_car.laps, red_car.driver)

RaceCar.laps = 10
print(RaceCar.laps, red_car.laps)




