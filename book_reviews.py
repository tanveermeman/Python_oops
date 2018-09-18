class book:
    def __init__(self, id, name, author):
        self.id = id
        self.name = name
        self.author = author
        self.reviews = []

    def __repr__(self):
        return repr((self.id, self.name, self.author, self.reviews))

    def add_review(self, review):
        self.reviews.append(review)


class review:
    def __init__(self, id, description, rating):
        self.id =id
        self.description = description
        self.rating = rating

    def __repr__(self):
        return repr((self.id, self.description, self.rating))




book = book(123, 'Object Oriented Programming with Python', 'Tanveer')

book.add_review(review(10, 'great book', 5))
book.add_review(review(5,'awesome', 4))
print(book)

print(review(10, 'great book', 5))
