from Models.ProductModel import Product
from DataAccess.ProductDataAccess import ProductDataAccess

class productBusinessLogic:
    def __init__(self, product: Product = None):
        self.Product = product
        self.AllDataProduct = []

    def getProduct(self):
        GetProductDALObject = ProductDataAccess()
        GetProductDALObject.spGetProduct()
        self.AllDataProduct = GetProductDALObject.AllData

    def insertProduct(self):
        insertProductDALObject = ProductDataAccess(self.Product)
        insertProductDALObject.spInsertProduct()

    def updateProduct(self, ProductId):
        updateProductDALObject = ProductDataAccess(self.Product)
        updateProductDALObject.spUpdateProduct(ProductId)


    def deleteProduct(self, ProductId):
        deleteProductDALObject = ProductDataAccess(ProductId)
        deleteProductDALObject.spDeleteProduct()

    def getCategoryList(self):
        productDALObject = ProductDataAccess()
        return productDALObject.spGetCategoryList()

    def getSupplierList(self):
        productDALObject = ProductDataAccess()
        return productDALObject.spGetSupplierList()