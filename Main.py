class man:
    # Constructor
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Welcome to a new year at Hogwarts, I am your headmaster", self.name)


# Creating the object of the class "man"
headmaster = man("Albus Dumbledore")
headmaster.introduce()

# Adding some extra text for fun
print("I hope you all will find this year quite special!")