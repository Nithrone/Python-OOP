# Object Oriented Programming (OOP)

# class

class Person:
    # class attributes
    address = 'no information'

    #constructor
    def __init__(self, name, year):
        # object attributes
        self.name = name
        self.year = year
        
    # instance methods
    def intro(self):
        print('Hello, I am ' + self.name)


    def calculateAge(self):
        return 2023 - self.year
    
# object (instance)

p1 = Person(name = 'Piotr', year = 1990)
p2 = Person(name = 'Celil', year = 1995)

# updating
p1.name = 'Tobias'
p2.name = 'Reaper'

#accessing object attributes
print(f'p1 :name: {p1.name} year: {p1.year} address : {p1.address}')
print(f'p1 :name: {p2.name} year: {p2.year} address : {p2.address}')

p1.intro()
p2.intro()

print(f'Name: {p1.name} , Age:{p1.calculateAge()}')
print(f'Name: {p2.name} , Age:{p2.calculateAge()}')