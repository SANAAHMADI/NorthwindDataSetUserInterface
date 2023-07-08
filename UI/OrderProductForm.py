import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

from BusinessLogic.OrderDetailesBusinessLogic import OrderDetailesBusinessLogic
from DataAccess.OrderDetailesDataAccess import OrderDetailesDataAccess
from Models.EmployeeModel import EmloyeeIdDelete
from Models.OrderDetailesModel import OrderDetailes
from Models.UserModel import User
from Models.OrderModel import Order, OrderIdDelete
from BusinessLogic.OrderBusinessLogic import OrderBusinessLogic
from DataAccess.OrderDataAccess import OrderDataAccess
from tkcalendar import DateEntry
from datetime import datetime
from Models.ProductModel import *
from BusinessLogic.ProductBusinessLogic import productBusinessLogic


class OrderForm:

    def __init__(self, user: User):
        self.User = user
        self.GetData = []
        self.DeleteID = 0
        self.UpdateID = 0

    def order_FormLoad(self):
        orderForm = Tk()
        orderForm.title('Order Register')
        orderForm.geometry('800x1500')
        orderForm.config(bg="LightBlue")
        # frame = LabelFrame(orderForm, text="Product Fields...", width=1500, height=800, padx=10)
        #
        # sb = Scrollbar(
        #     orderForm,
        #     orient=VERTICAL
        # )
        #
        # frame1 = Frame(
        #     frame,
        #     bg='#A8B9BF'
        # )
        #
        #
        # sb = Scrollbar(
        #     frame,
        #     orient=VERTICAL
        # )
        #
        # sb.grid(row=0, column=1, sticky=NS)
        #
        # frame.config(yscrollcommand=sb.set)
        # sb.config(command=frame.yview)
        #
        # frame.config(yscrollcommand=sb.set)
        # sb.config(command=orderForm.yview)
        # orderForm.mainloop()

        # orderForm.resizable(0, 0)
        positionRight = int(orderForm.winfo_screenwidth() / 2 - 800 / 2)
        positionDown = int(orderForm.winfo_screenheight() / 2 - 1500 / 2)
        orderForm.geometry("+{}+{}".format(positionRight, positionDown))

        employeeBusinessLogic = OrderBusinessLogic()
        employeeBusinessLogic.getOrder()
        self.GetData = employeeBusinessLogic.AllDataOrder

        def destroyForm():
            orderForm.destroy()

        def clearText():
            entFreight.delete(0, END)
            entOrderDate.delete(0, END)
            entShipVia.delete(0, END)
            entShipCity.delete(0, END)
            entCustomerID.delete(0, END)
            entEmployeeID.delete(0, END)
            entRrequiredDate.delete(0, END)
            entShipAddress.delete(0, END)
            entShipCountry.delete(0, END)
            entShipName.delete(0, END)
            entShippedDate.delete(0, END)
            entShipPostalCode.delete(0, END)
            entShipRegion.delete(0, END)
        def clearText():
            entOrderID.delete(0, END)
            entProductID.delete(0, END)
            entUnitPrice.delete(0, END)
            entQuantity.delete(0, END)
            entDiscount.delete(0, END)


        def registerOrderDetails():
            orderDetailsObject = OrderDetailes(
                orderID=entOrderID.get(),
                productID=entProductID.get().split('-')[0],
                unitPrice=entUnitPrice.get().split('-')[0],
                quantity=entQuantity.get(),
                discount=entDiscount.get()
            )
            OrderDetailsBLLObject = OrderDetailesBusinessLogic(orderDetailsObject)
            OrderDetailsBLLObject.insertOrderDetailes()
            showinfo('Success', 'Order Details Registered successfully.')
            for i in tree.get_children():
                tree.delete(i)
            OrderDetailsBusinessLogic = OrderDetailesBusinessLogic()
            OrderDetailsBusinessLogic.insertOrderDetailes()
            self.GetData = OrderDetailsBusinessLogic.AllDataOrderDetailes

            for item in self.GetData:
                tree.insert("", 'end', values=item)
            clearText()

        def updateOrderDetails():
            orderDetailsObject = OrderDetailes(
                orderID=entOrderID.get(),
                productID=entProductID.get().split('-')[0],
                unitPrice=entUnitPrice.get().split('-')[0],
                quantity=entQuantity.get(),
                discount=entDiscount.get()
            )
            OrderDetailsBLLObject = OrderDetailesBusinessLogic(orderDetailsObject)
            OrderDetailsBLLObject.insertOrderDetailes(self.UpdateID)
            showinfo('Success', 'Order Details Updated successfully.')
            for i in tree.get_children():
                tree.delete(i)
            OrderDetailsBusinessLogic = OrderDetailesBusinessLogic()
            OrderDetailsBusinessLogic.updateOrderDetailes()
            self.GetData = OrderDetailsBusinessLogic.AllDataOrderDetailes
            for item in self.GetData:
                tree.insert("", 'end', values=item)

            clearText()

        def deleteOrderDetails():
            orderDetailsObject = ProductIdDelete(
                OrderDetailesID=self.DeleteID)
            OrderDetailsBLLObject = OrderDetailesBusinessLogic(orderDetailsObject)
            OrderDetailsBLLObject.insertOrderDetailes(self.DeleteID)
            showinfo('Success', 'Order Details Deleted successfully.')
            for i in tree.get_children():
                tree.delete(i)
            OrderDetailsBusinessLogic = OrderDetailesBusinessLogic()
            OrderDetailsBusinessLogic.updateOrderDetailes()
            self.GetData = OrderDetailsBusinessLogic.AllDataOrderDetailes
            for item in self.GetData:
                tree.insert("", 'end', values=item)

            clearText()



        def registerOrder():
            orderObject = Order(
                customerID=entCustomerID.get().split('-')[0],
                employeeID=entEmployeeID.get().split('-')[0],
                orderDate=entOrderDate.get(),
                requiredDate=entRrequiredDate.get(),
                shippedDate=entShippedDate.get(),
                shipVia=entShipVia.get().split('-')[0],
                freight=entFreight.get(),
                shipName=entShipName.get(),
                shipAddress=entShipAddress.get(),
                shipCity=entShipCity.get(),
                shipRegion=entShipRegion.get(),
                shipPostalCode=entShipPostalCode.get(),
                shipCountry=entShipCountry.get())
            orderBLLObject = OrderBusinessLogic(orderObject)
            orderBLLObject.insertOrder()
            showinfo('Success', 'Order Registered successfully.')
            for i in tree.get_children():
                tree.delete(i)
            orderBusinessLogic = OrderBusinessLogic()
            orderBusinessLogic.getOrder()
            self.GetData = orderBusinessLogic.AllDataOrder
            clearText()

        def updateOrder():
            orderObject = Order(
                customerID=entCustomerID.get().split('-')[0],
                employeeID=entEmployeeID.get().split('-')[0],
                orderDate=entOrderDate.get(),
                requiredDate=entRrequiredDate.get(),
                shippedDate=entShippedDate.get(),
                shipVia=entShipVia.get().split('-')[0],
                freight=entFreight.get(),
                shipName=entShipName.get(),
                shipAddress=entShipAddress.get(),
                shipCity=entShipCity.get(),
                shipRegion=entShipRegion.get(),
                shipPostalCode=entShipPostalCode.get(),
                shipCountry=entShipCountry.get())
            orderBLLObject = OrderBusinessLogic(orderObject)
            orderBLLObject.updateOrder(self.UpdateID)
            showinfo('Success', 'Order updated successfully.')
            for i in tree.get_children():
                tree.delete(i)
            orderBusinessLogic = OrderBusinessLogic()
            orderBusinessLogic.getOrder()
            self.GetData = orderBusinessLogic.AllDataOrder

        def deleteOrder():
            orderObject = OrderIdDelete(
                orderID=self.DeleteID)
            orderBusinessLogic = OrderBusinessLogic(orderObject)
            orderBusinessLogic.deleteOrder(self.DeleteID)

            showinfo('Success', 'Order deleted successfully.')
            for i in tree.get_children():
                tree.delete(i)
            orderBLLObject = OrderBusinessLogic()
            orderBLLObject.getOrder()
            self.GetData = orderBusinessLogic.AllDataOrder

            for item in self.GetData:
                tree.insert("", 'end', values=item)
            clearText()

        # endregion
        # frame = LabelFrame(orderForm, text="Product Fields...", width=1500, height=800, padx=10)
        # frame1 = LabelFrame(frame, text="Product Fields...", width=750, height=400, padx=10)
        # frameButton1 = LabelFrame(frame, text="Product Opertation ...", width=750, height=200, padx=10)
        # frame1 = LabelFrame(frame, text="Product Data ...", width=750, height=290, padx=10, pady=10)
        # frame2 = LabelFrame(frame, text="Order Fields...", width=750, height=400, padx=10)
        # frameButton2 = LabelFrame(frame, text="Order Opertation ...", width=750, height=200, padx=10)
        # frameGrid2 = LabelFrame(frame, text="Order Data ...", width=750, height=290, padx=10, pady=10)


        frame1 = LabelFrame(orderForm, text="Order Details Fields...", width=750, height=400, padx=10)
        frameButton1 = LabelFrame(orderForm, text="Order Details Opertation ...", width=750, height=200, padx=10)
        frame1 = LabelFrame(orderForm, text="Order Details Data ...", width=750, height=290, padx=10, pady=10)
        frame2 = LabelFrame(orderForm, text="Order Fields...", width=750, height=400, padx=10)
        frameButton2 = LabelFrame(orderForm, text="Order Opertation ...", width=750, height=200, padx=10)
        frameGrid2 = LabelFrame(orderForm, text="Order Data ...", width=750, height=290, padx=10, pady=10)

