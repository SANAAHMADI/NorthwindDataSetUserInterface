from Models.RegisterModel import RegisterUser
from DataAccess.RegisterDataAccess import RegisterUserDataAccess
class RegisterUserBusinessLogic:
    def __init__(self, registerUser: RegisterUser = None):
        self.RegisterUser = registerUser
        self.AllDataEmployee = []

    def insertRegisterUserObject(self):
        insertRegisterUserObjectDALObject = RegisterUserDataAccess(self.RegisterUser)
        insertRegisterUserObjectDALObject.spInsertRegisterUser()
    # def getEmployee(self):
    #     GetEmployeeDALObject = RegisterUserDataAccess()
    #     GetEmployeeDALObject.spGetEmployee()
    #     self.AllDataEmployee = GetEmployeeDALObject.AllData



    # def updateEmployee(self, EmployeeId):
    #     updateEmployeeDALObject = EmployeeDataAccess(self.Employee)
    #     updateEmployeeDALObject.spUpdateEmployee(EmployeeId)
    #
    # def deleteEmployee(self, EmployeeId):
    #     deleteEmployeeDALObject = EmployeeDataAccess(EmployeeId)
    #     deleteEmployeeDALObject.spDeleteEmployee()
