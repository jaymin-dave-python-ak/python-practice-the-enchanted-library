from abc import ABC, abstractmethod
from utils.constants import UserRole

class User(ABC):
    def __init__(self, user_id, name, role):
        self.user_id = user_id
        self.name = name
        self.role = role

    @abstractmethod
    def can_borrow(self, book):
        pass

class Librarian(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, UserRole.LIBRARIAN)

    def can_borrow(self, book):
        return True

class Scholar(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, UserRole.SCHOLAR)

    def can_borrow(self, book):
        # Can borrow RareBooks and GeneralBooks, but NOT AncientScripts
        return book.access_level != "RESTRICTED"

class Guest(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, UserRole.GUEST)

    def can_borrow(self, book):
        # Can borrow ONLY GeneralBooks
        return book.access_level == "GENERAL"