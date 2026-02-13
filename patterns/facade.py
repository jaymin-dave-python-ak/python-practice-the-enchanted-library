from patterns.catalog_singleton import CentralCatalog

class LibraryManagementFacade:
    def __init__(self):
        self.catalog = CentralCatalog()
        print("--- Library Management Dashboard Active ---")

    def register_user(self, user_obj):
        return self.catalog.register_user(user_obj)

    def register_new_book(self, book_obj):
        return self.catalog.register_book(book_obj)

    def borrow_book(self, user_id, password, book_id):
        user = self.catalog.get_user(user_id)
        book = self.catalog.get_book(book_id)

        if not user or not book:
            return "Error: User or Book not found in the vault."
        
        if user.password != password:
            return "Access Denied: Invalid credentials."

        if not user.can_borrow(book):
            return f"Access Denied: {user.role}s cannot borrow {book.book_type}."

        try:
            book.borrow_book()
            if book.status == "BORROWED": 
                return ""    
            self.catalog.update_book_status(book)
            return f"Success: {user.name} has secured '{book.title}'."
        except Exception as e:
            return f"Action Failed: {str(e)}"

    def return_book(self, book_id):
        book = self.catalog.get_book(book_id)
        if not book:
            return "Error: Book ID not recognized."
        
        try:
            book.return_book()
            if book.status == "AVAILABLE":
                return ""
            self.catalog.update_book_status(book)
            return f"Returned: '{book.title}' is back in the vault."
        except Exception as e:
            return f"Return Failed: {str(e)}"

    def search_books(self, query):
        """Search by title or author."""
        query = query.lower()
        all_books = self.catalog.list_all_books() 
        
        if not all_books: 
            return "The library is currently empty."
        
        results = []
    
        for b in all_books:
            if query in b.title.lower() or query in b.author.lower():
                results.append(f"[{b.book_id}] {b.title} ({b.status})")
        
        if not results:
            return "No matching scrolls found."
        return "\n".join(results)
    
    def show_available_collection(self):
        books = self.catalog.list_available_books()
        if not books:
            return "The shelves are currently empty."
        
        output = []
        for b in books:
            output.append(f"[{b.book_id}] {b.title} ({b.book_type})")
        return "\n".join(output)
    
    def list_all_users(self):
        users = self.catalog.list_users()
        if not users:
            return "The library registry is empty."
        
        output = []
        for u in users:
            output.append(f"ID: {u.user_id} | Name: {u.name} | Role: {u.role}")
        return "\n".join(output)