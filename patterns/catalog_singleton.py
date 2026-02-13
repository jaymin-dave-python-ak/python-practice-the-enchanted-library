import os
from dotenv import load_dotenv
from pymongo import MongoClient
from models.book import AncientScript, RareBook, GeneralBook
from models.user import Librarian, Scholar, Guest
from patterns.book_state import AvailableState, BorrowedState

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')

class CentralCatalog:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CentralCatalog, cls).__new__(cls)
            cls._instance.client = MongoClient(MONGO_URI)
            cls._instance.db = cls._instance.client['library_db']
            cls._instance.books_col = cls._instance.db['books']
            cls._instance.users_col = cls._instance.db['users']
            print("--- Central Catalog Linked to MongoDB ---")
        return cls._instance

    def register_user(self, user):
        if self.users_col.count_documents({"user_id": user.user_id}) > 0:
            raise ValueError(f"ID Collision: User ID {user.user_id} already exists.")
        
        user_dict = user.__dict__.copy()
        self.users_col.insert_one(user_dict)
    
    def register_book(self, book):
        if self.books_col.count_documents({"book_id": book.book_id}) > 0:
            raise ValueError(f"ID Collision: Book ID {book.book_id} already exists.")
        book_dict = book.__dict__.copy()
        if "_state_logic" in book_dict:
            del book_dict["_state_logic"]
        self.books_col.insert_one(book_dict)
    
    def update_book_status(self, book):
        self.books_col.update_one(
            {"book_id": book.book_id},
            {"$set": {"status": book.status}}
        )
    
    def _create_book_object(self, data):
        if data is None:
            return None

        b_type = data.get("book_type")
        if b_type == "ANCIENT_SCRIPT":
            obj = AncientScript(data['book_id'], data['title'], data['author'])
        elif b_type == "RARE_BOOK":
            obj = RareBook(data['book_id'], data['title'], data['author'])
        else:
            obj = GeneralBook(data['book_id'], data['title'], data['author'])
        
        obj.status = data.get("status", "AVAILABLE")
        obj.preservation_notes = data.get("preservation_notes", "Standard")
        obj.special_restrictions = data.get("special_restrictions", [])
        
        if obj.status == "BORROWED":
            obj.set_state(BorrowedState())
        else:
            obj.set_state(AvailableState())

        return obj

    def get_book(self, book_id):
        data = self.books_col.find_one({"book_id": book_id})
        return self._create_book_object(data)
    
    def _create_user_object(self, data):
        if data is None:
            return None
            
        role = data.get("role")
        if role == "LIBRARIAN":
            return Librarian(data['user_id'], data['password'], data['name'])
        elif role == "SCHOLAR":
            return Scholar(data['user_id'], data['password'], data['name'])
        else:
            return Guest(data['user_id'], data['password'], data['name'])

    def list_all_books(self):
        cursor = self.books_col.find()
        results = []
        for doc in cursor:
            book_obj = self._create_book_object(doc)
            results.append(book_obj)
        return results

    def list_available_books(self):
        cursor = self.books_col.find({"status": "AVAILABLE"})
        results = []
        for doc in cursor:
            book_obj = self._create_book_object(doc)
            results.append(book_obj)
        return results

    def get_user(self, user_id):
        data = self.users_col.find_one({"user_id": user_id})
        return self._create_user_object(data)

    def list_users(self):
        cursor = self.users_col.find()
        results = []
        for doc in cursor:
            user_obj = self._create_user_object(doc)
            results.append(user_obj)
        return results