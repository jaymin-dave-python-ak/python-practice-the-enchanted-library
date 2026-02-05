from patterns.factory.user_factory import UserFactory
from patterns.factory.book_factory import BookFactory
from patterns.book_builder import BookBuilder
from utils.constants import UserRole, BookType

if __name__ == "__main__":
    user_factory = UserFactory()
    book_factory = BookFactory()

    user1 = user_factory.create_user("U001", "password", "Jaymin Dave" ,UserRole.SCHOLAR)
    book1 = book_factory.create_book("B001", "The Art of War", "Kishan Mehta", BookType.ANCIENT_SCRIPT)

    # Use Builder to add complex metadata
    builder = BookBuilder(book1)
    custom_book = (builder.set_preservation("Keep in vacuum-sealed glass").enable_digital_access(False).add_restriction("Librarian oversight required").build())
    print(user1)
    print(book1)