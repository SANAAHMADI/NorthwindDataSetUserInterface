from Models.OrderModel import Order
from DataAccess.OrderDataAccess import OrderDataAccess


class OrderBusinessLogic:
    def __init__(self,order:Order=None):
        self.Order = order
        self.AllDataOrder = []

    def getOrder(self):
        GetOrderDALObject = OrderDataAccess()
        GetOrderDALObject.spGetOrder()
        self.AllDataOrder = GetOrderDALObject.AllData

    def insertOrder(self):
        insertOrderDALObject = OrderDataAccess(self.Order)
        insertOrderDALObject.spInsertOrder()

    def updateOrder(self, OrderId):
        updateOrderDALObject = OrderDataAccess(self.Order)
        updateOrderDALObject.spUpdateOrder(OrderId)

    def deleteOrder(self, OrderId):
        deleteOrderDALObject = OrderDataAccess(OrderId)
        deleteOrderDALObject.spDeleteOrder()


    def getCustomerList(self):
        customerDALObject = OrderDataAccess()
        return customerDALObject.spGetCustomerList()

    def getEmployeeList(self):
        employeeDALObject = OrderDataAccess()
        return employeeDALObject.spGetEmployeeList()

    def getShipViaList(self):
        shipViaDALObject = OrderDataAccess()
        return shipViaDALObject.spGetShipViaList()