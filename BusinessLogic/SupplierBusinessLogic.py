from Models.SupplierModel import Supplier
from DataAccess.SupplierDataAccess import SupplierDataAccess

class SupplierBusinessLogic:
    def __init__(self, supplier: Supplier = None):
        self.Supplier = supplier
        self.AllDataSupplier = []

    def getSupplier(self):
        GetSupplierDALObject = SupplierDataAccess()
        GetSupplierDALObject.spGetSupplier()
        self.AllDataSupplier = GetSupplierDALObject.AllData

    def insertSupplier(self):
        insertSupplierDALObject = SupplierDataAccess(self.Supplier)
        insertSupplierDALObject.spInsertSupplier()

    def updateSupplier(self, SupplierId):
        updateSupplierDALObject = SupplierDataAccess(self.Supplier)
        updateSupplierDALObject.spUpdateSupplier(SupplierId)

    def deleteSupplier(self, SupplierId):
        deleteSupplierDALObject = SupplierDataAccess(SupplierId)
        deleteSupplierDALObject.spDeleteSupplier()
