"""Class practice 2"""
class PartyAnimal:
    """Party class"""
    x = 0
    name = ''
    def __init__(self, z):
        self.name = z
        print(self.name,"constructed")

    def party(self):
        """Adding one to the party"""
        self.x += 1
        print(self.name,"party count",self.x)

    def hi(self):
        """Greeting"""
        print(f'Hi, my name is {self.name}')

s = PartyAnimal('Sally')
s.party()
s.hi()
print(s.name)
j = PartyAnimal('Jim')
j.party()
j.party()
