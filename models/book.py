from abc import ABC
from patterns.book_state import AvailableState

class Book(ABC):
    def __init__(self, book_id, title, author, book_type, access_level):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.book_type = book_type
        self.access_level = access_level
        self.status = "AVAILABLE"
        self._state_logic = AvailableState()
        self.preservation_notes = "Standard"
        self.digital_access = False
        self.special_restrictions = []
      
    def set_state(self, state):
        self._state_logic = state

    def borrow_book(self):
        self._state_logic.borrow_book(self)

    def return_book(self):
        self._state_logic.return_book(self)

class AncientScript(Book):
    def __init__(self, book_id, title, author):
        super().__init__(book_id, title, author, "ANCIENT_SCRIPT", "RESTRICTED")

class RareBook(Book):
    def __init__(self, book_id, title, author):
        super().__init__(book_id, title, author, "RARE_BOOK", "SCHOLAR_ONLY")

class GeneralBook(Book):
    def __init__(self, book_id, title, author):
        super().__init__(book_id, title, author, "GENERAL_BOOK", "GENERAL")