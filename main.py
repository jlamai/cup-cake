class Robot:
    def __init__(self, mode, wheels, size, tires,):
        self.mode = mode  # mode whether land, sea, or sir
        self.wheels = wheels  # Does it use wheels or does it fly
        self.size = size  # What is the size of the vehicle
        self.tires = tires  # Amount of tires the vehicle has

    mode = input("Enter the mode of transportation:")
    print("You chose " + mode)









