class User:
    def __init__(self, username: str, password: str):
        self.Username = username
        self.Password = password

    def Login(self, username: str, password: str):
        if self.Username == username and self.Password == password:
            return True
        else:
            return False
