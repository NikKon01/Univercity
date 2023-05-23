class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def zapusk(self):
        print("Автомобиль заведен")

    def otkl(self):
        print("Автомобиль заглушен")

    def setColor(self, color):
        self.color = color

    def setType(self, type):
        self.type = type

    def setYear(self, year):
        self.year = year

    def printInfo(self):
        print(f'color: {self.color} type: {self.type} year: {self.year}')

car = Car("white", "bmv", 2016)
car.printInfo()
car.zapusk()
car.otkl()
car.setColor("blue")
car.setType("ford")
car.setYear(2001)
car.printInfo()