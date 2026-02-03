from models.user import Librarian, Scholar, Guest, UserRole

class UserFactory:
    @staticmethod
    def create_user(user_id, password, name, role):
        if role == UserRole.LIBRARIAN:
            return Librarian(user_id, password, name)
        elif role == UserRole.SCHOLAR:
            return Scholar(user_id, password, name)
        elif role == UserRole.GUEST:
            return Guest(user_id, password, name)
        else:
            raise ValueError("Invalid user role")