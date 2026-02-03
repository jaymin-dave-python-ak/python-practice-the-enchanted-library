from models.user import *

class UserFactory:
    @staticmethod
    def create_user(user_id, name, role):
        if role == UserRole.LIBRARIAN:
            return Librarian(user_id, name)
        elif role == UserRole.SCHOLAR:
            return Scholar(user_id, name)
        elif role == UserRole.GUEST:
            return Guest(user_id, name)
        else:
            raise ValueError("Invalid user role")
