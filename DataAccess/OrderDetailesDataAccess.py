from Models.OrderDetailesModel import OrderDetailes
from Models.ProductModel import Product
from DataAccess.ConnectionString import *
from datetime import *
import struct
import pyodbc


class OrderDetailesDataAccess:
    def __init__(self,orderDetailes:OrderDetailes=None):
        self.AllData = []
        self.ConnectionString = f'Driver={"{SQL SERVER}"};Server={Server};Database={DB_Name};UID={UserName};PWD={Password};'
        self.OrderDetailes = orderDetailes

    def spGetOrderDetailes(self):
        commandTextSP = 'EXEC GetOrderDetailes'
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


    def spInsertOrderDetailes(self):
        commandTextSP = 'EXEC OrderDetailesRegister @OrderID  =?,@ProductID=?,@UnitPrice=?,@Quantity =?,@Discount =?'
        params = (
                    self.OrderDetailes.OrderID
                   ,self.OrderDetailes.ProductID
                   ,self.OrderDetailes.UnitPrice
                   ,self.OrderDetailes.Quantity
                   ,self.OrderDetailes.Discount )
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            sqlConnection.commit()

    def spUpdateOrderDetailes(self, orderDetailesId):
        commandTextSP = 'EXEC [dbo].[UpdateOrderDetailes] @OrderID  =?,@ProductID=?,@UnitPrice=?,@Quantity =?,@Discount =?'

        params = ( orderDetailesId
                   ,self.OrderDetailes.OrderID
                   ,self.OrderDetailes.ProductID
                   ,self.OrderDetailes.UnitPrice
                   ,self.OrderDetailes.Quantity
                   ,self.OrderDetailes.Discount

                   )
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            sqlConnection.commit()
    def spDeleteOrderDetailes(self):
        commandTextSP = 'EXEC [dbo].[DeleteOrderDetailes] @OrderDetailesID = ?'
        params = (self.OrderDetailes)
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            sqlConnection.commit()


    def spGetProductList(self):
        productList=[]
        commandTextSP = 'EXEC GetProductList '
        params = ()
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            rows = cursor.fetchall()
            sqlConnection.commit()
        for row in rows:
            productList.append(str(row[0])+'-'+row[1])

        return productList

    def spGetOrderList(self):
        orderList=[]
        commandTextSP = 'EXEC GetOrderList '
        params = ()
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            rows = cursor.fetchall()
            sqlConnection.commit()
        for row in rows:
            orderList.append(str(row[0])+'-'+row[1])

        return orderList

