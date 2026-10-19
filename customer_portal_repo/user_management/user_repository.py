class UserRepository:
    users=[]

    def find_by_email(self,email):
        for user in self.users:
            if user["email"]==email:
                return user
        return None

    def save(self,user):
        self.users.append(user)
        return {"message":"User created","user":user}
