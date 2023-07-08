from Models.EmployeeModel import Employee
from DataAccess.EmployeeDataAccess import EmployeeDataAccess

class EmployeeBusinessLogic:
    def __init__(self, employee: Employee = None):
        self.Employee = employee
        self.AllDataEmployee = []

    def getEmployee(self):
        GetEmployeeDALObject = EmployeeDataAccess()
        GetEmployeeDALObject.spGetEmployee()
        self.AllDataEmployee = GetEmployeeDALObject.AllData

    def insertEmployee(self):
        insertEmployeeDALObject = EmployeeDataAccess(self.Employee)
        insertEmployeeDALObject.spInsertEmployee()

    def updateEmployee(self, EmployeeId):
        updateEmployeeDALObject = EmployeeDataAccess(self.Employee)
        updateEmployeeDALObject.spUpdateEmployee(EmployeeId)

    def deleteEmployee(self, EmployeeId):
        deleteEmployeeDALObject = EmployeeDataAccess(EmployeeId)
        deleteEmployeeDALObject.spDeleteEmployee()
