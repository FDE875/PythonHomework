
class BookNotFoundException(Exception):
    pass


class BookAlreadyBorrowedException(Exception):
    pass


class MemberLimitExceededException(Exception):
    pass


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} - {status}"


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(
                f"{self.name} cannot borrow more than 3 books!"
            )

        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book.title}")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member added: {member.name}")

    def borrow_book(self, member, title):

        book = None

        for b in self.books:
            if b.title.lower() == title.lower():
                book = b
                break

        if book is None:
            raise BookNotFoundException(
                f"Book '{title}' not found!"
            )

        if book.is_borrowed:
            raise BookAlreadyBorrowedException(
                f"'{title}' is already borrowed!"
            )

    
        member.borrow_book(book)

        book.is_borrowed = True

        print(f"{member.name} borrowed '{title}'")

    def return_book(self, member, title):

        for book in self.books:
            if book.title.lower() == title.lower():

                if book not in member.borrowed_books:
                    print("This member has not borrowed this book.")
                    return

                member.return_book(book)
                book.is_borrowed = False

                print(f"{member.name} returned '{title}'")
                return

        raise BookNotFoundException(
            f"Book '{title}' not found!"
        )

    def show_books(self):
        print("\n--- Library Books ---")
        for book in self.books:
            print(book)

    def show_members(self):
        print("\n--- Library Members ---")
        for member in self.members:
            print(f"\n{member.name}:")
            for book in member.borrowed_books:
                print(f"  - {book.title}")

library = Library()

book1 = Book("Python Basics", "John Smith")
book2 = Book("Data Science", "Mark Lee")
book3 = Book("Economics", "David Brown")
book4 = Book("Financial Modeling", "James Wilson")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
member1 = Member("Ali")
member2 = Member("Vali")
library.add_member(member1)
library.add_member(member2)

try:
    library.borrow_book(member1, "Python Basics")
    library.borrow_book(member1, "Data Science")
    library.borrow_book(member1, "Economics")
    library.borrow_book(member1, "Financial Modeling")

except MemberLimitExceededException as e:
    print("Error:", e)

try:
    library.borrow_book(member2, "Python Basics")

except BookAlreadyBorrowedException as e:
    print("Error:", e)

try:
    library.borrow_book(member2, "Java Programming")

except BookNotFoundException as e:
    print("Error:", e)

library.return_book(member1, "Python Basics")
library.borrow_book(member2, "Python Basics")
library.show_books()
library.show_members()
