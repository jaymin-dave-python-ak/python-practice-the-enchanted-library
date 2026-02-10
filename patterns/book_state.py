from abc import ABC, abstractmethod

class BookState(ABC):
    @abstractmethod
    def borrow_book(self, book):
        pass

    @abstractmethod
    def return_book(self, book):
        pass

class AvailableState(BookState):
    def borrow_book(self, book):
        print(f"Success: '{book.title}' has been borrowed.")
        book.status = "BORROWED"
        book.set_state(BorrowedState()) 

    def return_book(self, book):
        print(f"'{book.title}' is already available.")

class BorrowedState(BookState):
    def borrow_book(self, book):
        print(f"Error: '{book.title}' is already borrowed.")

    def return_book(self, book):
        print(f"Success: '{book.title}' returned.")
        book.status = "AVAILABLE"
        book.set_state(AvailableState())