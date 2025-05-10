# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects


class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price

        self.author = author

        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append(chapter)

    def showchapters(self):
        return "Chapters:\n" + "\n".join(
            [f"{ch.name} {ch.pages}" for ch in self.chapters]
        )

    def get_book_page_count(self):
        page_count = 0
        for ch in self.chapters:
            page_count += ch.pages
        return f"Book page count: {page_count}"


class Author:
    def __init__(self, authorfname, authorlname):
        self.authorfname = authorfname
        self.authorlname = authorlname

    def __str__(self):
        return f"{self.authorfname} {self.authorlname}"


class Chapter:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages


auth = Author("Leo", "Tolstoy")
b1 = Book("War and Peace", 39.0, auth)

b1.addchapter(Chapter("Chapter 1", 125))
b1.addchapter(Chapter("Chapter 2", 97))
b1.addchapter(Chapter("Chapter 3", 143))


print(b1.title)
print(b1.author)
print(b1.showchapters())
print(b1.get_book_page_count())
