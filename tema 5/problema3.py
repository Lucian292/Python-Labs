import random


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Type: Car, Doors: {self.num_doors}")

    def calculate_mileage(self):
        base_mileage = 30  # miles per gallon

        efficiency_factor = random.uniform(0.9, 1.1)
        weather_factor = random.uniform(0.8, 1.2)

        calculated_mileage = base_mileage * efficiency_factor * weather_factor

        return round(calculated_mileage, 2)


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels

    def display_info(self):
        super().display_info()
        print(f"Type: Motorcycle, Wheels: {self.num_wheels}")

    def calculate_mileage(self):
        base_mileage = 50  # miles per gallon

        # Simulating factors affecting mileage
        efficiency_factor = random.uniform(0.9, 1.1)
        weather_factor = random.uniform(0.8, 1.2)

        calculated_mileage = base_mileage * efficiency_factor * weather_factor

        return round(calculated_mileage, 2)


class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def display_info(self):
        super().display_info()
        print(f"Type: Truck, Towing Capacity: {self.towing_capacity} lbs")

    def calculate_towing_capacity(self):
        return self.towing_capacity


car = Car("Toyota", "Camry", 2023, 4)
car.display_info()
print("Mileage:", car.calculate_mileage())

motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2020, 2)
motorcycle.display_info()
print("Mileage:", motorcycle.calculate_mileage())

truck = Truck("Ford", "F-150", 1995, 10000)
truck.display_info()
print("Towing Capacity:", truck.calculate_towing_capacity())
