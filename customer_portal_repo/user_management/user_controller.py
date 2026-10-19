from .user_service import UserService

class UserController:
    def __init__(self):
        self.service = UserService()

    def register_user(self,payload):
        for field in ["name","email"]:
            if field not in payload:
                raise ValueError(f"Missing {field}")
        return self.service.create_user(payload)
