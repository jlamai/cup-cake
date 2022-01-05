class Robot: # How multiple classes and objects interact with each other.
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name, ". My color is" + self.color, ". I weigh", self.weight, "kg.")


r1 = Robot("Tom", "Red", 30)
r2 = Robot("Jerry", "Blue", 40)


class Person:
    def __init__(self, n, p, i, r):
        self.name = n
        self.personality = p
        self.is_sitting = i
        self.robotOwned = r

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False


p1 = Person("Alice", "Friendly", False, r2)
p2 = Person("Jumoke", "Nice", True, r1)

p1.robotOwned.introduce_self()
p2.robotOwned.introduce_self()

