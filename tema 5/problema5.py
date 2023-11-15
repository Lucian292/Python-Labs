class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def display_info(self):
        print(f"{self.name} - Habitat: {self.habitat}")


class Mammal(Animal):
    def __init__(self, name, habitat, fur_color, num_legs):
        super().__init__(name, habitat)
        self.fur_color = fur_color
        self.num_legs = num_legs

    def display_info(self):
        super().display_info()
        print(f"Type: Mammal, Fur Color: {self.fur_color}, Number of Legs: {self.num_legs}")

    def give_birth(self):
        print(f"{self.name} is giving birth to live young.")

    def produce_milk(self):
        print(f"{self.name} produces milk to feed its young.")


class Bird(Animal):
    def __init__(self, name, habitat, feather_color, wingspan):
        super().__init__(name, habitat)
        self.feather_color = feather_color
        self.wingspan = wingspan

    def display_info(self):
        super().display_info()
        print(f"Type: Bird, Feather Color: {self.feather_color}, Wingspan: {self.wingspan} inches")

    def build_nest(self):
        print(f"{self.name} is building a nest for its eggs.")

    def fly(self):
        print(f"{self.name} is flying in the sky.")


class Fish(Animal):
    def __init__(self, name, habitat, scale_color, fin_type):
        super().__init__(name, habitat)
        self.scale_color = scale_color
        self.fin_type = fin_type

    def display_info(self):
        super().display_info()
        print(f"Type: Fish, Scale Color: {self.scale_color}, Fin Type: {self.fin_type}")

    def lay_eggs(self):
        print(f"{self.name} is laying eggs in the water.")

    def swim(self):
        print(f"{self.name} is swimming in the ocean.")


# Example usage:
mammal = Mammal("Lion", "Grasslands", "Yellow", 4)
mammal.display_info()
mammal.give_birth()
mammal.produce_milk()

bird = Bird("Eagle", "Mountains", "Brown", 72)
bird.display_info()
bird.build_nest()
bird.fly()

fish = Fish("Clownfish", "Reef", "Orange", "Dorsal")
fish.display_info()
fish.lay_eggs()
fish.swim()
