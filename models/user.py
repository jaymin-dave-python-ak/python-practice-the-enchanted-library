from abc import ABC, abstractmethod
from enum import Enum

class UserRole(Enum):
    LIBRARIAN = 1
    SCHOLAR = 2
    GUEST = 3

class User(ABC):
    def __init__(self, user_id, name, role):
        self.__user_id = user_id
        self.__name = name
        self.__role = role

    @property
    def user_id(self):
        return self.__user_id

    @property
    def name(self):
        return self.__name

    @property
    def role(self):
        return self.__role

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
