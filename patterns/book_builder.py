from models.book import Book

class BookBuilder:
    def __init__(self, book_instance):
        self.book = book_instance
        pass

    def set_preservation(self, requirements: str):
        self.book.preservation_notes = requirements
        return self 

    def enable_digital_access(self, allowed: bool):
        self.book.digital_access = allowed
        return self

    def add_restriction(self, restriction: str):
        self.book.special_restrictions.append(restriction)
        return self

    def build(self):
        return self.book
    
