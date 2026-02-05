from catalog_singleton import CentralCatalog
from utils.constants import BookStatus

class LibraryManagementFacade:
    def __init__(self):
        self.catalog = CentralCatalog()
        print("--- Library Management Dashboard Active ---")

    # --- Unified Interface for Guests, Scholar & Librarians ---

    def borrow_book(self, user, book_id):
        """Coordinates security, availability, and state transition."""
        book = self.catalog.get_book(book_id)
        
        if not book:
            return "Error: This tome does not exist in our records."

        # 1. Security Check (Role-Based Access Control)
        if not user.can_borrow(book):
            return f"Access Denied: {user.role.name}s cannot access {book.book_type.name}."

        # 2. Availability Check
        if book.status != BookStatus.AVAILABLE:
            return f"Unavailable: '{book.title}' is currently {book.status.name}."

        # 3. State Transition (Triggers your State Pattern logic)
        try:
            book.borrow_book()
            return f"Success: {user.name} has borrowed '{book.title}'."
        except Exception as e:
            return f"Failed: {str(e)}"

    def return_book(self, book_id):
        """Simplifies the return process."""
        book = self.catalog.get_book(book_id)
        if book:
            book.return_book() # Triggers State Pattern
            return f"Returned: '{book.title}' is back in the vault."
        return "Error: Book ID not recognized."

    # --- Administrative Interface (Librarian Specific) ---

    def register_new_book(self, book_obj):
        """Facade simplifies adding to catalog."""
        self.catalog.add_book(book_obj)
        return f"Archived: {book_obj.title} is now tracked."

    def show_available_collection(self):
        """Provides a simplified view for the user."""
        books = self.catalog.list_available_books()
        if not books:
            return "The shelves are currently empty."
        return "\n".join([f"[{b.book_id}] {b.title} ({b.book_type.name})" for b in books])
