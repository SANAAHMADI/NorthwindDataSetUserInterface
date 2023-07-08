import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from Models.UserModel import User
from Models.CustomerModel import Customer, CustomerIdDelete
from BusinessLogic.CustomerBusinessLogic import CustomerBusinessLogic
from tkcalendar import DateEntry
from datetime import datetime


class customerForm:

    def __init__(self, user: User):
        self.User = user
        self.GetData = []
        self.DeleteID = 0
        self.UpdateID = 0

    def customer_FormLoad(self):
        customerForm = Tk()
        customerForm.title('Customer Register')
        customerForm.geometry('800x610')
        # customerForm.config(bg="#6F9270")
        # customerForm.resizable(0, 0)
        positionRight = int(customerForm.winfo_screenwidth() / 2 - 800 / 2)
        positionDown = int(customerForm.winfo_screenheight() / 2 - 610 / 2)
        customerForm.geometry("+{}+{}".format(positionRight, positionDown))
        customerBusinessLogic = CustomerBusinessLogic()
        customerBusinessLogic.getCustomer()
        self.GetData = customerBusinessLogic.AllDataCustomer

        def destroyForm():
            customerForm.destroy()

        def clearText():
            entCustomerID.delete(0,END)
            entCompanyName.delete(0, END)
            entRegion.delete(0, END)
            entCity.delete(0, END)
            entAddress.delete(0, END)
            entCountry.delete(0, END)
            entPostalCode.delete(0, END)
            entContactName.delete(0, END)
            entContactTitle.delete(0, END)
            entPhone.delete(0, END)
            entFax.delete(0, END)


        def validate10(value):
            return len(value) <= 10
        def validate15(value):
            return len(value) <= 15
        def validate40(value):
            return len(value) <= 40
        def validate30(value):
            return len(value) <= 30
        def validate60(value):
            return len(value) <= 60
        def validate24(value):
            return len(value) <= 24


        def registerCustomer():
            companyName = entCompanyName.get()
            contactName = entContactName.get()
            contactTitle = entContactTitle.get()
            phone = entPhone.get()
            fax = entFax.get()
            customerID = entCustomerID.get()
            if not contactTitle.isalpha() or not contactName.isalpha() or not companyName.isalpha():
                showinfo('Error', 'Contact title and Contact Name and Company Name can only contain letters.')
                return False
            if not fax.isalnum() or not phone.isalnum() or fax.isalpha() or phone.isalpha():
                showinfo('Error', 'Fax and Phone can only contain numbers.')
                return False
            if customerID=='':
                showinfo('Error', 'Fill The Customer ID')
                return False
            else:
                customerObject = Customer(
                    customerID=entCustomerID.get(),
                    companyName=entCompanyName.get(),
                    contactName=entContactName.get(),
                    contactTitle=entContactTitle.get(),
                    address=entAddress.get(),
                    city=entCity.get(),
                    region=entRegion.get(),
                    postalCode=entPostalCode.get(),
                    country=entCountry.get(),
                    phone=entPhone.get(),
                    fax=entFax.get())
                customerBLLObject = CustomerBusinessLogic(customerObject)
                customerBLLObject.insertCustomer()
                showinfo('Success', 'Customer registered successfully.')
                for i in tree.get_children():
                    tree.delete(i)
                customerBusinessLogic = CustomerBusinessLogic()
                customerBusinessLogic.getCustomer()
                self.GetData = customerBusinessLogic.AllDataCustomer
                for item in self.GetData:
                    tree.insert("", 'end', values=item)
                clearText()


        def updateCustomer():
            companyName = entCompanyName.get()
            contactName = entContactName.get()
            contactTitle = entContactTitle.get()
            phone = entPhone.get()
            fax = entFax.get()
            if not contactTitle.isalpha() or not contactName.isalpha() or not companyName.isalpha():
                showinfo('Error', 'Contact title and Contact Name and Company Name can only contain letters.')
                return False
            if not fax.isalnum() or not phone.isalnum() or fax.isalpha() or phone.isalpha():
                showinfo('Error', 'Fax and Phone can only contain numbers.')
                return False
            else:
                customerObject = Customer(
                    customerID=self.UpdateID,
                    companyName=entCompanyName.get(),
                    contactName=entContactName.get(),
                    contactTitle=entContactTitle.get(),
                    address=entAddress.get(),
                    city=entCity.get(),
                    region=entRegion.get(),
                    postalCode=entPostalCode.get(),
                    country=entCountry.get(),
                    phone=entPhone.get(),
                    fax=entFax.get())
                customerBusinessLogic = CustomerBusinessLogic(customerObject)
                customerBusinessLogic.updateCustomer(self.UpdateID)
                showinfo('Success', 'Customer updated successfully.')
                for i in tree.get_children():
                    tree.delete(i)
                customerBusinessLogic = CustomerBusinessLogic()
                customerBusinessLogic.getCustomer()
                self.GetData = customerBusinessLogic.AllDataCustomer

                for item in self.GetData:
                    tree.insert("", 'end', values=item)
                clearText()

        def deleteCustomer():
            customerObject = CustomerIdDelete(
                customerID=self.DeleteID)
            customerBusinessLogic = CustomerBusinessLogic(customerObject)
            customerBusinessLogic.deleteCustomer(self.DeleteID)
            showinfo('Success', 'Customer deleted successfully.')
            for i in tree.get_children():
                tree.delete(i)
            customerBusinessLogic = CustomerBusinessLogic()
            customerBusinessLogic.getCustomer()
            self.GetData = customerBusinessLogic.AllDataCustomer

            for item in self.GetData:
                tree.insert("", 'end', values=item)
            clearText()


        # endregion

        frame = LabelFrame(customerForm, text="Field...", width=750, height=400, padx=10)
        frameButton = LabelFrame(customerForm, text="Opertation ...", width=750, height=200, padx=10)
        frameGrid = LabelFrame(customerForm, text="Data ...", width=750, height=290, padx=10, pady=10)

        frame.grid(row=0, column=0, padx=10)
        frameButton.grid(row=1, column=0, padx=10)
        frameGrid.grid(row=2, column=0, padx=10)

        lblCustomerID = Label(frame, text='Company ID: ')
        lblCustomerID.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        txtCustomerID = StringVar()
        entCustomerID = ttk.Entry(frame, textvariable=txtCustomerID, width=40)

        entCustomerID.grid(row=0, column=1, padx=10, pady=10, sticky='e')

        lblCompanyName = Label(frame, text='Company Name: ')
        lblCompanyName.grid(row=0, column=2, padx=10, pady=10, sticky='w')

        txtCompanyName = StringVar()
        entCompanyName = ttk.Entry(frame, textvariable=txtCompanyName, width=40)
        entCompanyName.focus()
        entCompanyName.config(validate="key", validatecommand=(entCompanyName.register(validate40), "%P"))
        entCompanyName.grid(row=0, column=3, padx=10, pady=10, sticky='e')

        lblContactName = Label(frame, text='Contact Name:  ')
        lblContactName.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        txtContactName = StringVar()
        entContactName = ttk.Entry(frame, textvariable=txtContactName, width=40)
        entContactName.focus()
        entContactName.config(validate="key", validatecommand=(entContactName.register(validate30), "%P"))
        entContactName.grid(row=1, column=1, padx=10, pady=10, sticky='e')

        lblContactTitle = Label(frame, text='Contact Title: ')
        lblContactTitle.grid(row=1, column=2, padx=10, pady=10, sticky='w')

        txtContactTitle = StringVar()
        entContactTitle = ttk.Entry(frame, textvariable=txtContactTitle, width=40)
        entContactTitle.focus()
        entContactTitle.config(validate="key", validatecommand=(entContactTitle.register(validate30), "%P"))
        entContactTitle.grid(row=1, column=3, padx=10, pady=10, sticky='e')

        lblAddress = Label(frame, text='Address: ')
        lblAddress.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        txtAddress = StringVar()
        entAddress = ttk.Entry(frame, textvariable=txtAddress, width=40)
        entAddress.focus()
        entAddress.config(validate="key", validatecommand=(entAddress.register(validate60), "%P"))
        entAddress.grid(row=2, column=1, padx=10, pady=10, sticky='e')

        lblCity = Label(frame, text='City: ')
        lblCity.grid(row=2, column=2, padx=10, pady=10, sticky='w')

        txtCity = StringVar()
        entCity = ttk.Entry(frame, textvariable=txtCity, width=40)
        entCity.focus()
        entCity.config(validate="key", validatecommand=(entCity.register(validate15), "%P"))
        entCity.grid(row=2, column=3, padx=10, pady=10, sticky='e')

        lblRegion = Label(frame, text='Region: ')
        lblRegion.grid(row=3, column=0, padx=10, pady=10, sticky='w')

        txtRegion = StringVar()
        entRegion = ttk.Entry(frame, textvariable=txtRegion, width=40)
        entRegion.config(validate="key", validatecommand=(entRegion.register(validate15), "%P"))
        entRegion.grid(row=3, column=1, padx=10, pady=10, sticky='e')

        lblPostalCode = Label(frame, text='Postal Code: ')
        lblPostalCode.grid(row=3, column=2, padx=10, pady=10, sticky='w')

        txtPostalCode = StringVar()
        entPostalCode = ttk.Entry(frame, textvariable=txtPostalCode, width=40)
        entPostalCode.focus()
        entPostalCode.config(validate="key", validatecommand=(entPostalCode.register(validate10), "%P"))
        entPostalCode.grid(row=3, column=3, padx=10, pady=10, sticky='e')

        lblCountry = Label(frame, text='Country: ')
        lblCountry.grid(row=4, column=0, padx=10, pady=10, sticky='w')

        txtCountry = StringVar()
        entCountry = ttk.Entry(frame, textvariable=txtCountry, width=40)
        entCountry.focus()
        entCountry.config(validate="key", validatecommand=(entCountry.register(validate15), "%P"))
        entCountry.grid(row=4, column=1, padx=10, pady=10, sticky='e')

        lbtPhone = Label(frame, text='Phone: ')
        lbtPhone.grid(row=4, column=2, padx=10, pady=10, sticky='w')

        txtPhone = StringVar()
        entPhone = ttk.Entry(frame, textvariable=txtPhone, width=40)
        entPhone.focus()
        entPhone.config(validate="key", validatecommand=(entPhone.register(validate24), "%P"))
        entPhone.grid(row=4, column=3, padx=10, pady=10, sticky='e')

        lbtFax = Label(frame, text='Fax: ')
        lbtFax.grid(row=5, column=0, padx=10, pady=10, sticky='w')

        txtFax = StringVar()
        entFax = ttk.Entry(frame, textvariable=txtFax, width=40)
        entFax.focus()
        entFax.config(validate="key", validatecommand=(entFax.register(validate24), "%P"))
        entFax.grid(row=5, column=1, padx=10, pady=10, sticky='e')



        btnClearCustomer= ttk.Button(frameButton, text='Clear', command=clearText, width=16)
        btnClearCustomer.focus()
        btnClearCustomer.grid(row=0, column=0, padx=10, pady=10, sticky='e')

        btnInsertCustomer = ttk.Button(frameButton, text='Insert',command=registerCustomer, width=16)
        btnInsertCustomer.focus()
        btnInsertCustomer.grid(row=0, column=1, padx=10, pady=10, sticky='e')

        btnUpdateCustomer = ttk.Button(frameButton, text='Update',command=updateCustomer, width=16)
        btnUpdateCustomer.focus()
        btnUpdateCustomer.grid(row=0, column=2, padx=10, pady=10, sticky='e')

        btnDeleteCustomer = ttk.Button(frameButton, text='Delete',command=deleteCustomer, width=16)
        btnDeleteCustomer.focus()
        btnDeleteCustomer.grid(row=0, column=3, padx=10, pady=10, sticky='e')

        btnBackToMain = ttk.Button(frameButton, text='Close', command=destroyForm, width=16)
        btnBackToMain.focus()
        btnBackToMain.grid(row=0, column=4, padx=10, pady=10, sticky='e')

        columns = ("customerID",
                   "companyName",
                   "contactName",
                   "contactTitle",
                   "address",
                   "city",
                   "region",
                   "postalCode",
                   "country",
                   "phone",
                   "fax")

        tree = ttk.Treeview(frameGrid, columns=columns, show='headings')

        tree.heading("customerID", text="CustomerID", anchor=W)
        tree.heading("companyName", text="CompanyName", anchor=W)
        tree.heading("contactName", text="ContactName", anchor=W)
        tree.heading("contactTitle", text="ContactTitle", anchor=W)
        tree.heading("address", text="Address", anchor=W)
        tree.heading("city", text="City", anchor=W)
        tree.heading("region", text="Region", anchor=W)
        tree.heading("postalCode", text="PostalCode", anchor=W)
        tree.heading("country", text="Country", anchor=W)
        tree.heading("phone", text="Phone", anchor=W)
        tree.heading("fax", text="Fax", anchor=W)

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


                entCustomerID.delete(0, END)
                entCustomerID(0, record[11])

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

        customerForm.columnconfigure(0, weight=1)
        customerForm.rowconfigure(0, weight=1)
        frameGrid.columnconfigure(0, weight=3)
        frameGrid.columnconfigure(1, weight=3)
        frameGrid.columnconfigure(2, weight=3)
        frameGrid.columnconfigure(3, weight=1)
        frameGrid.columnconfigure(4, weight=1)
        frameGrid.rowconfigure(1, weight=1)

        customerForm.mainloop()
