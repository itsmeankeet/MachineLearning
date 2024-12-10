class CircumstanceOfCircle:
    pi = 3.14
    def setRadius(self, rad):
        self.radius = rad
        self.circumstance = 2 * self.pi * self.radius
result = CircumstanceOfCircle()
radius = float(input("Enter the radius of the circle: "))
result.setRadius(radius)
print("The circumstance of the circle is: ", result.circumstance)
