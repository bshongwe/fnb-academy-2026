class Cat:
    # 1: add an extra parameter to the constructor to define the colour
    # of the cat and store it for use
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def meow(self):
        print(f"Meow my name is {self.name}")

    # 2: Define a method called Jump that takes in a value and prints
    # "The {color} cat jumps x meters high"
    # NOTE: the {color} part refers to the colour attribute you defined
    # in the constructor above.
    def Jump(self, x):
        print(f"The {self.color} cat jumps {x} meters high")


def demo():
    # Updated to include color parameter as per TODO 1
    cat1 = Cat("sussie", "orange")

    cat2 = Cat("Bob", "black")

    # 3: Create a new cat object with name JOHN and colour purple
    cat3 = Cat("JOHN", "purple")

    cat1.meow()
    cat2.meow()
    cat3.meow()

    cat1.name = "Tiffany"

    # 4: Change the colour of cat 2 to be white and observe the change
    cat2.color = "white"

    cat1.meow()
    cat2.meow()
    cat3.meow()

    # 5: Call the newly defined Jump method on each cat here
    # and observe what it prints
    cat1.Jump(1)
    cat2.Jump(2)
    cat3.Jump(3)


demo()
