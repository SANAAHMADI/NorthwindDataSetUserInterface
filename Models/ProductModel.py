class Product:
    def __init__(self, productName, supplierID, categoryID, quantityPerUnit=None, unitPrice=None,
                 unitsInStock=None, unitsOnOrder=None,reorderLevel=None, discontinued=None):
        self.ProductName = productName
        self.SupplierID = supplierID
        self.CategoryID = categoryID
        self.QuantityPerUnit = quantityPerUnit
        self.UnitPrice = unitPrice
        self.UnitsInStock = unitsInStock
        self.UnitsOnOrder = unitsOnOrder
        self.ReorderLevel = reorderLevel
        self.Discontinued = discontinued


class ProductIdDelete:
    def __init__(self, productID=None):
        self.ProductID = productID