# order
        frame2.grid(row=0, column=0, padx=10)
        frameButton2.grid(row=2, column=0, padx=10)
        frameGrid2.grid(row=3, column=0, padx=10)

        lblCustomerID = Label(frame2, text='Customer ID: ')
        lblCustomerID.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        txtCustomerID = StringVar()
        customerIDBLLObject = OrderBusinessLogic()
        customers = customerIDBLLObject.getCustomerList()
        entCustomerID = ttk.Combobox(frame2, textvariable=txtCustomerID, values=customers, width=37)
        entCustomerID.grid(row=0, column=1, padx=10, pady=10, sticky='e')


        lblEmployeeID = Label(frame2, text='Employee ID: ')
        lblEmployeeID.grid(row=0, column=2, padx=10, pady=10, sticky='w')

        txtEmployeeID = StringVar()
        employeeIDBLLObject = OrderBusinessLogic()
        employees = employeeIDBLLObject.getEmployeeList()
        entEmployeeID = ttk.Combobox(frame2, textvariable=txtEmployeeID,values=employees, width=37)
        entEmployeeID.grid(row=0, column=3, padx=10, pady=10, sticky='e')

        lblOrderDate =Label(frame2, text='Order Date: ')
        lblOrderDate.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        txtOrderDate= StringVar()
        entOrderDate =DateEntry(frame2, textvariable=txtOrderDate, width=30)
        entOrderDate.grid(row=1, column=1, padx=10, pady=10, sticky='e')

        lblRrequiredDate = Label(frame2, text='Require Date: ')
        lblRrequiredDate.grid(row=1, column=2, padx=10, pady=10, sticky='w')

        txtRrequiredDate = StringVar()
        entRrequiredDate = DateEntry(frame2, textvariable=txtRrequiredDate, width=30)
        entRrequiredDate.grid(row=1, column=3, padx=10, pady=10, sticky='e')

        lblShippedDate = Label(frame2, text='Shipped Date: ')
        lblShippedDate.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        txtShippedDate = StringVar()
        entShippedDate = DateEntry(frame2, textvariable=txtShippedDate, width=30)
        entShippedDate.grid(row=2, column=1, padx=10, pady=10, sticky='e')

        lblShipVia = Label(frame2, text='Ship Via: ')
        lblShipVia.grid(row=2, column=2, padx=10, pady=10, sticky='w')

        txtShipVia = StringVar()
        shipViasIDBLLObject = OrderBusinessLogic()
        shipVias = shipViasIDBLLObject.getShipViaList()
        entShipVia = ttk.Combobox(frame2, textvariable=txtShipVia,values=shipVias, width=37)
        entShipVia.grid(row=2, column=3, padx=10, pady=10, sticky='e')

        lblFreight = Label(frame2, text='Freight ')
        lblFreight.grid(row=3, column=0, padx=10, pady=10, sticky='w')

        txtFreight = StringVar()
        entFreight = ttk.Entry(frame2, textvariable=txtFreight, width=40)
        entFreight.grid(row=3, column=1, padx=10, pady=10, sticky='e')

        lblShipName = Label(frame2, text='Ship Name: ')
        lblShipName.grid(row=3, column=2, padx=10, pady=10, sticky='w')

        txtShipName = StringVar()
        entShipName = ttk.Entry(frame2, textvariable=txtShipName, width=40)
        entShipName.grid(row=3, column=3, padx=10, pady=10, sticky='e')

        lblShipAddress = Label(frame2, text='Ship Address: ')
        lblShipAddress.grid(row=4, column=0, padx=10, pady=10, sticky='w')

        txtShipAddress = StringVar()
        entShipAddress = ttk.Entry(frame2, textvariable=txtShipAddress, width=40)
        entShipAddress.grid(row=4, column=1, padx=10, pady=10, sticky='e')

        lblShipCity = Label(frame2, text='Ship City: ')
        lblShipCity.grid(row=4, column=2, padx=10, pady=10, sticky='w')

        txtShipCity = StringVar()
        entShipCity = ttk.Entry(frame2, textvariable=txtShipCity, width=40)
        entShipCity.grid(row=4, column=3, padx=10, pady=10, sticky='e')

        lblShipRegion = Label(frame2, text='Ship Region: ')
        lblShipRegion.grid(row=5, column=0, padx=10, pady=10, sticky='w')

        txtShipRegion = StringVar()
        entShipRegion = ttk.Entry(frame2, textvariable=txtShipRegion, width=40)
        entShipRegion.grid(row=5, column=1, padx=10, pady=10, sticky='e')

        lblShipPostalCode = Label(frame2, text='Ship Postal Code: ')
        lblShipPostalCode.grid(row=5, column=2, padx=10, pady=10, sticky='w')

        txtShipPostalCode = StringVar()
        entShipPostalCode = ttk.Entry(frame2, textvariable=txtShipPostalCode, width=40)
        entShipPostalCode.grid(row=5, column=3, padx=10, pady=10, sticky='e')

        lblShipCountry = Label(frame2, text='Ship Country: ')
        lblShipCountry.grid(row=6, column=0, padx=10, pady=10, sticky='w')

        txtShipCountry = StringVar()
        entShipCountry = ttk.Entry(frame2, textvariable=txtShipCountry, width=40)
        entShipCountry.grid(row=6, column=1, padx=10, pady=10, sticky='e')




