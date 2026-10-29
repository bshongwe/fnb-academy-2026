class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def makeSound(self):
        print(f"My name is {self.name} and I am {self.age} years old")


class Snake(Animal):

    def __init__(self, name, age, length):
        super().__init__(name, age)
        self.length = length

    def makeSound(self):
        print(f"I am a snake and i go SSSSSSS ")


class Lion(Animal):

    def __init__(self, name, age, fColor):
        super().__init__(name, age)
        self.furrcolor = fColor

    def makeSound(self):
        print("I am a lion and i go ROAR")

    def run(self, runSpeed):
        print(f"I am {self.name} and i am running at a speed of {runSpeed} km/h")


class Elephant(Animal):

    # TODO 1: Call the parent class's __init__ using super(),
    # passing name and age, then set self.trunkLength

    def __init__(self, name, age, trunkLength):
        super().__init__(name, age)
        self.trunkLength = trunkLength

    # TODO 2: Override makeSound() so it:
    #   - calls the base class's makeSound() using super()
    #   - then prints "GORRRRRRR"

    def makeSound(self):
        super().makeSound()
        print("GORRRRRRR")

class ZOO:

    def __init__(self, name, animals):
        self.name = name
        self.animals = animals

    # TODO 3: complete this method so animals can be added after the Zoo is created

    def addAnimal(self, new_animal):
        self.animals.append(new_animal)

    # TODO 4: complete this method so animals can be removed after creation

    def removeAnimal(self, animal_to_remove):
        if animal_to_remove in self.animals:
            self.animals.remove(animal_to_remove)

def demo():
    L1 = Lion("Bob", 20, "yellow")
    S1 = Snake("Steve", 15, 900)

    listAnimal = [L1, S1]

    Z1 = ZOO("Johannesburg Zoo", listAnimal)

    for A in Z1.animals:
        A.makeSound()

    print("--------END OF TEST 1--------")

    # TODO 5: Create an instance of Elephant and add it to the zoo
    # using the addAnimal() method provided

    E1 = Elephant("Dumbo", 5, 150)
    Z1.addAnimal(E1)

    # If correctly defined, this second loop should now also print
    # the elephant's info and its sound
    for A in Z1.animals:
        A.makeSound()

    print("--------END OF TEST 2--------")

    # If removeAnimal is correctly defined the loop below should print
    # for every animal except the lion

    Z1.removeAnimal(L1)

    for A in Z1.animals:
        A.makeSound()

    print("--------END OF TEST 3--------")

    return Z1

# =====================================================================
#  DO NOT MODIFY ANYTHING BELOW THIS LINE
#  Press Enter when you click Run to see your program's output.
# =====================================================================
import io
import contextlib

def _quiet(fn, *args):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        value = fn(*args)
    return buf.getvalue(), value

def _main():
    try:
        test = input().strip()
    except EOFError:
        test = ""

    if test in ("", "demo"):
        demo()
        return

    try:
        if test == "1":
            e = Elephant("Dumbo", 5, 150)
            print(e.name, e.age, e.trunkLength)

        elif test == "2":
            e = Elephant("Dumbo", 5, 150)
            out, _ = _quiet(e.makeSound)
            lines = [l.strip() for l in out.splitlines() if l.strip()]
            print(len(lines), lines[-1] if lines else "")

        elif test == "3":
            z = ZOO("Test", [])
            z.addAnimal(Lion("Leo", 4, "gold"))
            z.addAnimal(Snake("Sid", 2, 100))
            print(len(z.animals))

        elif test == "4":
            lion = Lion("Leo", 4, "gold")
            z = ZOO("Test", [lion, Snake("Sid", 2, 100)])
            z.removeAnimal(lion)
            print(len(z.animals), lion in z.animals)

        elif test == "5":
            _, zoo = _quiet(demo)
            print(any(isinstance(a, Elephant) for a in zoo.animals),
                  any(isinstance(a, Lion) for a in zoo.animals))

        else:
            print("unknown test")

    except Exception as error:
        print("ERROR:", type(error).__name__)

if __name__ == "__main__":
    _main()