from Models.OrderDetailesModel import OrderDetailes
# from DataAccess.OrderDetailesDataAccess import orderDetailesDataAccess
from Models.OrderDetailesModel import OrderDetailes
from DataAccess.OrderDetailesDataAccess import OrderDetailesDataAccess

class OrderDetailesBusinessLogic:
    def __init__(self, orderDetailes: OrderDetailes = None):
        self.OrderDetailes = orderDetailes
        self.AllDataOrderDetailes = []

    def getOrderDetailes(self):
        GetOrderDetailesDALObject = OrderDetailesDataAccess()
        GetOrderDetailesDALObject.spGetOrderDetailes()
        self.AllDataOrderDetailes = GetOrderDetailesDALObject.AllData

    def insertOrderDetailes(self):
        insertOrderDetailesDALObject = OrderDetailesDataAccess(self.OrderDetailes)
        insertOrderDetailesDALObject.spInsertOrderDetailes()

    def updateOrderDetailes(self, OrderDetailesId):
        updateOrderDetailesDALObject = OrderDetailesDataAccess(self.OrderDetailes)
        updateOrderDetailesDALObject.spUpdateOrderDetailes(OrderDetailesId)


    def deleteOrderDetailes(self, OrderDetailesId):
        deleteOrderDetailesDALObject = OrderDetailesDataAccess(OrderDetailesId)
        deleteOrderDetailesDALObject.spDeleteOrderDetailes()

    def getCategoryList(self):
        OrderDetailesDALObject = OrderDetailesDataAccess()
        return OrderDetailesDALObject.spGetCategoryList()

    def getSupplierList(self):
        OrderDetailesDALObject = OrderDetailesDataAccess()
        return OrderDetailesDALObject.spGetSupplierList()