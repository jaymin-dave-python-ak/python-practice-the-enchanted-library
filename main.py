import sys
from patterns.facade import LibraryManagementFacade
from patterns.factory.user_factory import UserFactory
from patterns.factory.book_factory import BookFactory  
from patterns.book_builder import BookBuilder
from utils.constants import UserRole, BookType

def main():
    library = LibraryManagementFacade()
    
    while True:
        print("\n--- Ancient Library Management System ---")
        print("1. Register User")
        print("2. Add New Book")  
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Search Catalog")
        print("6. Show Available Books")
        print("7. List All Users")
        print("8. Exit")
        
        choice = input("\nSelect an option: ")

        if choice == "1":
            uid = input("User ID: "); name = input("Name: "); pwd = input("Password: ")
            print("1. Librarian, 2. Scholar, 3. Guest")
            role_choice = input("Select Role: ")
            roles = {"1": UserRole.LIBRARIAN, "2": UserRole.SCHOLAR, "3": UserRole.GUEST}
            user = UserFactory.create_user(uid, pwd, name, roles.get(role_choice, UserRole.GUEST))
            print(library.register_user(user))

        elif choice == "2":
            print("\n--- Book Registration ---")
            print("a. Standard Registration (Quick)")
            print("b. Detailed Registration (Custom Builder)")
            sub_choice = input("Select method: ").lower()

            bid = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            print("1. Ancient, 2. Rare, 3. General")
            t_choice = input("Type: ")
            types = {"1": BookType.ANCIENT_SCRIPT, "2": BookType.RARE_BOOK, "3": BookType.GENERAL_BOOK}
            b_type = types.get(t_choice, BookType.GENERAL_BOOK)

            if sub_choice == "a":
                book_obj = BookFactory.create_book(bid, title, author, b_type)
            else:
                builder = BookBuilder(bid, title, author, b_type)
                
                pres = input("Preservation Notes: ")
                digi = input("Enable Digital Access? (y/n): ").lower() == 'y'
                rest = input("Enter special restriction (or leave blank): ")
                
                builder.set_preservation(pres).enable_digital_access(digi)
                if rest: builder.add_restriction(rest)
                
                book_obj = builder.build()
            
            print(library.register_new_book(book_obj))

        elif choice == "3":
            print(library.borrow_book(input("User ID: "), input("Password: "), input("Book ID: ")))

        elif choice == "4":
            print(library.return_book(input("Enter Book ID: ")))

        elif choice == "5":
            print(library.search_books(input("Search: ")))

        elif choice == "6":
            print(library.show_available_collection())

        elif choice == "7":
            print(library.list_all_users())

        elif choice == "8":
            sys.exit("Good Bye.")

if __name__ == "__main__":
    main()
