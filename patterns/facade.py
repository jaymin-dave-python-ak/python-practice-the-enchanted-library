from patterns.catalog_singleton import CentralCatalog

class LibraryManagementFacade:
    def __init__(self):
        self.catalog = CentralCatalog()
        print("--- Library Management Dashboard Active ---")

    def borrow_book(self, user_id, password, book_id):
        """Authenticated borrowing process."""
        user = self.catalog.get_user(user_id)
        book = self.catalog.get_book(book_id)

        if not user or not book:
            return "Error: User or Book not found in the vault."
        
        if user.password != password:
            return "Access Denied: Invalid credentials."

        # Check permissions based on User Role vs Book Access Level
        if not user.can_borrow(book):
            return f"Access Denied: {user.role.name}s cannot borrow {book.book_type.name}."

        # Delegate availability logic to the State Pattern within the Book
        try:
            book.borrow_book() 
            return f"Success: {user.name} has secured '{book.title}'."
        except Exception as e:
            return f"Action Failed: {str(e)}"

    def return_book(self, book_id):
        """Returns a book to the library and updates its state."""
        book = self.catalog.get_book(book_id)
        if not book:
            return "Error: Book ID not recognized."
        
        try:
            book.return_book()
            return f"Returned: '{book.title}' is back in the vault."
        
        except Exception as e:
            return f"Return Failed: {str(e)}"

    def register_user(self, user_obj):
        """Registers a new user into the system via the Catalog."""
        if not user_obj.user_id:
            return "Error: Invalid User Data."
        try:
            self.catalog.add_user(user_obj)
            return f"Identity Verified: {user_obj.name} ({user_obj.role.name}) registered."
        except ValueError as e:
            return f"Registration Failed: {str(e)}"

    def find_user(self, user_id):
        user = self.catalog.get_user(user_id)
        return user if user else f"Error: User {user_id} not found."

    def list_all_users(self):
        users = self.catalog.list_users()
        if not users:
            return "The library registry is empty."
        
        return "\n".join([f"ID: {u.user_id} | Name: {u.name} | Role: {u.role.name}" 
                         for u in users.values()])

    def register_new_book(self, book_obj):
        """Adds a new physical or digital book to the catalog."""
        try:
            self.catalog.add_book(book_obj)
            return f"Archived: '{book_obj.title}' is now tracked."
        except ValueError as e:
            return f"Archive Error: {str(e)}"

    def search_books(self, query):
        """Search by title or author (case-insensitive)."""
        query = query.lower()
        results = [b for b in self.catalog.books.values() 
                   if query in b.title.lower() or query in b.author.lower()]
        
        if not results:
            return "No matching scrolls found."
        
        return "\n".join([f"[{b.book_id}] {b.title} ({b.status.name})" for b in results])

    def show_available_collection(self):
        """Returns a list of books currently on the shelves."""
        books = self.catalog.list_available_books()
        if not books:
            return "The shelves are currently empty."
        return "\n".join([f"[{b.book_id}] {b.title} ({b.book_type.name})" for b in books])

    def remove_book(self, book_id):
        """Removes a book permanently from the catalog."""
        if book_id in self.catalog.books:
            del self.catalog.books[book_id]
            return f"Success: Book {book_id} removed from the vault."
        return "Error: Book ID not found."