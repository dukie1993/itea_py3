'''
Створити клас Country (Країна). Додати їй такі поля, як кількість населення, ім’я, площа. 
Додати до класу метод calc_population, Всередині якого рандомно буде або додаватися, або 
відніматися декілька тисяч населення від об’єкту. Створити об’єкт типу Country та викликати 
даний метод.
'''
import random

class Country:
    def __init__(self, population, name, area):
        print(f"Init object Country with values: {population}, {name}, {area}")
        self.population = population
        self.name = name
        self.area = area

    def calc_population(self):
        random_eval = random.random()
        if random_eval <= 0.5:
            self.population = self.population - random.randint(1000, 10000)
        elif random_eval > 0.5:
            self.population = self.population + random.randint(1000, 10000)
        
result = Country(100000, "France", 40000)
result.calc_population()
print(result.population)
