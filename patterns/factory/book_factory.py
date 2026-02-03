from models.book import AncientScript, RareBook, GeneralBook, BookType

class BookFactory:
    @staticmethod
    def create_book(book_id, title, author, book_type):
        if book_type == BookType.ANCIENT_SCRIPT:
            return AncientScript(book_id, title, author)
        elif book_type == BookType.RARE_BOOK:
            return RareBook(book_id, title, author)
        elif book_type == BookType.GENERAL_BOOK:
            return GeneralBook(book_id, title, author)
        else:
            raise ValueError("Invalid book type")