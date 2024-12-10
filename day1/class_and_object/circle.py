class CircleArea:
    pi = 3.14
    def setRadius(self, radius):
        self.radius = radius 
        self.area = self.pi * self.radius ** 2
result = CircleArea()
radius = float(input("Enter the radius of the circle: "))
result.setRadius(radius)
print(result.area)
