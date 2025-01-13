class Book:

    def __init__(self, title=None, writer=None, genres=None):
        self.title = title
        self.writer = writer
        self.genres = genres
        self.pages = 100

book = Book()
book.title = "Pupung Collections"
book.writer = "Tonton Young"
book.genres = ["Family", "Comedy"]
