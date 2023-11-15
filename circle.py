class Circle:
    pi = 3.14

    def __init__(self, halfDiameter=1):
        self.halfDiameter = halfDiameter
        
        

    #Methods
    def calc_circum(self):
        return 2 * self.pi * ((self.halfDiameter))

    def calc_area(self):
        return self.pi * ((self.halfDiameter)**2)
    
c1 = Circle()
c2 = Circle(3)

print(f'c1 --> Area :{c1.calc_area()}, Circumference:{c1.calc_circum()}')
print(f'c2 --> Area :{c2.calc_area()}, Circumference:{c2.calc_circum()}')