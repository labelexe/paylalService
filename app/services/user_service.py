from app.models import User


class UserService:
    def __init__(self):
        self.users = []

    def create_user(self, user: User):
        user.id = len(self.users) + 1
        self.users.append(user)
        return user

    def get_user(self, user_id: int):
        for user in self.users:
            if user.id == user_id:
                return user
        return None
