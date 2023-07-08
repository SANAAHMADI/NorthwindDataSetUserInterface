from Models.EmployeeModel import Employee
from DataAccess.ConnectionString import *
from datetime import *
import struct
import pyodbc


class EmployeeDataAccess:
    def __init__(self,employee:Employee=None):
        self.AllData = []
        self.ConnectionString = f'Driver={"{SQL SERVER}"};Server={Server};Database={DB_Name};UID={UserName};PWD={Password};'
        self.Employee = employee

    def spGetEmployee(self):
        commandTextSP = 'EXEC SP_GetEmployee'
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            def handle_datetimeoffset(dto_value):
                tup = struct.unpack("<6hI2h", dto_value)
                return datetime(tup[0], tup[1], tup[2])
            cursor = sqlConnection.cursor()
            sqlConnection.add_output_converter(-155, handle_datetimeoffset)
            cursor.execute(commandTextSP).fetchval()
            data = cursor.fetchall()
            sqlConnection.commit()
        for row in data:
            aa= type(row)
            bb = tuple(row)
            self.AllData.append(bb)


    def spInsertEmployee(self):
        commandTextSP = 'EXEC EmployeeRegister @lastName =?, @firstName =?, @title =? , @titleOfCourtesy =? , @birthDate =? , @hireDate =? , ' \
                        '@address =? , @city=? , @region =?, @postalCode =?, @country =? , @homePhone =?, @extension =? ,' \
                        ' @notes =? '
        params = (self.Employee.LastName, self.Employee.FirstName, self.Employee.Title, self.Employee.TitleOfCourtesy,
                  self.Employee.BirthDate, self.Employee.HireDate, self.Employee.Address, self.Employee.City,self.Employee.Region,
                  self.Employee.PostalCode, self.Employee.Country, self.Employee.HomePhone, self.Employee.Extension,
                  self.Employee.Notes)
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            sqlConnection.commit()

    def spUpdateEmployee(self, employeeId):
        commandTextSP = 'EXEC [dbo].[SP_UpdateEmployee] @employeeId =?, @LastName =? ,@FirstName  =? ' \
                        ',@Title  =?  ,@TitleOfCourtesy  =? ,@BirthDate  =? ,@HireDate  =? ,@Address  =? ,' \
                        '@City =? ,@Region =? ,@PostalCode =? ' \
                        ',@Country =? ,@HomePhone  =? ,@Extension  =?  ,@Notes =? '
        params = ( employeeId ,self.Employee.LastName, self.Employee.FirstName, self.Employee.Title, self.Employee.TitleOfCourtesy,
                  self.Employee.BirthDate, self.Employee.HireDate, self.Employee.Address, self.Employee.City,self.Employee.Region,
                  self.Employee.PostalCode, self.Employee.Country, self.Employee.HomePhone, self.Employee.Extension,self.Employee.Notes)
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            sqlConnection.commit()
    def spDeleteEmployee(self):
        commandTextSP = 'EXEC [dbo].[SP_DeleteEmployee] @EmployeeID = ?'
        params = (self.Employee)
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            sqlConnection.commit()


