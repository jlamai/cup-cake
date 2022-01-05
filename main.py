class Robot:
    def __init__(self, mode, wheels, size, tires, ):
        self.mode = mode  # mode whether land, sea, or sir
        self.wheels = wheels  # Does it use wheels or does it fly
        self.size = size  # What is the size of the vehicle
        self.tires = tires  # Amount of tires the vehicle has

    def vehicle_type(self):
        print("You chose a " + self.mode, " mode of transportation, " + self.wheels, " It uses wheels for movement")

    # mode1 = input("Enter the mode of transportation:")
    # wheels1 = input("Does your transportation have wheels?:")
    # size1 = input("Is your transport Small Large or Extra Large?:")
    # tires1 = input("How many tires does your transportation have?:")
    # print("You chose " + mode1)


v1 = Robot("Land", "Yes", "Large", 4)
v2 = Robot(input("Enter the mode of transportation:"),
           input("Does your transportation have wheels?:"),
           input("Is your transport Small Large or Extra Large?:"),
           input("How many tires does your transportation have?:")
           )

v1.vehicle_type()
v2.vehicle_type()