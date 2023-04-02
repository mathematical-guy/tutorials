

class Book:
    def __init__(self, name, author, pages):
        self.page = pages
        self.name = name
        self.author = author


class Novel(Book):
    def __str__(self):
        return self.name
        
    

book = Book(name="Core Python Programming", author="Nageshwar Rao", pages=350)

novel = Novel(name="The secrets of Mahabarata", author="Sweety", pages=3000)

print(novel)