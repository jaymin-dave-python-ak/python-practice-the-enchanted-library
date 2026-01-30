from designPatterns.factory import UserFactory, BookFactory, UserRole, BookType

if __name__ == "__main__":
    user_factory = UserFactory()
    book_factory = BookFactory()

    user1 = user_factory.create_user("U001", "Jaymin Dave", UserRole.SCHOLAR)
    book1 = book_factory.create_book("B001", "The Art of War", "Kishan Mehta", BookType.RARE_BOOK)

    print(user1.name)
    print(book1.title)