from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from Models.UserModel import User
from Models.EmployeeModel import Employee
from Models.ShipperModel import *
from UI.OrderForm import OrderForm
from UI.ShipperForm import ShipperForm
from UI.EmployeeForm import EmployeeForm
from UI.CustomerForm import customerForm
from UI.OrderForm import OrderForm
from UI.OrderProductForm import OrderForm
from UI.ProductForm import ProductForm
from UI.SupplierForm import SupplierForm
from UI.CategoryForm import CategoryForm
from UI.OrderDetailesForm import OrderDetailsForm


# from UserInterFaceLayer.OrderReportModule import OrderReportClass
# from UserInterFaceLayer.EmployeeRegisterModule import EmployeeRegisterClass
# from UserInterFaceLayer.GetShippers import GetShipperClass
# from UserInterFaceLayer.DeleteOrderModule import DeleteOrderClass
# from UserInterFaceLayer.CustomerRegisterModule import CustomerRegisterClass
# from UserInterFaceLayer.RegisterOrderModule import orderRegisterClass
# from UserInterFaceLayer.EmployeeUpdateModule import EmployeeUpdateClass
# from UserInterFaceLayer.OrderUpdateModule import orderUpdateClass
# from UserInterFaceLayer.EmployeeDeleteModule import DeleteEmployeeClass
# from UserInterFaceLayer.CustomerDeleteModule import DeleteCustomerClass
# from UserInterFaceLayer.CustomerReportModule import GetCustomerClass
# from UserInterFaceLayer.EmployeeReportModule import GetEmployeeClass
# from UserInterFaceLayer.OrderReportModule import GetOrderClass

class MainForm:
    def __init__(self, user: User):
        self.User = user

    def mainFormClass_FormLoad(self):
        mainForm = Tk()
        mainForm.title('Main Form')
        mainForm.geometry('800x150')
        mainForm.config(bg="#C5CAE9")
        mainForm.resizable(0, 0)
        positionRight = int(mainForm.winfo_screenwidth() / 2 - 800 / 2)
        positionDown = int(mainForm.winfo_screenheight() / 2 - 150 / 2)
        mainForm.geometry("+{}+{}".format(positionRight, positionDown))

        # #RegisterForm
        def Employee_FormLoad():
            employeeObject = EmployeeForm(self.User)
            employeeObject.employee_FormLoad()

        def Customer_FormLoad():
            customerObject = customerForm(self.User)
            customerObject.customer_FormLoad()

        def Shipper_FormLoad():
            shipperObject = ShipperForm(self.User)
            shipperObject.shipper_FormLoad()

        # def Order_FormLoad():
        #     orderObject = OrderForm(self.User)
        #     orderObject.order_FormLoad()

        def OrderProduct_FormLoad():
            orderObject = OrderForm(self.User)
            orderObject.order_FormLoad()

        def Product_FormLoad():
            productObject = ProductForm(self.User)
            productObject.product_FormLoad()

        def Supplier_FormLoad():
            supplierObject = SupplierForm(self.User)
            supplierObject.supplier_FormLoad()

        def Category_FormLoad():
            categoryObject = CategoryForm(self.User)
            categoryObject.category_FormLoad()

        def OrderDetails_FormLoad():
            orderDetailsObject = OrderDetailsForm(self.User)
            OrderDetailsForm.orderDetails_FormLoad(self)

        lblMSG = Label(mainForm, text=f'Dear {self.User.UserName} welcome!')
        lblMSG.grid(row=0, column=0, padx=20, pady=20)

        width = 15
        height = 15
        buttonImage = Image.open('./Image/Employee.jpg')
        buttonImage = buttonImage.resize((width, height))
        buttonEmployee = ImageTk.PhotoImage(buttonImage)
        btnRegisterEmployee =ttk.Button(mainForm, compound=LEFT, text='Employee', image=buttonEmployee,
                                     command=Employee_FormLoad, width=20)
        btnRegisterEmployee.grid(row=0, column=0, padx=20, pady=20)

        buttonImage = Image.open('./Image/Customer.png')
        buttonImage = buttonImage.resize((width, height))
        buttonCustomer = ImageTk.PhotoImage(buttonImage)
        btnRegisterCustomer = ttk.Button(mainForm, compound=LEFT, text='Customer', image=buttonCustomer,
                                         command=Customer_FormLoad, width=20)
        btnRegisterCustomer.grid(row=0, column=1, padx=20, pady=20)

        buttonImage = Image.open('./Image/Order.png')
        buttonImage = buttonImage.resize((width, height))
        buttonOrder = ImageTk.PhotoImage(buttonImage)
        btnRegisterOrder =ttk.Button(mainForm, compound=LEFT, text='Order', command=OrderProduct_FormLoad, image=buttonOrder,
                                  width=20)
        btnRegisterOrder.grid(row=0, column=2, padx=20, pady=20)

        buttonImage = Image.open('./Image/Shipper.png')
        buttonImage = buttonImage.resize((width, height))
        buttonShipper = ImageTk.PhotoImage(buttonImage)
        btnRegisterShipper =ttk.Button(mainForm, compound=LEFT, text='Shipper', image=buttonShipper,
                                    command=Shipper_FormLoad, width=20)
        btnRegisterShipper.grid(row=0, column=3, padx=20, pady=20)

        buttonImage = Image.open('./Image/Product.png')
        buttonImage = buttonImage.resize((width, height))
        buttonProduct = ImageTk.PhotoImage(buttonImage)
        btnRegisterShipper =ttk.Button(mainForm, compound=LEFT, text='Product', image=buttonProduct,
                                    command=Product_FormLoad, width=20)
        btnRegisterShipper.grid(row=1, column=0, padx=20, pady=20)

        # SupplierImage = PhotoImage(file='./Image/Supplier.png')
        buttonImage = Image.open('./Image/Supplier.jpg')
        buttonImage = buttonImage.resize((width, height))
        buttonSupplier = ImageTk.PhotoImage(buttonImage)
        btnRegisterShipper =ttk.Button(mainForm, compound=LEFT, image=buttonSupplier, text='Supplier',
                                    command=Supplier_FormLoad, width=20)
        btnRegisterShipper.grid(row=1, column=1, padx=20, pady=20)

        # CategoryImage = PhotoImage(file='./Image/Category1.png')
        buttonImage = Image.open('./Image/Category.png')
        buttonImage = buttonImage.resize((width, height))
        buttonCategory = ImageTk.PhotoImage(buttonImage)
        btnRegisterShipper =ttk.Button(mainForm, compound=LEFT, image=buttonCategory, text='Category',
                                    command=Category_FormLoad, width=20)
        btnRegisterShipper.grid(row=1, column=2, padx=20, pady=20)

        buttonImage = Image.open('./Image/Orderdetails.png')
        buttonImage = buttonImage.resize((width, height))
        buttonOrderdetails = ImageTk.PhotoImage(buttonImage)
        btnRegisterShipper =ttk.Button(mainForm, compound=LEFT, image=buttonOrderdetails, text='Order Details',
                                    command=OrderDetails_FormLoad, width=20)
        btnRegisterShipper.grid(row=1, column=3, padx=20, pady=20)
        mainForm.mainloop()
        # image = EmployeeImage,
        # , image = OrderImage
        # , image = CategoryImage
        # image = SupplierImage,
        # image = ShipperImage,
        # image = ShipperImage,
        # image = OrderImage,
        # image = CustomerImage,
