from utils.constants import BookStatus

class CentralCatalog:
    _instance = None  

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CentralCatalog, cls).__new__(cls)
            
            cls._instance.books = {}  # Dictionary: {book_id: book_object}
            cls._instance.users = {}  # Dictionary: {user_id: user_object}
            print("--- Central Catalog System Initialized Successfully ---")
            
        return cls._instance

    # --- Catalog Methods ---
    
    def add_book(self, book):
        self.books[book.book_id] = book
        print(f"Book '{book.title}' added to the vaults.")

    def get_book(self, book_id):
        return self.books.get(book_id)

    def list_available_books(self):
        available_list = []  
        for b in self.books.values():  
            if b.status == BookStatus.AVAILABLE: 
                available_list.append(b)  
        return available_list
    
    