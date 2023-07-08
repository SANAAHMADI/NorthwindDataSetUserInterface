import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from Models.UserModel import User
from Models.ProductModel import *
from BusinessLogic.ProductBusinessLogic import productBusinessLogic
from DataAccess.ProductDataAccess import ProductDataAccess
from tkcalendar import DateEntry
from datetime import datetime


class ProductForm:

    def __init__(self, user: User):
        self.User = user
        self.GetData = []
        self.DeleteID = 0
        self.UpdateID = 0

    def product_FormLoad(self):
        productForm = Tk()
        productForm.title('Product Register')
        productForm.geometry('800x720')
        productForm.config(bg="LightBlue")
        # productForm.resizable(0, 0)
        positionRight = int(productForm.winfo_screenwidth() / 2 - 800 / 2)
        positionDown = int(productForm.winfo_screenheight() / 2 - 720 / 2)
        productForm.geometry("+{}+{}".format(positionRight, positionDown))
        ProductBusinessLogic = productBusinessLogic()
        ProductBusinessLogic.getProduct()
        self.GetData = ProductBusinessLogic.AllDataProduct

        def destroyForm():
            productForm.destroy()

        def clearText():

            # entProductID.delete(0, END)
            entProductName.delete(0, END)
            entSupplierID.delete(0, END)
            entCategoryID.delete(0, END)
            entQuantityPerUnit.delete(0, END)
            entUnitPrice.delete(0, END)
            entUnitsInStock.delete(0, END)
            entUnitsOnOrder.delete(0, END)
            entReorderLevel.delete(0, END)
            entDiscontinued.delete(0, END)

        def registerProduct():
            productName = entProductName.get(),
            quantityPerUnit = entQuantityPerUnit.get(),
            unitPrice = entUnitPrice.get(),
            unitsInStock = entUnitsInStock.get(),
            unitsOnOrder = entUnitsOnOrder.get(),
            reorderLevel = entReorderLevel.get(),
            discontinued = entDiscontinued.get()
            if len(productName) > 15 or not productName.isalpha():
                showinfo('Error', 'product Name cannot exceed 40 characters and can only contain letters.')
                return False
            if len(quantityPerUnit) > 24 or not quantityPerUnit.isalnum():
                showinfo('Error', 'quantityPerUnit cannot exceed 20 characters can only contain numbers.')
                return False
            if not unitPrice.isalnum():
                showinfo('Error', 'unitPrice can only contain numbers.')
                return False
            if not unitsInStock.isalnum():
                showinfo('Error', 'unitsInStock can only contain numbers.')
                return False
            if not unitsOnOrder.isalnum():
                showinfo('Error', 'unitsOnOrder can only contain numbers.')
                return False
            if not reorderLevel.isalnum():
                showinfo('Error', 'reorderLevel can only contain numbers.')
                return False
            if not discontinued=='0' or discontinued=='1':
                showinfo('Error', 'discontinued can only contain 0 or 1.')
                return False
            else:
                productObject = Product(
                    productName=entProductName.get(),
                    supplierID=entSupplierID.get().split('-')[0],
                    categoryID=entCategoryID.get().split('-')[0],
                    quantityPerUnit=entQuantityPerUnit.get(),
                    unitPrice=entUnitPrice.get(),
                    unitsInStock=entUnitsInStock.get(),
                    unitsOnOrder=entUnitsOnOrder.get(),
                    reorderLevel=entReorderLevel.get(),
                    discontinued=entDiscontinued.get()
                )
                ProductBLLObject = productBusinessLogic(productObject)
                ProductBLLObject.insertProduct()
                showinfo('Success', 'Product Registered successfully.')
                for i in tree.get_children():
                    tree.delete(i)
                ProductBusinessLogic = productBusinessLogic()
                ProductBusinessLogic.getProduct()
                self.GetData = ProductBusinessLogic.AllDataProduct

                for item in self.GetData:
                    tree.insert("", 'end', values=item)
                clearText()

        def updateProduct():
            productName = entProductName.get(),
            quantityPerUnit = entQuantityPerUnit.get(),
            unitPrice = entUnitPrice.get(),
            unitsInStock = entUnitsInStock.get(),
            unitsOnOrder = entUnitsOnOrder.get(),
            reorderLevel = entReorderLevel.get(),
            discontinued = entDiscontinued.get()
            if len(productName) > 15 or not productName.isalpha():
                showinfo('Error', 'product Name cannot exceed 40 characters and can only contain letters.')
                return False
            if len(quantityPerUnit) > 24 or not quantityPerUnit.isalnum():
                showinfo('Error', 'quantityPerUnit cannot exceed 20 characters can only contain numbers.')
                return False
            if not unitPrice.isalnum():
                showinfo('Error', 'unitPrice can only contain numbers.')
                return False
            if not unitsInStock.isalnum():
                showinfo('Error', 'unitsInStock can only contain numbers.')
                return False
            if not unitsOnOrder.isalnum():
                showinfo('Error', 'unitsOnOrder can only contain numbers.')
                return False
            if not reorderLevel.isalnum():
                showinfo('Error', 'reorderLevel can only contain numbers.')
                return False
            if not discontinued == '0' or discontinued == '1':
                showinfo('Error', 'discontinued can only contain 0 or 1.')
                return False
            else:
                productObject = Product(
                    # productID=self.UpdateID,
                    productName=entProductName.get(),
                    supplierID=entSupplierID.get().split('-')[0],
                    categoryID=entCategoryID.get().split('-')[0],
                    quantityPerUnit=entQuantityPerUnit.get(),
                    unitPrice=entUnitPrice.get(),
                    unitsInStock=entUnitsInStock.get(),
                    unitsOnOrder=entUnitsOnOrder.get(),
                    reorderLevel=entReorderLevel.get(),
                    discontinued=entDiscontinued.get())
                ProductBusinessLogic = productBusinessLogic(productObject)
                ProductBusinessLogic.updateProduct(self.UpdateID)

                showinfo('Success', 'Product updated successfully.')
                for i in tree.get_children():
                    tree.delete(i)
                ProductBusinessLogic = productBusinessLogic()
                ProductBusinessLogic.getProduct()
                self.GetData = ProductBusinessLogic.AllDataProduct
                for item in self.GetData:
                    tree.insert("", 'end', values=item)

                clearText()

        def deleteProduct():
            productObject = ProductIdDelete(
                productID=self.DeleteID)
            ProductBusinessLogic = productBusinessLogic(productObject)
            ProductBusinessLogic.deleteProduct(self.DeleteID)
            showinfo('Success', 'Product deleted successfully.')
            for i in tree.get_children():
                tree.delete(i)
            ProductBusinessLogic = productBusinessLogic()
            ProductBusinessLogic.getProduct()
            self.GetData = ProductBusinessLogic.AllDataProduct

            for item in self.GetData:
                tree.insert("", 'end', values=item)
            clearText()

        # endregion

        frame = LabelFrame(productForm, text="Field...", width=750, height=400, padx=10)
        frameButton = LabelFrame(productForm, text="Opertation ...", width=750, height=200, padx=10)
        frameGrid = LabelFrame(productForm, text="Data ...", width=750, height=290, padx=10, pady=10)

        frame.grid(row=0, column=0, padx=10)
        frameButton.grid(row=1, column=0, padx=10)
        frameGrid.grid(row=2, column=0, padx=10)

        lblProductName = Label(frame, text='Product Name: ')
        lblProductName.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        txtProductName = StringVar()
        entProductName = ttk.Entry(frame, textvariable=txtProductName, width=40)
        entProductName.grid(row=0, column=1, padx=10, pady=10, sticky='e')

        lblSupplierID = Label(frame, text='SupplierID: ')
        lblSupplierID.grid(row=0, column=2, padx=10, pady=10, sticky='w')

        txtSupplierID = StringVar()
        supplierBLLObject = productBusinessLogic()
        suppliers = supplierBLLObject.getSupplierList()
        entSupplierID = ttk.Combobox(frame, textvariable=txtSupplierID,values=suppliers, width=37)
        entSupplierID.grid(row=0, column=3, padx=10, pady=10, sticky='e')

        lblCategoryID = Label(frame, text='CategoryID: ')
        lblCategoryID.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        txtCategoryID = StringVar()
        categoryBLLObject = productBusinessLogic()
        categories = categoryBLLObject.getCategoryList()
        entCategoryID = ttk.Combobox(frame, textvariable=txtCategoryID, values=categories, width=37)
        entCategoryID.grid(row=1, column=1, padx=10, pady=10, sticky='e')

        lblQuantityPerUnit = Label(frame, text='Quantity Per Unit: ')
        lblQuantityPerUnit.grid(row=1, column=2, padx=10, pady=10, sticky='w')

        txtQuantityPerUnit = StringVar()
        entQuantityPerUnit = ttk.Entry(frame, textvariable=txtQuantityPerUnit, width=40)
        entQuantityPerUnit.grid(row=1, column=3, padx=10, pady=10, sticky='e')

        lblUnitPrice = Label(frame, text='UnitPrice: ')
        lblUnitPrice.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        txtUnitPrice = StringVar()
        entUnitPrice = ttk.Entry(frame, textvariable=txtUnitPrice, width=40)
        entUnitPrice.grid(row=2, column=1, padx=10, pady=10, sticky='e')

        lblUnitsInStock = Label(frame, text='Units In Stock: ')
        lblUnitsInStock.grid(row=2, column=2, padx=10, pady=10, sticky='w')

        txtUnitsInStock = StringVar()
        entUnitsInStock = ttk.Entry(frame, textvariable=txtUnitsInStock, width=40)
        entUnitsInStock.grid(row=2, column=3, padx=10, pady=10, sticky='e')

        lblUnitsOnOrder = Label(frame, text='Units On Order: ')
        lblUnitsOnOrder.grid(row=3, column=0, padx=10, pady=10, sticky='w')

        txtUnitsOnOrder = StringVar()
        entUnitsOnOrder = ttk.Entry(frame, textvariable=txtUnitsOnOrder, width=40)
        entUnitsOnOrder.grid(row=3, column=1, padx=10, pady=10, sticky='e')

        lblReorderLevel = Label(frame, text='Reorder Level: ')
        lblReorderLevel.grid(row=3, column=0, padx=10, pady=10, sticky='w')

        txtReorderLevel = StringVar()
        entReorderLevel = ttk.Entry(frame, textvariable=txtReorderLevel, width=40)
        entReorderLevel.grid(row=3, column=1, padx=10, pady=10, sticky='e')

        lblDiscontinued = Label(frame, text='Discontinued: ')
        lblDiscontinued.grid(row=3, column=0, padx=10, pady=10, sticky='w')

        txtDiscontinued = StringVar()
        entDiscontinued = ttk.Entry(frame, textvariable=txtDiscontinued, width=40)
        entDiscontinued.grid(row=3, column=1, padx=10, pady=10, sticky='e')

        btnClearProduct = ttk.Button(frameButton, text='Clear', command=clearText, width=16)
        btnClearProduct.grid(row=8, column=0, padx=10, pady=10, sticky='e')

        btnInsertProduct = ttk.Button(frameButton, text='Insert', command=registerProduct, width=16)
        btnInsertProduct.grid(row=8, column=1, padx=10, pady=10, sticky='e')

        btnUpdateProduct = ttk.Button(frameButton, text='Update', command=updateProduct, width=16)
        btnUpdateProduct.grid(row=8, column=2, padx=10, pady=10, sticky='e')

        btnDeleteProduct = ttk.Button(frameButton, text='Delete', command=deleteProduct, width=16)
        btnDeleteProduct.grid(row=8, column=3, padx=10, pady=10, sticky='e')

        btnBackToMain = ttk.Button(frameButton, text='Close', command=destroyForm, width=14)
        btnBackToMain.grid(row=8, column=4, padx=10, pady=10, sticky='w')

        columns = ("productID"
                   , "productName"
                   , "supplierID"
                   , "categoryID"
                   , "quantityPerUnit"
                   , "unitPrice"
                   , "unitsInStock"
                   , "unitsOnOrder"
                   , "reorderLevel"
                   , "discontinued"
                   )
        tree = ttk.Treeview(frameGrid, columns=columns, show='headings')

        tree.heading("productID", text="ProductID", anchor=W)
        tree.heading("productName", text="ProductName", anchor=W)
        tree.heading("supplierID", text="SupplierID", anchor=W)
        tree.heading("categoryID", text="CategoryID", anchor=W)
        tree.heading("quantityPerUnit", text="QuantityPerUnit", anchor=W)
        tree.heading("unitPrice", text="UnitPrice", anchor=W)
        tree.heading("unitsInStock", text="UnitsInStock", anchor=W)
        tree.heading("unitsOnOrder", text="UnitsOnOrder", anchor=W)
        tree.heading("reorderLevel", text="ReorderLevel", anchor=W)
        tree.heading("discontinued", text="Discontinued", anchor=W)

        for item in self.GetData:
            tree.insert("", 'end', values=item)

        def item_selected(event):
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                record = item['values']

                entProductName.delete(0, END)
                entProductName.insert(0, record[1])

                entSupplierID.delete(0, END)
                entSupplierID.insert(0, record[2])

                entCategoryID.delete(0, END)
                entCategoryID.insert(0, record[3])

                entQuantityPerUnit.delete(0, END)
                entQuantityPerUnit.insert(0, record[4])

                entUnitPrice.delete(0, END)
                entUnitPrice.insert(0, record[5])

                entUnitsInStock.delete(0, END)
                entUnitsInStock.insert(0, record[6])

                entUnitsOnOrder.delete(0, END)
                entUnitsOnOrder.insert(0, record[7])

                entReorderLevel.delete(0, END)
                entReorderLevel.insert(0, record[8])

                entDiscontinued.delete(0, END)
                entDiscontinued.insert(0, record[9])

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

        productForm.columnconfigure(0, weight=1)
        productForm.rowconfigure(0, weight=1)
        frameGrid.columnconfigure(0, weight=3)
        frameGrid.columnconfigure(1, weight=3)
        frameGrid.columnconfigure(2, weight=3)
        frameGrid.columnconfigure(3, weight=1)
        frameGrid.columnconfigure(4, weight=1)
        frameGrid.rowconfigure(1, weight=1)

        productForm.mainloop()
