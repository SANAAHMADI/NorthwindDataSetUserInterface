class Order:
    def __init__(self,
                 customerID,
                 employeeID,
                 orderDate=None,
                 requiredDate=None,
                 shippedDate=None,
                 shipVia=None,
                 freight=None,
                 shipName=None,
                 shipAddress=None,
                 shipCity=None,
                 shipRegion=None,
                 shipPostalCode=None,
                 shipCountry=None
                 ):
        self.CustomerID = customerID
        self.EmployeeID = employeeID
        self.OrderDate = orderDate
        self.RequiredDate = requiredDate
        self.ShippedDate = shippedDate
        self.ShipVia = shipVia
        self.Freight = freight
        self.ShipName = shipName
        self.ShipAddress = shipAddress
        self.ShipCity = shipCity
        self.ShipRegion = shipRegion
        self.ShipPostalCode = shipPostalCode
        self.ShipCountry = shipCountry

class OrderIdDelete:
    def __init__(self, orderID = None):
        self.OrderID = orderID


