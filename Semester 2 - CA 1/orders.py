# Exercises 2.1 and 2.2 - Pizza orders

class Pizza:
    def __init__(self, toppings, size="Medium"):
        self.toppings = toppings
        self.__size = size
