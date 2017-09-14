class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeted_people = []
        self.number_unique_people = 0

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        self.greeting_count += 1
        if(other_person not in self.greeted_people):
            self.greeted_people.append(other_person)
            self.number_unique_people += 1

    def print_contact_info(self):
        print '%s\'s email: %s, %s\'s phone number: %s' % (self.name, self.email, self.name, self.phone)

    def add_friend(self, other_person):
        self.friends.append(other_person)

    def num_friends(self):
        return len(self.friends)

    def __repr__(self)

sonny = Person('Sonny','sonny@hotmail.com','483-485-4948')

jordan = Person('Jordan','jordan@aol.com','495-586-3456')

sonny.greet(jordan)
jordan.greet(sonny)

print sonny.email
print sonny.phone

print jordan.email
print jordan.phone


class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print '%s %s %s' % (self.year, self.make, self.model)

car = Vehicle('Nissan','Leaf',2015)



car.print_info()

sonny.print_contact_info()
#jordan.friends.append(sonny)
jordan.add_friend(sonny)
print jordan.friends[0]
print len(jordan.friends)
print len(sonny.friends)
