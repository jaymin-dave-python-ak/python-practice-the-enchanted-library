from enum import Enum

class BookType(Enum):
    ANCIENT_SCRIPT = 1
    RARE_BOOK = 2
    GENERAL_BOOK = 3
    
class UserRole(Enum):
    LIBRARIAN = 1
    SCHOLAR = 2
    GUEST = 3