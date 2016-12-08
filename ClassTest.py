
class Person:
    def __init__(self):
        self.firstname = ""
        self.lastname = ""


    def FullName(self):
        print(self.firstname + self.lastname)


p = Person()

p.firstname ="Richard"
p.lastname ="Egenäs"

print(p.FullName())

print(p.firstname)
print(p.lastname)
