class User:
    def __init__(self, username, password, firstname=None, lastname=None, is_admin=0):
        self.UserName = username
        self.Password = password
        self.FirstName = firstname
        self.LastName = lastname
        self.isAdmin = is_admin
