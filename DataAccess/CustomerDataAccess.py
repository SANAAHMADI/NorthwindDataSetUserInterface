from Models.CustomerModel import Customer
from DataAccess.ConnectionString import *
from datetime import *
import struct
import pyodbc


class CustomerDataAccess:
    def __init__(self, customer: Customer = None):
        self.AllData = []
        self.ConnectionString = f'Driver={"{SQL SERVER}"};Server={Server};Database={DB_Name};UID={UserName};PWD={Password};'
        self.Customer = customer

    def spGetCustomer(self):
        commandTextSP = 'EXEC SP_GetCustomer'
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            def handle_datetimeoffset(dto_value):
                tup = struct.unpack("<6hI2h", dto_value)
                return datetime(tup[0], tup[1], tup[2])
            cursor = sqlConnection.cursor()
            sqlConnection.add_output_converter(-155, handle_datetimeoffset)
            cursor.execute(commandTextSP)
            data = cursor.fetchall()
            sqlConnection.commit()
        for row in data:
            aa = type(row)
            bb = tuple(row)
            self.AllData.append(bb)

    def spInsertCustomer(self):
        commandTextSP = 'EXEC SP_RegisterCustomer @CustomerID = ?, @CompanyName = ?,  @ContactName = ?, @ContactTitle = ?,' \
                        ' @ADDRESS = ?, @City = ? , @Region = ? ,@PostalCode = ? ,@Country = ? ,@Phone = ? ,@Fax = ?'
        params = (self.Customer.CustomerID, self.Customer.CompanyName,self.Customer.ContactName,self.Customer.ContactTitle,
                  self.Customer.ADDRESS,self.Customer.City,self.Customer.Region,self.Customer.PostalCode,
                  self.Customer.Country,self.Customer.Phone,self.Customer.Fax)
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            sqlConnection.commit()

    def spUpdateCustomer(self,customerID):
        commandTextSP = 'EXEC [dbo].[SP_UpdtaeCustomer] @CustomerID = ?, @CompanyName = ?, @ContactName = ?, @ContactTitle =?,' \
                        ' @Address = ?, @City = ?, @Region = ?, @PostalCode =?, @Country =?, @Phone = ?, @Fax =   ?'
        params = (self.Customer.CustomerID,self.Customer.CompanyName,self.Customer.ContactName,self.Customer.ContactTitle,
                  self.Customer.ADDRESS,self.Customer.City,self.Customer.Region,
                  self.Customer.PostalCode,self.Customer.Country,self.Customer.Phone,self.Customer.Fax)
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            sqlConnection.commit()


    def spDeleteCustomer(self):
        commandTextSP = 'EXEC [dbo].[SP_DeleteCustomer] @CustomerID = ?'
        params = (self.Customer)
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            sqlConnection.commit()



