from enum import Enum

class BookType(Enum):
    ANCIENT_SCRIPT = 1
    RARE_BOOK = 2
    GENERAL_BOOK = 3
 
class BookStatus(Enum):
    AVAILABLE = 1 
    BORROWED = 0

class BookAccessLevel(Enum):
    RESTRICTED = 1      # Only Librarian
    SCHOLAR_ONLY = 2    # Only Librarian and Scholar
    GENERAL = 3         # Librarian, Scholar And Guest
    
class UserRole(Enum):
    LIBRARIAN = 1
    SCHOLAR = 2
    GUEST = 3