# 1. Create add method to add two countries together.
# This method should create another country object with the name of the two countries combined and the population of the two countries added together.

class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def add(self, other):
        new_country = self.name + other.name
        new_population = self.population + other.population
        country = Country(new_country, new_population)
        return country

bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)

print(bosnia_herzegovina.population)
print(bosnia_herzegovina.name)


#2. Implement the previous method with a magic method

class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def __add__(self, other):
        new_country = self.name + other.name
        new_population = self.population + other.population
        country = Country(new_country, new_population)
        return country

bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)
bosnia_herzegovina = bosnia + herzegovina
print(bosnia_herzegovina.population)
print(bosnia_herzegovina.name)


# 3. Create a Car class with the following attributes: brand, model, year, and speed. 
# The Car class should have the following methods: accelerate, brake and display_speed. 
# The accelerate method should increase the speed by 5, and the brake method should decrease the speed by 5. 
# Remember that the speed cannot be negative.

class Car:
    def __init__(self, brand: str, model:str, year:int, speed:int):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed > 4:
            self.speed -= 5
        else:
            self.speed = 0

    def display_speed(self):
        print(self.speed)


ford = Car("Ford", "Mustang", 2023, 1)

print(ford)
ford.display_speed()
ford.brake()
ford.display_speed()