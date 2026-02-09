from models.book import AncientScript, RareBook, GeneralBook
from utils.constants import BookType

class BookBuilder:
    def __init__(self, book_id, title, author, book_type):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.book_type = book_type
        
        self.preservation = "Standard"
        self.digital = False
        self.restrictions = []

    def set_preservation(self, requirements: str):
        self.preservation = requirements
        return self 

    def enable_digital_access(self, allowed: bool):
        self.digital = allowed
        return self

    def add_restriction(self, restriction: str):
        self.restrictions.append(restriction)
        return self

    def build(self):
        if self.book_type == BookType.ANCIENT_SCRIPT:
            book = AncientScript(self.book_id, self.title, self.author)
        elif self.book_type == BookType.RARE_BOOK:
            book = RareBook(self.book_id, self.title, self.author)
        else:
            book = GeneralBook(self.book_id, self.title, self.author)

        book.preservation_notes = self.preservation
        book.digital_access = self.digital
        book.special_restrictions = self.restrictions
        
        return book