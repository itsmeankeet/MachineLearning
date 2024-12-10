class CarInfo:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")
brand = str(input("Enter the brand of the car: "))
model = str(input("Enter the model of the car: "))
year = int(input("Enter the year of the car: "))
result = CarInfo(brand, model, year)
result.display()
