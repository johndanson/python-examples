###############################################################################
# Python classes and objects
###############################################################################


def speed_2(x):
    print("The car's speed is", x)


class CarName:
    number_of_cars = 0

    def __init__(self,number_of_doors, color, make, vin, number_of_tires):
        self.number_of_doors = number_of_doors
        self.color = color
        self.make = make
        self.vin = vin
        self.number_of_tires = number_of_tires
        print(number_of_doors, color, make, vin, number_of_tires)


f150 = CarName(4, "Blue", "Ford F150", 21342, 4)
print("The colour of the car is", f150.color)
speed_2(60)

chevy = CarName(4, "Red", "Chevy Silverado", 645736, 4)
print("The make of the car is", chevy.make)
speed_2(65)




