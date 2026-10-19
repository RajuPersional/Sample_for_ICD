from .user_repository import UserRepository

class UserService:
    def __init__(self):
        self.repo = UserRepository()

    def create_user(self,payload):
        existing=self.repo.find_by_email(payload["email"])
        if existing:
            raise Exception("User exists")

        user={
            "name":payload["name"],
            "email":payload["email"],
            "status":"ACTIVE"
        }
        return self.repo.save(user)
