from Models.ProductModel import Product
from DataAccess.ConnectionString import *
from datetime import *
import struct
import pyodbc


class ProductDataAccess:
    def __init__(self,product:Product=None):
        self.AllData = []
        self.ConnectionString = f'Driver={"{SQL SERVER}"};Server={Server};Database={DB_Name};UID={UserName};PWD={Password};'
        self.Product = product

    def spGetProduct(self):
        commandTextSP = 'EXEC GetProduct'
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


    def spInsertProduct(self):
        commandTextSP = 'EXEC ProductRegister 	@ProductName=?	,@SupplierID=?	,@CategoryID=?	,' \
                        '@QuantityPerUnit=?, @UnitPrice=?	,@UnitsInStock=?	,@UnitsOnOrder=?	,@ReorderLevel=?' \
                        '	,@Discontinued=?'
        params = (
                   # self.Product.ProductID
                   self.Product.ProductName
                   ,self.Product.SupplierID
                   ,self.Product.CategoryID
                   ,self.Product.QuantityPerUnit
                   ,self.Product.UnitPrice
                   ,self.Product.UnitsInStock
                   ,self.Product.UnitsOnOrder
                   ,self.Product.ReorderLevel
                   ,self.Product.Discontinued)
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            sqlConnection.commit()

    def spUpdateProduct(self, productId):
        commandTextSP = 'EXEC [dbo].[UpdateProduct] @ProductID=?	,@ProductName	=?	,@SupplierID=?	,@CategoryID=?	,' \
                        '@QuantityPerUnit=?,@UnitPrice=?	,@UnitsInStock	=?	,@UnitsOnOrder	=?	,@ReorderLevel	=?' \
                        '	,@Discontinued	=? '
        params = ( productId
                   ,self.Product.ProductName
                   ,self.Product.SupplierID
                   ,self.Product.CategoryID
                   ,self.Product.QuantityPerUnit
                   ,self.Product.UnitPrice
                   ,self.Product.UnitsInStock
                   ,self.Product.UnitsOnOrder
                   ,self.Product.ReorderLevel
                   ,self.Product.Discontinued
                   )
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            sqlConnection.commit()
    def spDeleteProduct(self):
        commandTextSP = 'EXEC [dbo].[DeleteProduct] @ProductID = ?'
        params = (self.Product)
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            sqlConnection.commit()


    def spGetCategoryList(self):
        categoryList=[]
        commandTextSP = 'EXEC GetCategoryList '
        params = ()
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            rows = cursor.fetchall()
            sqlConnection.commit()
        for row in rows:
            categoryList.append(str(row[0])+'-'+row[1])

        return categoryList

    def spGetSupplierList(self):
        supplierList=[]
        commandTextSP = 'EXEC GetSupplierList '
        params = ()
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            rows = cursor.fetchall()
            sqlConnection.commit()
        for row in rows:
            supplierList.append(str(row[0])+'-'+row[1])

        return supplierList

