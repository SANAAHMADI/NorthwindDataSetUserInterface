class OrderDetailes:
    def __init__(self, orderID, productID, unitPrice, quantity=None, discount=None):
        self.OrderID  =  orderID
        self.ProductID= productID
        self.UnitPrice= unitPrice
        self.Quantity = quantity
        self.Discount = discount


# class OrderDetailesIdDelete:
#     def __init__(self, orderDetailesID=None):
#         self.OrderDetailesID = orderDetailesID


