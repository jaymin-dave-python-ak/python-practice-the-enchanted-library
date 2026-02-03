from abc import ABC, abstractmethod
from utils.constants import BookType, BookStatus, BookAccessLevel, BookLendingPolicy

class Book(ABC):
    def __init__(self, book_id, title, author, book_type, access_level):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.book_type = book_type
        self.access_level = access_level
        self.status = BookStatus.AVAILABLE
        # Metadata fields for Builder to populate
        self.preservation_notes = "Standard"
        self.digital_access = False
        self.special_restrictions = []
    
    def __str__(self):
        return f"Book ID: {self.book_id}\n Book Title: {self.title}\n Book Author: {self.author}"
    
    @abstractmethod
    def lending_policy(self):
        pass

class AncientScript(Book):
    def __init__(self, book_id, title, author):
        super().__init__(book_id, title, author, 
                         BookType.ANCIENT_SCRIPT, 
                         BookAccessLevel.RESTRICTED)

    def lending_policy(self):
        return BookLendingPolicy.RESTRICTED_ACCESS

class RareBook(Book):
    def __init__(self, book_id, title, author):
        super().__init__(book_id, title, author, 
                         BookType.RARE_BOOK, 
                         BookAccessLevel.SCHOLAR_ONLY)

    def lending_policy(self):
        return BookLendingPolicy.SHORT_TERM

class GeneralBook(Book):
    def __init__(self, book_id, title, author):
        super().__init__(book_id, title, author, 
                         BookType.GENERAL_BOOK, 
                         BookAccessLevel.GENERAL)

    def lending_policy(self):
        return BookLendingPolicy.LONG_TERM