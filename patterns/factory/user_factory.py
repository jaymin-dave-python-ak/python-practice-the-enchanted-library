from models.user import Librarian, Scholar, Guest

class UserFactory:
    @staticmethod
    def create_user(user_id, password, name, role):
        if role == "LIBRARIAN":
            return Librarian(user_id, password, name)
        elif role == "SCHOLAR":
            return Scholar(user_id, password, name)
        elif role == "GUEST":
            return Guest(user_id, password, name)
        else:
            raise ValueError("Invalid user role")