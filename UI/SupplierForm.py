import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from Models.UserModel import User
from Models.SupplierModel import *
from BusinessLogic.SupplierBusinessLogic import SupplierBusinessLogic
from DataAccess.SupplierDataAccess import SupplierDataAccess
from tkcalendar import DateEntry
from datetime import datetime


class SupplierForm:

    def __init__(self, user: User):
        self.User = user
        self.GetData = []
        self.DeleteID = 0
        self.UpdateID = 0
        self.tree = None  # Initialize tree as None

    def supplier_FormLoad(self):
        supplierForm = Tk()
        supplierForm.title('Supplier Register')
        supplierForm.geometry('800x650')
        supplierForm.config(bg="LightBlue")
        positionRight = int(supplierForm.winfo_screenwidth() / 2 - 800 / 2)
        positionDown = int(supplierForm.winfo_screenheight() / 2 - 650 / 2)
        supplierForm.geometry("+{}+{}".format(positionRight, positionDown))
        supplierBusinessLogic = SupplierBusinessLogic()
        supplierBusinessLogic.getSupplier()
        self.GetData = supplierBusinessLogic.AllDataSupplier

        def destroyForm():
            supplierForm.destroy()

        def clearText():
            entCompanyName.delete(0, END)
            entContactName.delete(0, END)
            entContactTitle.delete(0, END)
            entAddress.delete(0, END)
            entCity.delete(0, END)
            entRegion.delete(0, END)
            entPostalCode.delete(0, END)
            entCountry.delete(0, END)
            entPhone.delete(0, END)
            entFax.delete(0, END)
            entHomePage.delete(0, END)

        # CompanyName
        # ContactName
        # ContactTitle
        # Address
        # City
        # Region
        # PostalCode
        # Country
        # Phone
        # Fax
        # HomePage

        def registerSupplier():
            companyName = entCompanyName.get(),
            contactName = entCompanyName.get(),
            contactTitle = entContactTitle.get(),
            address = entAddress.get(),
            city = entCity.get(),
            region = entRegion.get(),
            postalCode = entPostalCode.get(),
            country = entCountry.get(),
            phone = entPhone.get(),
            fax = entFax.get()
            if len(companyName) > 40 or not companyName.isalpha():
                showinfo('Error', 'Category name cannot exceed 40 characters and can only contain letters.')
                return False
            if len(contactName) > 30 or not contactName.isalpha():
                showinfo('Error', 'Contact name cannot exceed 30 characters and can only contain letters.')
                return False
            if len(contactTitle) > 30:
                showinfo('Error', 'Contact name cannot exceed 30 characters.')
                return False
            if len(address) > 60:
                showinfo('Error', 'Address cannot exceed 60 characters.')
                return False
            if len(city) > 15:
                showinfo('Error', 'City cannot exceed 15 characters.')
                return False
            if len(region) > 15:
                showinfo('Error', 'Region cannot exceed 15 characters.')
                return False
            if len(postalCode) > 10 or not postalCode.isalnum():
                showinfo('Error', 'Postal Code cannot exceed 10 characters and can only contain numbers.')
                return False
            if len(country) > 15:
                showinfo('Error', 'Country cannot exceed 15.')
                return False
            if len(phone) > 24 or not phone.isalnum():
                showinfo('Error', 'Phone cannot exceed 24 characters can only contain numbers.')
                return False
            if len(fax) > 24 or not fax.isalnum():
                showinfo('Error', 'Fax cannot exceed 24 characters and can only contain numbers.')
                return False
            else:
                supplierObject = Supplier(
                    companyName=entCompanyName.get(),
                    contactName=entCompanyName.get(),
                    contactTitle=entContactTitle.get(),
                    address=entAddress.get(),
                    city=entCity.get(),
                    region=entRegion.get(),
                    postalCode=entPostalCode.get(),
                    country=entCountry.get(),
                    phone=entPhone.get(),
                    fax=entFax.get(),
                    homePage=entHomePage.get())
                supplierBLLObject = SupplierBusinessLogic(supplierObject)
                supplierBLLObject.insertSupplier()
                showinfo('Success', 'Supplier Registered successfully.')
                for i in tree.get_children():
                    tree.delete(i)
                supplierBusinessLogic = SupplierBusinessLogic()
                supplierBusinessLogic.getSupplier()
                self.GetData = supplierBusinessLogic.AllDataSupplier

            for item in self.GetData:
                tree.insert("", 'end', values=item)
            clearText()

        def updateSupplier():
            companyName = entCompanyName.get()
            phone = entPhone.get()
            if len(companyName) > 15 or not companyName.isalpha():
                showinfo('Error', 'Category name cannot exceed 15 characters and can only contain letters.')
            if len(phone) > 24 or not phone.isalnum():
                showinfo('Error', 'Phone cannot exceed 24 characters can only contain numbers.')
            else:
                supplierObject = Supplier(
                # SupplierId=self.UpdateID,
                companyName=entCompanyName.get(),
                contactName=entCompanyName.get(),
                contactTitle=entContactTitle.get(),
                address=entAddress.get(),
                city=entCity.get(),
                region=entRegion.get(),
                postalCode=entPostalCode.get(),
                country=entCountry.get(),
                phone=entPhone.get(),
                fax=entFax.get(),
                homePage=entHomePage.get())
                supplierBusinessLogic = SupplierBusinessLogic(supplierObject)
                supplierBusinessLogic.updateSupplier(self.UpdateID)
                showinfo('Success', 'Supplier updated successfully.')
                for i in tree.get_children():
                    tree.delete(i)
                supplierBusinessLogic = SupplierBusinessLogic()
                supplierBusinessLogic.getSupplier()
                self.GetData = supplierBusinessLogic.AllDataSupplier

                for item in self.GetData:
                    tree.insert("", 'end', values=item)
                clearText()


        def deleteSupplier():
            supplierObject = SupplierIdDelete(
                supplierID=self.DeleteID)
            supplierBusinessLogic = SupplierBusinessLogic(supplierObject)
            supplierBusinessLogic.deleteSupplier(self.DeleteID)
            showinfo('Success', 'Supplier deleted successfully.')
            for i in self.tree.get_children():
                self.tree.delete(i)
            supplierBusinessLogic = SupplierBusinessLogic()
            supplierBusinessLogic.getSupplier()
            self.GetData = SupplierBusinessLogic.AllDataSupplier

            for item in self.GetData:
                self.tree.insert("", 'end', values=item)
            clearText()

        # endregion

        frame = LabelFrame(supplierForm, text="Field...", width=750, height=400, padx=10)
        frameButton = LabelFrame(supplierForm, text="Opertation ...", width=750, height=200, padx=10)
        frameGrid = LabelFrame(supplierForm, text="Data ...", width=750, height=290, padx=10, pady=10)

        frame.grid(row=0, column=0, padx=10)
        frameButton.grid(row=1, column=0, padx=10)
        frameGrid.grid(row=2, column=0, padx=10)

        lblCompanyName = Label(frame, text='Company Name: ')
        lblCompanyName.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        txtCompanyName = StringVar()
        entCompanyName = ttk.Entry(frame, textvariable=txtCompanyName, width=40)
        entCompanyName.grid(row=0, column=1, padx=10, pady=10, sticky='e')

        lblContactName = Label(frame, text='Contact Name: ')
        lblContactName.grid(row=0, column=2, padx=10, pady=10, sticky='w')

        txtContactName = StringVar()
        entContactName = ttk.Entry(frame, textvariable=txtContactName, width=40)
        entContactName.grid(row=0, column=3, padx=10, pady=10, sticky='e')

        lblContactTitle = Label(frame, text='Contact Title: ')
        lblContactTitle.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        txtContactTitle = StringVar()
        entContactTitle = ttk.Entry(frame, textvariable=txtContactTitle, width=40)
        entContactTitle.grid(row=1, column=1, padx=10, pady=10, sticky='e')


        lblAddress = Label(frame, text='Address: ')
        lblAddress.grid(row=1, column=2, padx=10, pady=10, sticky='w')

        txtAddress = StringVar()
        entAddress = ttk.Entry(frame, textvariable=txtAddress, width=40)
        entAddress.grid(row=1, column=3, padx=10, pady=10, sticky='e')

        lblCity = Label(frame, text='City: ')
        lblCity.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        txtCity = StringVar()
        entCity = ttk.Entry(frame, textvariable=txtCity, width=40)
        entCity.grid(row=2, column=1, padx=10, pady=10, sticky='e')

        lblRegion = Label(frame, text='Region: ')
        lblRegion.grid(row=2, column=2, padx=10, pady=10, sticky='w')

        txtRegion = StringVar()
        entRegion = ttk.Entry(frame, textvariable=txtRegion, width=40)
        entRegion.grid(row=2, column=3, padx=10, pady=10, sticky='e')

        lblPostalCode = Label(frame, text='Postal Code: ')
        lblPostalCode.grid(row=3, column=0, padx=10, pady=10, sticky='w')

        txtPostalCode = StringVar()
        entPostalCode = ttk.Entry(frame, textvariable=txtPostalCode, width=40)
        entPostalCode.grid(row=3, column=1, padx=10, pady=10, sticky='e')

        lblCountry = Label(frame, text='Country: ')
        lblCountry.grid(row=3, column=2, padx=10, pady=10, sticky='w')

        txtCountry = StringVar()
        entCountry = ttk.Entry(frame, textvariable=txtCountry, width=40)
        entCountry.grid(row=3, column=3, padx=10, pady=10, sticky='e')

        lblPhone = Label(frame, text='Phone: ')
        lblPhone.grid(row=4, column=0, padx=10, pady=10, sticky='w')

        txtPhone = StringVar()
        entPhone = ttk.Entry(frame, textvariable=txtPhone, width=40)
        entPhone.grid(row=4, column=1, padx=10, pady=10, sticky='e')

        lblFax = Label(frame, text='Fax: ')
        lblFax.grid(row=4, column=2, padx=10, pady=10, sticky='w')

        txtFax = StringVar()
        entFax = ttk.Entry(frame, textvariable=txtFax, width=40)
        entFax.grid(row=4, column=3, padx=10, pady=10, sticky='e')

        lblHomePage = Label(frame, text='HomePage: ')
        lblHomePage.grid(row=5, column=0, padx=10, pady=10, sticky='w')

        txtHomePage = StringVar()
        entHomePage = ttk.Entry(frame, textvariable=txtHomePage, width=40)
        entHomePage.grid(row=5, column=1, padx=10, pady=10, sticky='e')






        btnClearSupplier = ttk.Button(frameButton, text='Clear', command=clearText, width=16)
        btnClearSupplier.grid(row=8, column=0, padx=10, pady=10, sticky='e')

        btnInsertSupplier = ttk.Button(frameButton, text='Insert', command=registerSupplier, width=16)
        btnInsertSupplier.grid(row=8, column=1, padx=10, pady=10, sticky='e')

        btnUpdateSupplier = ttk.Button(frameButton, text='Update', command=updateSupplier , width=16)
        btnUpdateSupplier.grid(row=8, column=2, padx=10, pady=10, sticky='e')

        btnDeleteSupplier = ttk.Button(frameButton, text='Delete', command=deleteSupplier , width=16)
        btnDeleteSupplier.grid(row=8, column=3, padx=10, pady=10, sticky='e')

        btnBackToMain = ttk.Button(frameButton, text='Close', command=destroyForm, width=14)
        btnBackToMain.grid(row=8, column=4, padx=10, pady=10, sticky='w')

        columns = (
             "companyName"
            ,"contactName"
            ,"contactTitle"
            ,"address"
            ,"city"
            ,"region"
            ,"postalCode"
            ,"country"
            ,"phone"
            ,"fax"
            ,"homePage"
        )
        tree = ttk.Treeview(frameGrid, columns=columns, show='headings')

        tree.heading("companyName", text="EmployeeID", anchor=W)
        tree.heading("contactName", text="FirstName", anchor=W)
        tree.heading("contactTitle", text="lastName", anchor=W)
        tree.heading("address", text="title", anchor=W)
        tree.heading("city", text="titleOfCourtesy", anchor=W)
        tree.heading("region", text="birthDate", anchor=W)
        tree.heading("postalCode", text="hireDate", anchor=W)
        tree.heading("country", text="address", anchor=W)
        tree.heading("phone", text="city", anchor=W)
        tree.heading("fax", text="region", anchor=W)
        tree.heading("homePage", text="postalCode", anchor=W)

        for item in self.GetData:
            tree.insert("", 'end', values=item)

        def item_selected(event):
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                record = item['values']
                entCompanyName.delete(0, END)
                entCompanyName.insert(0, record[1])
                entContactName.delete(0, END)
                entContactName.insert(0, record[2])
                entContactTitle.delete(0, END)
                entContactTitle.insert(0, record[3])
                entAddress.delete(0, END)
                entAddress.insert(0, record[4])
                entCity.delete(0, END)
                entCity.insert(0, record[5])
                entRegion.delete(0, END)
                entRegion.insert(0, record[6])
                entPostalCode.delete(0, END)
                entPostalCode.insert(0, record[7])
                entCountry.delete(0, END)
                entCountry.insert(0, record[8])
                entPhone.delete(0, END)
                entPhone.insert(0, record[9])
                entFax.delete(0, END)
                entFax.insert(0, record[10])
                entHomePage.delete(0, END)
                entHomePage.insert(0, record[11])

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

        supplierForm.columnconfigure(0, weight=1)
        supplierForm.rowconfigure(0, weight=1)
        frameGrid.columnconfigure(0, weight=3)
        frameGrid.columnconfigure(1, weight=3)
        frameGrid.columnconfigure(2, weight=3)
        frameGrid.columnconfigure(3, weight=1)
        frameGrid.columnconfigure(4, weight=1)
        frameGrid.rowconfigure(1, weight=1)

        supplierForm.mainloop()
