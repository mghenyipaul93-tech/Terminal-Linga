 
 class UserService:
    def __init__(self):
        self.users = {}
        self.counter = 1

    def _generate_id(self):
        user_id = self.counter
        self.counter += 1
        return user_id

    def create_user(self, name, email):
        if not name:
            raise ValueError("Name cannot be empty.")
        if not email:
            raise ValueError("Email cannot be empty.")

        user_id = self._generate_id()

        user = {
            "id": user_id,
            "name": name,
            "email": email
        }

        self.users[user_id] = user
        return user

    def get_user_by_id(self, user_id):
        return self.users.get(user_id)

    def get_all_users(self):
        return list(self.users.values())