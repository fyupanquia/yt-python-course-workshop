class Book:
    def __init__(self, title, publisher, pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages


class Ebook(Book):
    def __init__(self, title, publisher, pages, format_):
        # super().__init__(title, publisher, pages)
        super(Ebook, self).__init__(title, publisher, pages)
        # Book.__init__(self, title, publisher, pages)
        self.format__ = format_
ebook = Ebook('Learning Python programming', 'Packt Publishing', 500, 'PDF')
print(ebook.title)
print(ebook.publisher)
print(ebook.pages)
print(ebook.format__)