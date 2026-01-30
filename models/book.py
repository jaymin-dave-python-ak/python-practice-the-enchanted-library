from abc import ABC, abstractmethod
from enum import Enum

class BookType(Enum):
    ANCIENT_SCRIPT = 1
    RARE_BOOK = 2
    GENERAL_BOOK = 3

class Book(ABC):
    def __init__(self, book_id, title, author, book_type, access_level):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__book_type = book_type
        self.__access_level = access_level
        self.__status = "AVAILABLE"
        
    @property
    def book_id(self):
        return self.__book_id

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def book_type(self):
        return self.__book_type

    @property
    def access_level(self):
        return self.__access_level

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

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

