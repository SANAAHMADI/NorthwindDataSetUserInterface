from Models.CategoryModel import Category
from DataAccess.ConnectionString import *
from datetime import *
import struct
import pyodbc


class CategoryDataAccess:
    def __init__(self,category:Category=None):
        self.AllData = []
        self.ConnectionString = f'Driver={"{SQL SERVER}"};Server={Server};Database={DB_Name};UID={UserName};PWD={Password};'
        self.Category = category

    def spGetCategory(self):
        commandTextSP = 'EXEC [dbo].[GetCategory]'
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


    def spInsertCategory(self):
        commandTextSP = 'EXEC CategoryRegister 	@CategoryName=? , @Description=? ,@Picture=?'
        params = (
                   # self.Product.ProductID
                    self.Category.CategoryName
                   ,self.Category.Description
                   ,self.Category.Picture)
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            sqlConnection.commit()

    def spUpdateCategory(self, categoryId):
        commandTextSP = 'EXEC [dbo].[UpdateCategory]  @CategoryID=?,@CategoryName=?,@Description =?,@Picture =?'
        params = ( categoryId
                   ,self.Category.CategoryName
                   , self.Category.Description
                   , self.Category.Picture
                   )
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            sqlConnection.commit()
    def spDeleteCategory(self):
        commandTextSP = 'EXEC [dbo].[DeleteCategory] @CategoryID = ?'
        params = (self.Category)
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            sqlConnection.commit()


    # def spGetCategoryList(self):
    #     categoryList=[]
    #     commandTextSP = 'EXEC GetCategoryList '
    #     params = ()
    #     with pyodbc.connect(self.ConnectionString) as sqlConnection:
    #         cursor = sqlConnection.cursor()
    #         cursor.execute(commandTextSP, params)
    #         rows = cursor.fetchall()
    #         sqlConnection.commit()
    #     for row in rows:
    #         categoryList.append(str(row[0])+'-'+row[1])
    #
    #     return categoryList
    #
    # def spGetSupplierList(self):
    #     supplierList=[]
    #     commandTextSP = 'EXEC GetSupplierList '
    #     params = ()
    #     with pyodbc.connect(self.ConnectionString) as sqlConnection:
    #         cursor = sqlConnection.cursor()
    #         cursor.execute(commandTextSP, params)
    #         rows = cursor.fetchall()
    #         sqlConnection.commit()
    #     for row in rows:
    #         supplierList.append(str(row[0])+'-'+row[1])
    #
    #     return supplierList

