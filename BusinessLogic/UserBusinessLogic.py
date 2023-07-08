from Models.UserModel import User
from DataAccess.UserDataAccess import UserDataAccess


class UserBusinessLogic:
    def __init__(self, user: User):
        self.User = user

    def getUserInfo(self):
        userDALObject = UserDataAccess(user=self.User)
        return userDALObject.getUserInfo()


