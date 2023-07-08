import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from Models.EmployeeModel import EmloyeeIdDelete
from Models.UserModel import User
from Models.OrderModel import Order, OrderIdDelete
from BusinessLogic.OrderBusinessLogic import OrderBusinessLogic
from DataAccess.OrderDataAccess import OrderDataAccess
from tkcalendar import DateEntry
from datetime import datetime


class OrderForm:

    def __init__(self, user: User):
        self.User = user
        self.GetData = []
        self.DeleteID = 0
        self.UpdateID = 0

    def order_FormLoad(self):
        orderForm = Tk()
        orderForm.title('Order Register')
        orderForm.geometry('800x750')
        orderForm.resizable(0, 0)
        orderForm.config(bg="LightBlue")
        positionRight = int(orderForm.winfo_screenwidth() / 2 - 800 / 2)
        positionDown = int(orderForm.winfo_screenheight() / 2 - 750 / 2)
        orderForm.geometry("+{}+{}".format(positionRight, positionDown))

        orderBusinessLogic = OrderBusinessLogic()
        orderBusinessLogic.getOrder()
        self.GetData = orderBusinessLogic.AllDataOrder
        def destroyForm():
            orderForm.destroy()

        def clearText():
            entFreight.delete(0, END)
            entOrderDate.delete(0, END)
            entShipVia.delete(0, END)
            entShipCity.delete(0, END)
            entCustomerID.delete(0, END)
            entEmployeeID.delete(0, END)
            entRequiredDate.delete(0, END)
            entShipAddress.delete(0, END)
            entShipCountry.delete(0, END)
            entShipName.delete(0, END)
            entShippedDate.delete(0, END)
            entShipPostalCode.delete(0, END)
            entShipRegion.delete(0, END)


        def registerOrder():
            orderObject = Order(
                customerID=entCustomerID.get().split('-')[0],
                employeeID=entEmployeeID.get().split('-')[0],
                orderDate=entOrderDate.get(),
                requiredDate=entRequiredDate.get(),
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
                requiredDate=entRequiredDate.get(),
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
            orderBLLObject = OrderBusinessLogic(orderObject)
            orderBLLObject.deleteOrder(self.DeleteID)
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

        frame = LabelFrame(orderForm, text="Field...", width=750, height=400, padx=10)
        frameButton = LabelFrame(orderForm, text="Opertation ...", width=750, height=200, padx=10)
        frameGrid = LabelFrame(orderForm, text="Data ...", width=750, height=290, padx=10, pady=10)

        frame.grid(row=0, column=0, padx=10)
        frameButton.grid(row=1, column=0, padx=10)
        frameGrid.grid(row=2, column=0, padx=10)

        lblCustomerID = Label(frame, text='Customer ID: ')
        lblCustomerID.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        txtCustomerID = StringVar()
        customerIDBLLObject = OrderBusinessLogic()
        customers = customerIDBLLObject.getCustomerList()
        entCustomerID = ttk.Combobox(frame, textvariable=txtCustomerID, values=customers, width=37)
        entCustomerID.grid(row=0, column=1, padx=10, pady=10, sticky='e')


        lblEmployeeID = Label(frame, text='Employee ID: ')
        lblEmployeeID.grid(row=0, column=2, padx=10, pady=10, sticky='w')

        txtEmployeeID = StringVar()
        employeeIDBLLObject = OrderBusinessLogic()
        employees = employeeIDBLLObject.getEmployeeList()
        entEmployeeID = ttk.Combobox(frame, textvariable=txtEmployeeID,values=employees, width=37)
        entEmployeeID.grid(row=0, column=3, padx=10, pady=10, sticky='e')

        lblOrderDate =Label(frame, text='Order Date: ')
        lblOrderDate.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        txtOrderDate= StringVar()
        entOrderDate =DateEntry(frame, textvariable=txtOrderDate, width=30)
        entOrderDate.grid(row=1, column=1, padx=10, pady=10, sticky='e')

        lblRrequiredDate = Label(frame, text='Require Date: ')
        lblRrequiredDate.grid(row=1, column=2, padx=10, pady=10, sticky='w')

        txtRrequiredDate = StringVar()
        entRequiredDate = DateEntry(frame, textvariable=txtRrequiredDate, width=30)
        entRequiredDate.grid(row=1, column=3, padx=10, pady=10, sticky='e')

        lblShippedDate = Label(frame, text='Shipped Date: ')
        lblShippedDate.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        txtShippedDate = StringVar()
        entShippedDate = DateEntry(frame, textvariable=txtShippedDate, width=30)
        entShippedDate.grid(row=2, column=1, padx=10, pady=10, sticky='e')

        lblShipVia = Label(frame, text='Ship Via: ')
        lblShipVia.grid(row=2, column=2, padx=10, pady=10, sticky='w')

        txtShipVia = StringVar()
        shipViasIDBLLObject = OrderBusinessLogic()
        shipVias = shipViasIDBLLObject.getShipViaList()
        entShipVia = ttk.Combobox(frame, textvariable=txtShipVia,values=shipVias, width=37)
        entShipVia.grid(row=2, column=3, padx=10, pady=10, sticky='e')

        lblFreight = Label(frame, text='Freight ')
        lblFreight.grid(row=3, column=0, padx=10, pady=10, sticky='w')

        txtFreight = StringVar()
        entFreight = ttk.Entry(frame, textvariable=txtFreight, width=40)
        entFreight.grid(row=3, column=1, padx=10, pady=10, sticky='e')

        lblShipName = Label(frame, text='Ship Name: ')
        lblShipName.grid(row=3, column=2, padx=10, pady=10, sticky='w')

        txtShipName = StringVar()
        entShipName = ttk.Entry(frame, textvariable=txtShipName, width=40)
        entShipName.grid(row=3, column=3, padx=10, pady=10, sticky='e')

        lblShipAddress = Label(frame, text='Ship Address: ')
        lblShipAddress.grid(row=4, column=0, padx=10, pady=10, sticky='w')

        txtShipAddress = StringVar()
        entShipAddress = ttk.Entry(frame, textvariable=txtShipAddress, width=40)
        entShipAddress.grid(row=4, column=1, padx=10, pady=10, sticky='e')

        lblShipCity = Label(frame, text='Ship City: ')
        lblShipCity.grid(row=4, column=2, padx=10, pady=10, sticky='w')

        txtShipCity = StringVar()
        entShipCity = ttk.Entry(frame, textvariable=txtShipCity, width=40)
        entShipCity.grid(row=4, column=3, padx=10, pady=10, sticky='e')

        lblShipRegion = Label(frame, text='Ship Region: ')
        lblShipRegion.grid(row=5, column=0, padx=10, pady=10, sticky='w')

        txtShipRegion = StringVar()
        entShipRegion = ttk.Entry(frame, textvariable=txtShipRegion, width=40)
        entShipRegion.grid(row=5, column=1, padx=10, pady=10, sticky='e')

        lblShipPostalCode = Label(frame, text='Ship Postal Code: ')
        lblShipPostalCode.grid(row=5, column=2, padx=10, pady=10, sticky='w')

        txtShipPostalCode = StringVar()
        entShipPostalCode = ttk.Entry(frame, textvariable=txtShipPostalCode, width=40)
        entShipPostalCode.grid(row=5, column=3, padx=10, pady=10, sticky='e')

        lblShipCountry = Label(frame, text='Ship Country: ')
        lblShipCountry.grid(row=6, column=0, padx=10, pady=10, sticky='w')

        txtShipCountry = StringVar()
        entShipCountry = ttk.Entry(frame, textvariable=txtShipCountry, width=40)
        entShipCountry.grid(row=6, column=1, padx=10, pady=10, sticky='e')



        btnClearEmployee = ttk.Button(frameButton, text='Clear', command=clearText, width=16)
        btnClearEmployee.grid(row=7, column=0, padx=10, pady=10, sticky='e')

        btnInsertEmployee = ttk.Button(frameButton, text='Insert', command=registerOrder, width=16)
        btnInsertEmployee.grid(row=7, column=1, padx=10, pady=10, sticky='e')

        btnUpdateEmployee = ttk.Button(frameButton, text='Update', command=updateOrder, width=16)
        btnUpdateEmployee.grid(row=7, column=2, padx=10, pady=10, sticky='e')

        btnDeleteEmployee = ttk.Button(frameButton, text='Delete', command=deleteOrder, width=16)
        btnDeleteEmployee.grid(row=7, column=3, padx=10, pady=10, sticky='e')

        btnBackToMain = ttk.Button(frameButton, text='Close', command=destroyForm, width=14)
        btnBackToMain.grid(row=7, column=4, padx=10, pady=10, sticky='w')

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
        tree = ttk.Treeview(frameGrid, columns=columns, show='headings')

        tree.heading("CustomerID", text="Customer ID", anchor=W)
        tree.heading("EmployeeID", text="Employee ID", anchor=W)
        tree.heading("OrderDate", text="Order Date", anchor=W)
        tree.heading("RequiredDate", text="Required Date", anchor=W)
        tree.heading("ShippedDate", text="Shipped Date", anchor=W)
        tree.heading("ShipVia", text="Ship Via", anchor=W)
        tree.heading("Freight", text="Freight", anchor=W)
        tree.heading("ShipName", text="Ship Name", anchor=W)
        tree.heading("ShipAddress", text="Ship Address", anchor=W)
        tree.heading("ShipCity", text="Ship City", anchor=W)
        tree.heading("ShipRegion", text="Ship Region", anchor=W)
        tree.heading("ShipPostalCode", text="Ship Postal Code", anchor=W)
        tree.heading("ShipCountry", text="Ship Country", anchor=W)

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

                entRequiredDate.delete(0, END)
                entRequiredDate.insert(0, record[5])

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

        treeXScroll = ttk.Scrollbar(frameGrid, orient=HORIZONTAL)
        treeXScroll.configure(command=tree.xview)
        tree.configure(xscrollcommand=treeXScroll.set)

        frameGrid.grid(column=0, row=3, sticky=(N, S, E, W))
        tree.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
        treeXScroll.grid(column=0, row=2, columnspan=3, sticky=W + E)

        orderForm.columnconfigure(0, weight=1)
        orderForm.rowconfigure(0, weight=1)
        frameGrid.columnconfigure(0, weight=3)
        frameGrid.columnconfigure(1, weight=3)
        frameGrid.columnconfigure(2, weight=3)
        frameGrid.columnconfigure(3, weight=1)
        frameGrid.columnconfigure(4, weight=1)
        frameGrid.rowconfigure(1, weight=1)

        orderForm.mainloop()