#order
#OrderDetails
        frame1.grid(row=1, column=0, padx=10)
        # frameButton1.grid(row=4, column=0, padx=10)
        frameGrid1.grid(row=1, column=1, padx=10)


        lblOrderID = Label(frame1, text='OrderID: ')
        lblOrderID.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        txtOrderID= StringVar()
        orderDetailesBLLObject = OrderDetailesDataAccess()
        OrderID = orderDetailesBLLObject.spGetOrderList()
        entOrderID = ttk.Combobox(frame1, textvariable=txtOrderID, values=OrderID, width=37)
        entOrderID.grid(row=0, column=1, padx=10, pady=10, sticky='e')

        lblProductID = Label(frame1, text='ProductID: ')
        lblProductID.grid(row=0, column=2, padx=10, pady=10, sticky='w')

        txtProductID = StringVar()
        orderDetailesBLLObject = OrderDetailesDataAccess()
        productID = orderDetailesBLLObject.spGetProductList()
        entProductID = ttk.Combobox(frame1, textvariable=txtProductID,values=productID, width=37)
        entProductID.grid(row=0, column=3, padx=10, pady=10, sticky='e')

        lblQuantity = Label(frame1, text='Quantity: ')
        lblQuantity.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        txtQuantity = StringVar()
        entQuantity = ttk.Entry(frame1, textvariable=txtQuantity, width=40)
        entQuantity.grid(row=1, column=1, padx=10, pady=10, sticky='e')

        lblUnitPrice = Label(frame1, text='Unit Price: ')
        lblUnitPrice.grid(row=1, column=2, padx=10, pady=10, sticky='w')

        txtUnitPrice = StringVar()
        entUnitPrice = ttk.Entry(frame1, textvariable=txtUnitPrice, width=40)
        entUnitPrice.grid(row=1, column=3, padx=10, pady=10, sticky='e')

        lblDiscount = Label(frame1, text='Discount: ')
        lblDiscount.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        txtDiscount = StringVar()
        entDiscount = ttk.Entry(frame1, textvariable=txtDiscount, width=40)
        entDiscount.grid(row=2, column=1, padx=10, pady=10, sticky='e')
