from operator import attrgetter


class country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def __repr__(self):
        return repr((self.name, self.population, self.area))


countries = [country("india", 1200, 100),
             country("china", 1400, 200),
             country("usa", 120, 300),
             country("russia", 80, 900)]

# print(countries[2:])
countries.sort(key=attrgetter("population"))
print(countries)

