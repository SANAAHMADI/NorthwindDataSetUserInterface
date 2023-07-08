from Models.SupplierModel import Supplier
from DataAccess.ConnectionString import *
from datetime import *
import struct
import pyodbc


class SupplierDataAccess:
    def __init__(self,supplier:Supplier=None):
        self.AllData = []
        self.ConnectionString = f'Driver={"{SQL SERVER}"};Server={Server};Database={DB_Name};UID={UserName};PWD={Password};'
        self.Supplier = supplier

    def spGetSupplier(self):
        commandTextSP = 'EXEC GetSupplier'
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


    def spInsertSupplier(self):
        commandTextSP = 'EXEC SupplierRegister @CompanyName=? ,@ContactName=?,@ContactTitle=?,@Address=?,@City=?,' \
                        '@Region=?,@PostalCode=?,@Country=?,@Phone=?,@Fax=?,@HomePage=?'
        params = (
             self.Supplier.CompanyName
            ,self.Supplier.ContactName
            ,self.Supplier.ContactTitle
            ,self.Supplier.Address
            ,self.Supplier.City
            ,self.Supplier.Region
            ,self.Supplier.PostalCode
            ,self.Supplier.Country
            ,self.Supplier.Phone
            ,self.Supplier.Fax
            ,self.Supplier.HomePage
        )
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            sqlConnection.commit()

    def spUpdateSupplier(self, supplierId):
        commandTextSP = 'EXEC [dbo].[UpdateSupplier] @SupplierId =?, @CompanyName=?,@ContactName=?,@ContactTitle=?,' \
                        '@Address=?,@City=?,' \
                        '@Region=?,@PostalCode=?,@Country=?,@Phone=?,@Fax=?,@HomePage=? '
        params = ( supplierId
                   ,self.Supplier.CompanyName
            ,self.Supplier.ContactName
            ,self.Supplier.ContactTitle
            ,self.Supplier.Address
            ,self.Supplier.City
            ,self.Supplier.Region
            ,self.Supplier.PostalCode
            ,self.Supplier.Country
            ,self.Supplier.Phone
            ,self.Supplier.Fax
            ,self.Supplier.HomePage)


        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            sqlConnection.commit()
    def spDeleteSupplier(self):
        commandTextSP = 'EXEC [dbo].[DeleteSupplier] @SupplierID = ?'
        params = (self.Supplier)
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            sqlConnection.commit()


