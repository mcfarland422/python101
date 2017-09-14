class Vehicle(object):
    def __init__(self, mk, mdl, yr, mpg):
        self.make = mk
        self.model = mdl
        self.year = yr
        self.mpg = mpg
    def 

class ElectricCar(Vehicle):
    def __init__(self,make,model,year,max_range,batter_size):
        super(ElectricCar,self).__init__(make,model,year,mpg)
        self.max_range = max_range
        self.batter_size = batter_size

leaf = Vehicle('Nissan','Leaf',2015)
leaf.print_info()
bmw = Vehicle('BMW','i328',1998,23)
bmw.print_info()
