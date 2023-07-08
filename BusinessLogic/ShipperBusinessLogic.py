from Models.ShipperModel import Shipper
from DataAccess.ShipperDataAccess import ShipperDataAccess

class ShipperBusinessLogic:
    def __init__(self, shipper: Shipper = None):
        self.Shipper = shipper
        self.AllDataShipper = []

    def getShipper(self):
        GetShipperDALObject = ShipperDataAccess()
        GetShipperDALObject.spGetShipper()
        self.AllDataShipper = GetShipperDALObject.AllData

    def insertShipper(self):
        insertShipperDALObject = ShipperDataAccess(self.Shipper)
        insertShipperDALObject.spInsertShipper()

    def updateShipper(self, ShipperId):
        updateShipperDALObject = ShipperDataAccess(self.Shipper)
        updateShipperDALObject.spUpdateShipper(ShipperId)

    def deleteShipper(self, ShipperId):
        deleteShipperDALObject = ShipperDataAccess(ShipperId)
        deleteShipperDALObject.spDeleteShipper()
