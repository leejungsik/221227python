class Person:
    #초기화메서드
    def __init__(self):
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

p1 = Person()
p2 = Person()

p1.print()
p2.print()
