from abc import ABC, abstractmethod
from utils.constants import BookStatus

class BookState(ABC):
    @abstractmethod
    def borrow_book(self, book):
        pass

    @abstractmethod
    def return_book(self, book):
        pass

    @abstractmethod
    def request_restoration(self, book):
        pass

class AvailableState(BookState):
    def borrow_book(self, book):
        print(f"Success: '{book.title}' has been borrowed.")
        book.status = BookStatus.BORROWED
        book.set_state(BorrowedState()) 

    def return_book(self, book):
        print(f"'{book.title}' is already available.")

    def request_restoration(self, book):
        print(f"'{book.title}' sent to restoration.")
        book.status = BookStatus.RESTORATION_NEEDED
        book.set_state(RestorationNeededState())

class BorrowedState(BookState):
    def borrow_book(self, book):
        print(f"Error: '{book.title}' is already borrowed.")

    def return_book(self, book):
        print(f"Success: '{book.title}' returned.")
        book.status = BookStatus.AVAILABLE
        book.set_state(AvailableState())

    def request_restoration(self, book):
        print(f"Error: '{book.title}' is currently borrowed. do it later.")

class RestorationNeededState(BookState):
    def borrow_book(self, book):
        print(f"Forbidden: '{book.title}' is under restoration.")

    def return_book(self, book):
        print(f"Invalid: '{book.title}' was never borrowed, it is being repaired.")

    def request_restoration(self, book):
        print(f"'{book.title}' is already in restoration.")