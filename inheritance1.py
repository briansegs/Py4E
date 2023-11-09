"""Class inheritance practice"""
class PartyAnimal:
    """party time"""
    x = 0
    name = ""
    def __init__(self, nam):
        self.name = nam
        print(self.name,"constructed")

    def party(self):
        """add one"""
        self.x = self.x + 1
        print(self.name,"party count",self.x)

class FootballFan(PartyAnimal):
    """a fan of foots and balls"""
    points = 0
    def touchdown(self):
        """now you can kick it"""
        self.points = self.points + 7
        self.party()
        print(self.name,"points",self.points)

s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()
