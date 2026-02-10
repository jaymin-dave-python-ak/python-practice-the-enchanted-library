from pymongo import MongoClient

class CentralCatalog:
    _instance = None  
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CentralCatalog, cls).__new__(cls)
            cls._instance.client = MongoClient("mongodb+srv://jaymin:jaymin@jaymin-dave-ak-cluster.x4jz7ed.mongodb.net/?appName=Jaymin-Dave-AK-Cluster")
            cls._instance.db = cls._instance.client['library_db']
            
            cls._instance.books_col = cls._instance.db['books']
            cls._instance.users_col = cls._instance.db['users']
            
            print("--- Central Catalog Linked to MongoDB ---")
        return cls._instance

    def add_book(self, book):
        if book.book_id in self.books:
            raise ValueError(f"ID Collision: Book ID {book.book_id} already exists.")
        self.books[book.book_id] = book

    def add_user(self, user):
        if user.user_id in self.users:
            raise ValueError(f"ID Collision: User ID {user.user_id} already exists.")
        self.users[user.user_id] = user
        
    def get_book(self, book_id):
        return self.books.get(book_id)

    def get_user(self, user_id):
        return self.users.get(user_id)

    def list_available_books(self):
        available_list = []  
        for b in self.books.values():  
            if b.status == "AVAILABLE": 
                available_list.append(b)  
        return available_list

    def list_users(self):
        return self.users.copy()