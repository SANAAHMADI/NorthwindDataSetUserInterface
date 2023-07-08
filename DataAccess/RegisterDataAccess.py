from DataAccess.ConnectionString import *
from datetime import *
import struct
import pyodbc

from Models.RegisterModel import RegisterUser


class RegisterUserDataAccess:
    def __init__(self,registerUser:RegisterUser=None):
        self.AllData = []
        self.ConnectionString = f'Driver={"{SQL SERVER}"};Server={Server};Database={DB_Name};UID={UserName};PWD={Password};'
        self.RegisterUser = registerUser

    def spInsertRegisterUser(self):
        commandTextSP = 'EXEC [dbo].[UserRegister] @UserName =?, @Password =?, @FirstName =? , @LastName =? , @isAdmin =?'
        params = (self.RegisterUser.UserName, self.RegisterUser.Password,self.RegisterUser.FirstName,self.RegisterUser.LastName,self.RegisterUser.isAdmin)
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            sqlConnection.commit()
    # def spGetEmployee(self):
    #     commandTextSP = 'EXEC SP_GetEmployee'
    #     with pyodbc.connect(self.ConnectionString) as sqlConnection:
    #         def handle_datetimeoffset(dto_value):
    #             tup = struct.unpack("<6hI2h", dto_value)
    #             return datetime(tup[0], tup[1], tup[2])
    #         cursor = sqlConnection.cursor()
    #         sqlConnection.add_output_converter(-155, handle_datetimeoffset)
    #         cursor.execute(commandTextSP).fetchval()
    #         data = cursor.fetchall()
    #         sqlConnection.commit()
    #     for row in data:
    #         aa= type(row)
    #         bb = tuple(row)
    #         self.AllData.append(bb)





    #
    # def spUpdateEmployee(self, employeeId):
    #     commandTextSP = 'EXEC [dbo].[SP_UpdateEmployee] @employeeId =?, @LastName =? ,@FirstName  =? ' \
    #                     ',@Title  =?  ,@TitleOfCourtesy  =? ,@BirthDate  =? ,@HireDate  =? ,@Address  =? ,' \
    #                     '@City =? ,@Region =? ,@PostalCode =? ' \
    #                     ',@Country =? ,@HomePhone  =? ,@Extension  =?  ,@Notes =? '
    #     params = ( employeeId ,self.Employee.LastName, self.Employee.FirstName, self.Employee.Title, self.Employee.TitleOfCourtesy,
    #               self.Employee.BirthDate, self.Employee.HireDate, self.Employee.Address, self.Employee.City,self.Employee.Region,
    #               self.Employee.PostalCode, self.Employee.Country, self.Employee.HomePhone, self.Employee.Extension,self.Employee.Notes)
    #     with pyodbc.connect(self.ConnectionString) as sqlConnection:
    #         cursor = sqlConnection.cursor()
    #         cursor.execute(commandTextSP, params)
    #         sqlConnection.commit()
    # def spDeleteEmployee(self):
    #     commandTextSP = 'EXEC [dbo].[SP_DeleteEmployee] @EmployeeID = ?'
    #     params = (self.Employee)
    #     with pyodbc.connect(self.ConnectionString) as sqlConnection:
    #         cursor = sqlConnection.cursor()
    #         cursor.execute(commandTextSP, params)
    #         sqlConnection.commit()
    #
    #
