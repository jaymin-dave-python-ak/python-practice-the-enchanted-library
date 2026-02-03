from abc import ABC, abstractmethod
from utils.constants import BookType

class Book(ABC):
    def __init__(self, book_id, title, author, book_type, access_level):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.book_type = book_type
        self.access_level = access_level
        self.status = "AVAILABLE"
    
    @abstractmethod
    def lending_policy(self):
        pass

class AncientScript(Book):
    def __init__(self, book_id, title, author):
        super().__init__(book_id, title, author, BookType.ANCIENT_SCRIPT, "RESTRICTED")

    def lending_policy(self):
        return "RESTRICTED_ACCESS"

class RareBook(Book):
    def __init__(self, book_id, title, author):
        super().__init__(book_id, title, author, BookType.RARE_BOOK, "SCHOLAR_ONLY")

    def lending_policy(self):
        return "LONG_TERM"

class GeneralBook(Book):
    def __init__(self, book_id, title, author):
        super().__init__(book_id, title, author, BookType.GENERAL_BOOK, "GENERAL")

    def lending_policy(self):
        return "SHORT_TERM"