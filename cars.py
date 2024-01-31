import random

def getModelYeal(years):
    return random.choice(years)

print("Hello World!")

cars = ["Toyota", "BMW", "Ford", "Cadillac", "Audi", "Tesla", "Porsche"]
modelYear = ["2010", "2012", "2014"]

print(cars[random.randint(0, len(cars)-1)])
print(getModelYeal(modelYear))