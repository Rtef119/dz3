class Animal:
    def __init__(self, name = "Animal"):
        self.name = name

class Aut:
    def __init__(self, navn):
        self.navn = navn
        self.Animals = []

    def add_passengers(self, *args):
        for Animals in args:
            self.Animals.append(Animals)


    def print_passengers_names(self):
        if self.Animals != []:
            print(f"Імена тварин в притулку №{self.navn}")
            for Animals in self.Animals:
                print(Animals.name)
        else:
            print(f"В притулку {self.navn} тварини відсутні")

Ptr = Aut("4367")
for i in range(4):
    p1 = Animal(input("Ведіть ім'я тварини:"))
    Ptr.add_passengers(p1)

Ptr.print_passengers_names()