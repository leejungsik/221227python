class Person:
    #초기화메서드
    def __init__(self):
        self.name = "default name"
        self.title = "New New"
    def print(self):
        print("My name is {0}".format(self.name))

p1 = Person()
p2 = Person()

p1.name = "전우치"

p1.print()
p2.print()

# Person.title = "New Title"
print(p1.title)
print(Person.title)