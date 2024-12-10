class SampleClass: 
    def __init__(self, a, b): #this is a constructor
        #self represent the instance of the class 
        self.c = a + b
        self.difference = a - b
# creating a object of the class
X = SampleClass(10, 20)
print(X.c)
print(X.difference)
