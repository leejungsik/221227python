class Person:
    #초기화메서드
    def ___init__(self):
        self.name = "default name"
    def print(self):
        print("My name is {0}".formant(self.name))

p1 = Person()
p2 = Person()

p1.print()
p2.print()
