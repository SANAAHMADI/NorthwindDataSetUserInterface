import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

from Models.OrderDetailesModel import OrderDetailes
from Models.UserModel import User
from Models.ProductModel import *
from BusinessLogic.OrderDetailesBusinessLogic import OrderDetailesBusinessLogic
from DataAccess.OrderDetailesDataAccess import OrderDetailesDataAccess
from tkcalendar import DateEntry
from datetime import datetime





class OrderDetailsForm:

    def __init__(self, user: User):
        self.User = user
        self.GetData = []
        self.DeleteID = 0
        self.UpdateID = 0

    def orderDetails_FormLoad(self):
        orderDetailsForm = Tk()
        orderDetailsForm.title('Order Details Register')
        orderDetailsForm.geometry('800x720')
        orderDetailsForm.config(bg="LightBlue")
        # orderDetailsForm.resizable(0, 0)
        positionRight = int(orderDetailsForm.winfo_screenwidth() / 2 - 800 / 2)
        positionDown = int(orderDetailsForm.winfo_screenheight() / 2 - 720 / 2)
        orderDetailsForm.geometry("+{}+{}".format(positionRight, positionDown))
        orderDetailesBusinessLogic = OrderDetailesBusinessLogic()
        orderDetailesBusinessLogic.getOrderDetailes()
        self.GetData = orderDetailesBusinessLogic.AllDataOrderDetailes

        def destroyForm():
            orderDetailsForm.destroy()

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

        # endregion

        frame = LabelFrame(orderDetailsForm, text="Field...", width=750, height=400, padx=10)
        frameButton = LabelFrame(orderDetailsForm, text="Opertation ...", width=750, height=200, padx=10)
        frameGrid = LabelFrame(orderDetailsForm, text="Data ...", width=750, height=290, padx=10, pady=10)

        frame.grid(row=0, column=0, padx=10)
        frameButton.grid(row=1, column=0, padx=10)
        frameGrid.grid(row=2, column=0, padx=10)

        lblOrderID = Label(frame, text='OrderID: ')
        lblOrderID.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        txtOrderID= StringVar()
        orderDetailesBLLObject = OrderDetailesDataAccess()
        OrderID = orderDetailesBLLObject.spGetOrderList()
        entOrderID = ttk.Combobox(frame, textvariable=txtOrderID, values=OrderID, width=37)
        entOrderID.grid(row=0, column=1, padx=10, pady=10, sticky='e')

        lblProductID = Label(frame, text='ProductID: ')
        lblProductID.grid(row=0, column=2, padx=10, pady=10, sticky='w')

        txtProductID = StringVar()
        orderDetailesBLLObject = OrderDetailesDataAccess()
        productID = orderDetailesBLLObject.spGetProductList()
        entProductID = ttk.Combobox(frame, textvariable=txtProductID,values=productID, width=37)
        entProductID.grid(row=0, column=3, padx=10, pady=10, sticky='e')

        lblQuantity = Label(frame, text='Quantity: ')
        lblQuantity.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        txtQuantity = StringVar()
        entQuantity = ttk.Entry(frame, textvariable=txtQuantity, width=40)
        entQuantity.grid(row=1, column=1, padx=10, pady=10, sticky='e')

        lblUnitPrice = Label(frame, text='Unit Price: ')
        lblUnitPrice.grid(row=1, column=2, padx=10, pady=10, sticky='w')

        txtUnitPrice = StringVar()
        entUnitPrice = ttk.Entry(frame, textvariable=txtUnitPrice, width=40)
        entUnitPrice.grid(row=1, column=3, padx=10, pady=10, sticky='e')

        lblDiscount = Label(frame, text='Discount: ')
        lblDiscount.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        txtDiscount = StringVar()
        entDiscount = ttk.Entry(frame, textvariable=txtDiscount, width=40)
        entDiscount.grid(row=2, column=1, padx=10, pady=10, sticky='e')



        btnClearProduct = ttk.Button(frameButton, text='Clear', command=clearText, width=16)
        btnClearProduct.grid(row=8, column=0, padx=10, pady=10, sticky='e')

        btnInsertProduct = ttk.Button(frameButton, text='Insert', command=registerOrderDetails, width=16)
        btnInsertProduct.grid(row=8, column=1, padx=10, pady=10, sticky='e')

        btnUpdateProduct = ttk.Button(frameButton, text='Update', command=updateOrderDetails, width=16)
        btnUpdateProduct.grid(row=8, column=2, padx=10, pady=10, sticky='e')

        btnDeleteProduct = ttk.Button(frameButton, text='Delete', command=deleteOrderDetails, width=16)
        btnDeleteProduct.grid(row=8, column=3, padx=10, pady=10, sticky='e')

        btnBackToMain = ttk.Button(frameButton, text='Close', command=destroyForm, width=14)
        btnBackToMain.grid(row=8, column=4, padx=10, pady=10, sticky='w')

        columns = ("orderID"
                    ,"productID"
                    ,"unitPrice"
                    ,"quantity"
                    ,"discount"
                   )
        tree = ttk.Treeview(frameGrid, columns=columns, show='headings')

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

        treeXScroll = ttk.Scrollbar(frameGrid, orient=HORIZONTAL)
        treeXScroll.configure(command=tree.xview)
        tree.configure(xscrollcommand=treeXScroll.set)

        frameGrid.grid(column=0, row=3, sticky=(N, S, E, W))
        tree.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
        treeXScroll.grid(column=0, row=2, columnspan=3, sticky=W + E)

        orderDetailsForm.columnconfigure(0, weight=1)
        orderDetailsForm.rowconfigure(0, weight=1)
        frameGrid.columnconfigure(0, weight=3)
        frameGrid.columnconfigure(1, weight=3)
        frameGrid.columnconfigure(2, weight=3)
        frameGrid.columnconfigure(3, weight=1)
        frameGrid.columnconfigure(4, weight=1)
        frameGrid.rowconfigure(1, weight=1)

        orderDetailsForm.mainloop()
