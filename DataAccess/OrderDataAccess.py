from Models.OrderModel import Order
from DataAccess.ConnectionString import *
from datetime import *
import struct
import pyodbc



class OrderDataAccess:
    def __init__(self,order:Order=None):
        self.AllData = []
        self.ConnectionString = f'Driver={"{SQL SERVER}"};Server={Server};Database={DB_Name};UID={UserName};PWD={Password};'
        self.Order = order


    def spGetOrder(self):
        commandTextSP = 'EXEC SP_GetOrder'
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
            aa = type(row)
            bb = tuple(row)
            self.AllData.append(bb)


    def spInsertOrder(self):
        commandTextSP = 'EXEC SP_RegisterOrder @CustomerID =?,@EmployeeID =?,@OrderDate  =?,@RequiretedDate=?,' \
                        '@ShippedeDate  =?,@ShipVia=?,@Freight =?,@ShipName =?,@ShipAddress=?,@ShipCity =?,' \
                        '@ShipRegion =?,@ShipPostalCode=?,@ShipCountry =?'
        params = (self.Order.CustomerID, self.Order.EmployeeID,self.Order.OrderDate, self.Order.RequiretedDate,
                  self.Order.ShippedeDate, self.Order.ShipVia, self.Order.Freight, self.Order.ShipName,
                  self.Order.ShipAddress,self.Order.ShipCity, self.Order.ShipRegion, self.Order.ShipPostalCode,
                  self.Order.ShipCountry)
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            sqlConnection.commit()


    def spUpdateOrder(self, orderId):
        #
        commandTextSP = 'EXEC SP_RegisterOrder @OrderId,@CustomerID =?,@EmployeeID =?, @OrderDate  =?,@RequiretedDate=?,' \
                        '@ShippedeDate  =?,@ShipVia=?,@Freight =?,@ShipName =?,@ShipAddress=?,@ShipCity =?,' \
                        '@ShipRegion =?,@ShipPostalCode=?,@ShipCountry =?'
        params = (orderId,self.Order.CustomerID, self.Order.EmployeeID, self.Order.OrderDate, self.Order.RequiretedDate,
                  self.Order.ShippedeDate, self.Order.ShipVia, self.Order.Freight, self.Order.ShipName,
                  self.Order.ShipAddress,self.Order.ShipCity, self.Order.ShipRegion, self.Order.ShipPostalCode,
                  self.Order.ShipCountry)
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            sqlConnection.commit()
            sqlConnection.commit()


    def spDeleteOrder(self):
        commandTextSP = 'EXEC SP_DeleteOrder @OrderID = ?'
        params = (self.Order)
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            sqlConnection.commit()


    def spGetCustomerList(self):
        customerList=[]
        commandTextSP = 'EXEC GetCustomerList '
        params = ()
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            rows = cursor.fetchall()
            sqlConnection.commit()
        for row in rows:
            if len(row) >= 2:  # Check if row has at least two elements
                customerList.append(str(row[0]) + '-' + row[1])

        return customerList

    def spGetEmployeeList(self):
        employeeList=[]
        commandTextSP = 'EXEC GetEmployeeList '
        params = ()
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            rows = cursor.fetchall()
            sqlConnection.commit()
        for row in rows:
            if len(row) >= 2:  # Check if row has at least two elements
                employeeList.append(str(row[0]) + '-' + row[1])

        return employeeList

    def spGetShipViaList(self):
        shipViaList=[]
        commandTextSP = 'EXEC GetShipViaList '
        params = ()
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            rows = cursor.fetchall()
            sqlConnection.commit()
        for row in rows:
            if len(row) >= 2:  # Check if row has at least two elements
                shipViaList.append(str(row[0]) + '-' + row[1])

        return shipViaList