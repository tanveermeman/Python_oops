class animal:
    def bark(self):
        print('bark')

class pet(animal):                          # class pet is inherited from class animal
    def groom(self):
        print('groom')



a = animal()
a.bark()

p= pet()
p.groom()
p.bark()