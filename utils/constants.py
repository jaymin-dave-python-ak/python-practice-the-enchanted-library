from enum import Enum

class BookType(Enum):
    ANCIENT_SCRIPT = 1
    RARE_BOOK = 2
    GENERAL_BOOK = 3
 
class BookStatus(Enum):
    AVAILABLE = 1 
    BORROWED = 2  # Unavailable
    RESTORATION_NEEDED = 3 # Unavailable

class BookAccessLevel(Enum):
    RESTRICTED = 1      # Only Librarian
    SCHOLAR_ONLY = 2    # Only Librarian and Scholar
    GENERAL = 3         # Librarian, Scholar And Guest
    
# For how many days you can lend it ? 
class BookLendingPolicy(Enum):
    RESTRICTED_ACCESS = 0  
    SHORT_TERM = 7    
    LONG_TERM = 21
    
class UserRole(Enum):
    LIBRARIAN = 1
    SCHOLAR = 2
    GUEST = 3