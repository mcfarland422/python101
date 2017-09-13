# a class to make Atl United players
class Player(object):
    EVERY class needs to start with def_init_
    # this function gets run ONCE and only ONCE, when the object is made def_init_(self):
    # you pass in args, when you make the object
    # self is ALWAYS the first
    # everything else is optional
    def_init_(self, name, position):
        self.name = name
        self.position = position
        self.team = "Atlanta United"

player1 = Player('Miguel Almiron', 'midfield')
print player1
