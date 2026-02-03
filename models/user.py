from abc import ABC, abstractmethod
from utils.constants import UserRole, BookAccessLevel

class User(ABC):
    def __init__(self, user_id, password, name, role):
        self.user_id = user_id
        self.password = password
        self.name = name
        self.role = role
        
    def __str__(self):
        return f"User ID: {self.user_id}\n Name: {self.name}\n"
    
    @abstractmethod
    def can_borrow(self, book):
        pass

class Librarian(User):
    def __init__(self, user_id, password, name):
        super().__init__(user_id, password, name, 
                         UserRole.LIBRARIAN)

    def can_borrow(self, book):
        return True

class Scholar(User):
    def __init__(self, user_id, password, name):
        super().__init__(user_id, password, name, 
                         UserRole.SCHOLAR)

    def can_borrow(self, book):
        # Can borrow RareBooks and GeneralBooks, but NOT AncientScripts
        return book.access_level != BookAccessLevel.RESTRICTED

class Guest(User):
    def __init__(self, user_id, password, name):
        super().__init__(user_id, password, name, 
                         UserRole.GUEST)

    def can_borrow(self, book):
        # Can borrow ONLY GeneralBooks
        return book.access_level == BookAccessLevel.GENERAL