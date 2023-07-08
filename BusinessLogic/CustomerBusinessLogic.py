from Models.CustomerModel import Customer
from DataAccess.CustomerDataAccess import CustomerDataAccess

class CustomerBusinessLogic:
    def __init__(self,customer:Customer=None):
        self.Customer = customer
        self.AllDataCustomer = []

    def getCustomer(self):
        GetCustomerDALObject = CustomerDataAccess()
        GetCustomerDALObject.spGetCustomer()
        self.AllDataCustomer = GetCustomerDALObject.AllData

    def insertCustomer(self):
        insertCustomerDALObject = CustomerDataAccess(self.Customer)
        insertCustomerDALObject.spInsertCustomer()

    def updateCustomer(self,CustomerId):
        updateCustomerDALObject = CustomerDataAccess(self.Customer)
        updateCustomerDALObject.spUpdateCustomer(CustomerId)

    def deleteCustomer(self,CustomerId):
        deleteCustomerDALObject = CustomerDataAccess(CustomerId)
        deleteCustomerDALObject.spDeleteCustomer()

