from Models.CategoryModel import Category
from DataAccess.CategoryDataAccess import CategoryDataAccess

class CategoryBusinessLogic:
    def __init__(self, category: Category = None):
        self.Category = category
        self.AllDataCategory = []

    def getCategory(self):
        GetCategoryDALObject = CategoryDataAccess()
        GetCategoryDALObject.spGetCategory()
        self.AllDataCategory = GetCategoryDALObject.AllData

    def insertCategory(self):
        insertCategoryDALObject = CategoryDataAccess(self.Category)
        insertCategoryDALObject.spInsertCategory()

    def updateCategory(self, CategoryId):
        updateCategoryDALObject = CategoryDataAccess(self.Category)
        updateCategoryDALObject.spUpdateCategory(CategoryId)


    def deleteCategory(self, CategoryId):
        deleteCategoryDALObject = CategoryDataAccess(CategoryId)
        deleteCategoryDALObject.spDeleteCategory()

    def getCategoryList(self):
        CategoryDALObject = CategoryDataAccess()
        return CategoryDALObject.spGetCategoryList()

    def getSupplierList(self):
        CategoryDALObject = CategoryDataAccess()
        return CategoryDALObject.spGetSupplierList()