#OrderDetails

#OrderDetailsTreeView
        columns = ("orderID"
                   , "productID"
                   , "unitPrice"
                   , "quantity"
                   , "discount"
                   )
        tree = ttk.Treeview(frame1, columns=columns, show='headings')

        tree.heading("orderID", text="orderID", anchor=W)
        tree.heading("productID", text="productID", anchor=W)
        tree.heading("unitPrice", text="unitPrice", anchor=W)
        tree.heading("quantity", text="quantity", anchor=W)
        tree.heading("discount", text="discount", anchor=W)

        for item in self.GetData:
            tree.insert("", 'end', values=item)

        def item_selected(event):
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                record = item['values']

                entOrderID.delete(0, END)
                entOrderID.insert(0, record[1])

                entProductID.delete(0, END)
                entProductID.insert(0, record[2])

                entUnitPrice.delete(0, END)
                entUnitPrice.insert(0, record[3])

                entQuantity.delete(0, END)
                entQuantity.insert(0, record[4])

                entDiscount.delete(0, END)
                entDiscount.insert(0, record[5])

                self.DeleteID = record[0]
                self.UpdateID = record[0]

        tree.bind('<<TreeviewSelect>>', item_selected)

        # tree.grid(row=0, column=0, sticky='nsew')

        treeXScroll = ttk.Scrollbar(frame1, orient=HORIZONTAL)
        treeXScroll.configure(command=tree.xview)
        tree.configure(xscrollcommand=treeXScroll.set)

        frame1.grid(column=1, row=3, sticky=(N, S, E, W))
        tree.grid(column=1, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
        treeXScroll.grid(column=1, row=2, columnspan=3, sticky=W + E)

        orderForm.columnconfigure(0, weight=1)
        orderForm.rowconfigure(0, weight=1)
        frame1.columnconfigure(0, weight=3)
        frame1.columnconfigure(1, weight=3)
        frame1.columnconfigure(2, weight=3)
        frame1.columnconfigure(3, weight=1)
        frame1.columnconfigure(4, weight=1)
        frame1.rowconfigure(1, weight=1)
#ENDOrderDetailsTreeView
#Operation
        btnClearEmployee = ttk.Button(frameButton2, text='Clear', command=clearText, width=16)
        btnClearEmployee.grid(row=7, column=0, padx=10, pady=10, sticky='e')

        btnInsertEmployee = ttk.Button(frameButton2, text='Insert', command=registerOrder, width=16)
        btnInsertEmployee.grid(row=7, column=1, padx=10, pady=10, sticky='e')

        btnUpdateEmployee = ttk.Button(frameButton2, text='Update', command=updateOrder, width=16)
        btnUpdateEmployee.grid(row=7, column=2, padx=10, pady=10, sticky='e')

        btnDeleteEmployee = ttk.Button(frameButton2, text='Delete', command=deleteOrder, width=16)
        btnDeleteEmployee.grid(row=7, column=3, padx=10, pady=10, sticky='e')

        btnBackToMain = ttk.Button(frameButton2, text='Close', command=destroyForm, width=14)
        btnBackToMain.grid(row=7, column=4, padx=10, pady=10, sticky='w')
#Operation
#order
        columns = ("CustomerID",
                   "EmployeeID",
                   "OrderDate",
                   "RequiredDate",
                   "ShippedDate",
                   "ShipVia",
                   "Freight",
                   "ShipName",
                   "ShipAddress",
                   "ShipCity",
                   "ShipRegion",
                   "ShipPostalCode",
                   "ShipCountry"
                   )
        tree = ttk.Treeview(frameGrid2, columns=columns, show='headings')

        tree.heading("CustomerID",  text="EmployeeID", anchor=W)
        tree.heading("EmployeeID",  text="FirstName", anchor=W)
        tree.heading("OrderDate",  text="lastName", anchor=W)
        tree.heading("RequiredDate",  text="title", anchor=W)
        tree.heading("ShippedDate",  text="titleOfCourtesy", anchor=W)
        tree.heading("ShipVia",  text="birthDate", anchor=W)
        tree.heading("Freight",  text="hireDate", anchor=W)
        tree.heading("ShipName",  text="address", anchor=W)
        tree.heading("ShipAddress",  text="city", anchor=W)
        tree.heading("ShipCity",  text="region", anchor=W)
        tree.heading("ShipRegion",  text="postalCode", anchor=W)
        tree.heading("ShipPostalCode", text="postalCode", anchor=W)
        tree.heading("ShipCountry", text="homePhone", anchor=W)


        for item in self.GetData:
            escaped_values = [str(val).replace('"', '""').replace("'", "''") for val in item]
            tree.insert('', tkinter.END, values=escaped_values)

        def item_selected(event):
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                record = item['values']
                entShipName.delete(0, END)
                entShipName.insert(0, record[1])

                entCustomerID.delete(0, END)
                entCustomerID.insert(0, record[2])

                entEmployeeID.delete(0, END)
                entEmployeeID.insert(0, record[3])

                entOrderDate.delete(0, END)
                entOrderDate.insert(0, record[4])

                entRrequiredDate.delete(0, END)
                entRrequiredDate.insert(0, record[5])

                entShippedDate.delete(0, END)
                entShippedDate.insert(0, record[6])

                entShipVia.delete(0, END)
                entShipVia.insert(0, record[7])

                entFreight.delete(0, END)
                entFreight.insert(0, record[8])

                entShipName.delete(0, END)
                entShipName.insert(0, record[9])

                entShipAddress.delete(0, END)
                entShipAddress.insert(0, record[10])

                entShipCity.delete(0, END)
                entShipCity.insert(0, record[11])

                entShipRegion.delete(0, END)
                entShipRegion.insert(0, record[12])

                entShipPostalCode.delete(0, END)
                entShipPostalCode.insert(0, record[13])

                entShipCountry.delete(0, END)
                entShipCountry.insert(0, record[14])

                self.DeleteID = record[0]
                self.UpdateID=record[0]
                # txtFirstName.set(record[2])
                # show a message
                # showinfo(title='Information', message=','.join(record))

        tree.bind('<<TreeviewSelect>>', item_selected)

        # tree.grid(row=0, column=0, sticky='nsew')

        treeXScroll = ttk.Scrollbar(frameGrid2, orient=HORIZONTAL)
        treeXScroll.configure(command=tree.xview)
        tree.configure(xscrollcommand=treeXScroll.set)

        frameGrid2.grid(column=0, row=3, sticky=(N, S, E, W))
        tree.grid(column=0, row=0, columnspan=3, roorderFormpan=2, sticky=(N, S, E, W))
        treeXScroll.grid(column=0, row=2, columnspan=3, sticky=W + E)

        orderForm.columnconfigure(0, weight=1)
        orderForm.rowconfigure(0, weight=1)
        frameGrid2.columnconfigure(0, weight=3)
        frameGrid2.columnconfigure(1, weight=3)
        frameGrid2.columnconfigure(2, weight=3)
        frameGrid2.columnconfigure(3, weight=1)
        frameGrid2.columnconfigure(4, weight=1)
        frameGrid2.rowconfigure(1, weight=1)

        orderForm.mainloop()
#order