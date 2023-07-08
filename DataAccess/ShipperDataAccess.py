from Models.ShipperModel import *
from DataAccess.ConnectionString import *
from datetime import *
import struct
import pyodbc


class ShipperDataAccess:
    def __init__(self,shipper:Shipper=None):
        self.AllData = []
        self.ConnectionString = f'Driver={"{SQL SERVER}"};Server={Server};Database={DB_Name};UID={UserName};PWD={Password};'
        self.Shipper = shipper

    def spGetShipper(self):
        commandTextSP = 'EXEC GetShipper'
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


    def spInsertShipper(self):
        commandTextSP = 'EXEC ShipperRegister @companyName = ?, @phone=?'
        params = (self.Shipper.CompanyName, self.Shipper.Phone)
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            sqlConnection.commit()

    def spUpdateShipper(self, ShipperId):
        commandTextSP = 'EXEC [dbo].[UpdateShipper] @ShipperID=?, @companyName = ?, @phone=?'
        params = ( ShipperId ,self.Shipper.CompanyName, self.Shipper.Phone)
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            sqlConnection.commit()
    def spDeleteShipper(self):
        commandTextSP = 'EXEC [dbo].[DeleteShipper] @ShipperID = ?'
        params = (self.Shipper)
        with pyodbc.connect(self.ConnectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandTextSP, params)
            sqlConnection.commit()


