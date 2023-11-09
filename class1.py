"""Class practice"""
class PartyAnimal:
    """Class representing a party monster"""
    def __init__(self):
        print('I am constructed')
    x = 0
    def party(self):
        """Adds one member to the party"""
        self.x = self.x + 1
        print(f'So far {self.x}')
    def __del__(self):
        print('I am destructed', self.x)

an = PartyAnimal()
print(type(an))
print(dir(an))

an.party()
an.party()
an = 42
print('an contains', an)
