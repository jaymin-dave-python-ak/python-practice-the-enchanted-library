from models.user import *
from models.book import *

class UserFactory:
    @staticmethod
    def create_user(user_id, name, role):
        if role == UserRole.LIBRARIAN:
            return Librarian(user_id, name)
        elif role == UserRole.SCHOLAR:
            return Scholar(user_id, name)
        elif role == UserRole.GUEST:
            return Guest(user_id, name)
        else:
            raise ValueError("Invalid user role")

class BookFactory:
    @staticmethod
    def create_book(book_id, title, author, book_type):
        if book_type == BookType.ANCIENT_SCRIPT:
            return AncientScript(book_id, title, author)
        elif book_type == BookType.RARE_BOOK:
            return RareBook(book_id, title, author)
        elif book_type == BookType.GENERAL_BOOK:
            return GeneralBook(book_id, title, author)
        else:
            raise ValueError("Invalid book type")
