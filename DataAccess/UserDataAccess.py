import pyodbc
from Models.UserModel import User
from DataAccess.ConnectionString import *


class UserDataAccess:
    def __init__(self, user: User):
        self.User = user

    def getUserInfo(self):
        commandTextSP = 'EXEC [dbo].[SP_UserLogin] ?,?'
        connectionString = f'Driver={"{SQL SERVER}"};Server={Server};Database={DB_Name};UID={UserName};PWD={Password};'
        params = (self.User.UserName.lower(), self.User.Password)
        with pyodbc.connect(connectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            rows = cursor.fetchall()
            sqlConnection.commit()
        if len(rows) > 0:
            self.User.FirstName = rows[0][3]
            self.User.LastName = rows[0][4]
        return self.User

    def insertUser(self):
        pass
        # commandTextSP = 'EXEC	[dbo].[InsertEmployee] @FirstName =?,@LastName = ?,@NationalCode = ?,@Birthdate = ?,@Sex = ?,@DepartmentID = ?'
        # connectionString = 'Driver={SQL SERVER};Server=SEMATEC;Database=SematecLMS;UID=sa;PWD=123;'
        # params = (self.Employee.FirstName, self.Employee.LastName, self.Employee.NationalCode, self.Employee.Birthdate,
        #           self.Employee.Sex, self.Employee.DepartmentID)
        # with pyodbc.connect(connectionString) as sqlConnection:
        #     cursor = sqlConnection.cursor()
        #     cursor.execute(commandTextSP, params)
        #     sqlConnection.commit()

    def updateUser(self):
        pass

    def deleteUser(self):
        pass


