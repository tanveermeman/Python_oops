class book:
    def __init__(self, name, copies):
        self.name = name
        self.copies = copies
        print('instance created')

    def increase_copies(self, how_much):
        self.copies += how_much

    def decrease_copies(self, how_much):
        self.copies -= how_much


math = book('Engineering mathematics', 10)
science = book('physics', 20)
grammar = book('tenses', 5)

# math.name = 'Engineering mathematics'
# science.name = 'physics'
# grammar.name = 'tenses'

print(math.name, math.copies)
print(science.name, science.copies)
print(grammar.name, grammar.copies)

math.increase_copies(10)
science.increase_copies(5)
grammar.increase_copies(2)

print(math.name, math.copies, ' incresed')
print(science.name, science.copies, ' incresed')
print(grammar.name, grammar.copies, ' incresed')

math.decrease_copies(5)

print(math.name, math.copies, ' decreased')


