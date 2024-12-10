class AreaAndPerimeterOfRectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculateArea(self):
        return self.length * self.width
    def calculatePerimeter(self):
        return 2 * (self.length + self.width)
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
result = AreaAndPerimeterOfRectangle(length, width)
print("The area of the rectangle is: ", result.calculateArea())
print("The perimeter of the rectangle is: ", result.calculatePerimeter())
