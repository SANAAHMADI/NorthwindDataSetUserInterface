import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from Models.UserModel import User
from Models.ShipperModel import *
from BusinessLogic.ShipperBusinessLogic import ShipperBusinessLogic
from DataAccess.ShipperDataAccess import ShipperDataAccess
from tkcalendar import DateEntry
from datetime import datetime


class ShipperForm:

    def __init__(self, user: User):
        self.User = user
        self.GetData = []
        self.DeleteID = 0
        self.UpdateID=0

    def shipper_FormLoad(self):
        shipperForm = Tk()
        shipperForm.title('Shipper Register')
        shipperForm.geometry('800x420')
        shipperForm.config(bg="LightBlue")
        positionRight = int(shipperForm.winfo_screenwidth() / 2 - 800 / 2)
        positionDown = int(shipperForm.winfo_screenheight() / 2 - 420 / 2)
        shipperForm.geometry("+{}+{}".format(positionRight, positionDown))
        shipperBusinessLogic = ShipperBusinessLogic()
        shipperBusinessLogic.getShipper()
        self.GetData = shipperBusinessLogic.AllDataShipper

        def destroyForm():
            shipperForm.destroy()

        def clearText():
            entCompanyName.delete(0, END)
            entPhone.delete(0, END)




        def registerShipper():
            companyName = entCompanyName.get(),
            phone = entPhone.get()
            if len(companyName) > 15 or not companyName.isalpha():
                showinfo('Error', 'Category name cannot exceed 15 characters and can only contain letters.')
                return False
            if len(phone) > 24 or not phone.isalnum():
                showinfo('Error', 'Phone cannot exceed 24 characters can only contain numbers.')
                return False
            else:
                shipperObject = Shipper(
                    companyName=entCompanyName.get(),
                    phone=entPhone.get())
                shipperBLLObject = ShipperBusinessLogic(shipperObject)
                shipperBLLObject.insertShipper()
                showinfo('Success', 'Shipper Registered successfully.')
                for i in tree.get_children():
                    tree.delete(i)
                shipperBusinessLogic = ShipperBusinessLogic()
                shipperBusinessLogic.getShipper()
                self.GetData = shipperBusinessLogic.AllDataShipper

                for item in self.GetData:
                    tree.insert("", 'end', values=item)
                clearText()

        def updateShipper():
            companyName = entCompanyName.get()
            if len(companyName) > 15 or not companyName.isalpha():
                showinfo('Error', 'Category name cannot exceed 15 characters and can only contain letters.')
            if len(entPhone) > 24 or not entPhone.isalnum():
                showinfo('Error', 'Phone cannot exceed 24 characters can only contain numbers.')
            else:
                shipperObject = Shipper(
                    companyName=entCompanyName.get(),
                    phone=entPhone.get())
                shipperBusinessLogic = ShipperBusinessLogic(shipperObject)
                shipperBusinessLogic.updateShipper(self.UpdateID)
                showinfo('Success', 'Shipper updated successfully.')
                for i in tree.get_children():
                    tree.delete(i)
                shipperBusinessLogic = ShipperBusinessLogic()
                shipperBusinessLogic.getShipper()
                self.GetData = shipperBusinessLogic.AllDataShipper

                for item in self.GetData:
                    tree.insert("", 'end', values=item)
                clearText()

        def deleteShipper():
            shipperObject = ShipperIdDelete(
                shipperID=self.DeleteID)
            shipperBusinessLogic = ShipperBusinessLogic(shipperObject)
            shipperBusinessLogic.deleteShipper(self.DeleteID)
            showinfo('Success', 'Shipper deleted successfully.')
            for i in tree.get_children():
                tree.delete(i)
            shipperBusinessLogic = ShipperBusinessLogic()
            shipperBusinessLogic.getShipper()
            self.GetData = shipperBusinessLogic.AllDataShipper

            for item in self.GetData:
                tree.insert("", 'end', values=item)
            clearText()

        # endregion

        frame = LabelFrame(shipperForm, text="Field...", width=750, height=400, padx=10)
        frameButton = LabelFrame(shipperForm, text="Opertation ...", width=750, height=200, padx=10)
        frameGrid = LabelFrame(shipperForm, text="Data ...", width=750, height=290, padx=10, pady=10)

        frame.grid(row=0, column=0, padx=10)
        frameButton.grid(row=1, column=0, padx=10)
        frameGrid.grid(row=2, column=0, padx=10)

        lblCompanyName = Label(frame, text='Company Name: ')
        lblCompanyName.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        txtCompanyName = StringVar()
        entCompanyName = ttk.Entry(frame, textvariable=txtCompanyName, width=40)
        entCompanyName.grid(row=0, column=1, padx=10, pady=10, sticky='e')

        lblPhone = Label(frame, text='Phone: ')
        lblPhone.grid(row=0, column=2, padx=10, pady=10, sticky='w')

        txtPhone = StringVar()
        entPhone = ttk.Entry(frame, textvariable=txtPhone, width=40)
        entPhone.grid(row=0, column=3, padx=10, pady=10, sticky='e')



        btnClearEmployee = ttk.Button(frameButton, text='Clear', command=clearText, width=16)
        btnClearEmployee.grid(row=1, column=0, padx=10, pady=10, sticky='e')

        btnInsertEmployee = ttk.Button(frameButton, text='Insert', command=registerShipper, width=16)
        btnInsertEmployee.grid(row=1, column=1, padx=10, pady=10, sticky='e')

        btnupdateShipper = ttk.Button(frameButton, text='Update', command=updateShipper , width=16)
        btnupdateShipper.grid(row=1, column=2, padx=10, pady=10, sticky='e')

        btndeleteShipper = ttk.Button(frameButton, text='Delete', command=deleteShipper , width=16)
        btndeleteShipper.grid(row=1, column=3, padx=10, pady=10, sticky='e')

        btnBackToMain = ttk.Button(frameButton, text='Close', command=destroyForm, width=14)
        btnBackToMain.grid(row=1, column=4, padx=10, pady=10, sticky='w')

        columns = ("shipperId","companyName","phone")
        tree = ttk.Treeview(frameGrid, columns=columns, show='headings')

        tree.heading("shipperId", text="ShipperID", anchor=W)
        tree.heading("companyName", text="CompanyName", anchor=W)
        tree.heading("phone", text="Phone", anchor=W)

        for item in self.GetData:
            tree.insert("", 'end', values=item)

        def item_selected(event):
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                record = item['values']

                entCompanyName.delete(0, END)
                entCompanyName.insert(0, record[1])

                entPhone.delete(0, END)
                entPhone.insert(0, record[2])\


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

        shipperForm.columnconfigure(0, weight=1)
        shipperForm.rowconfigure(0, weight=1)
        frameGrid.columnconfigure(0, weight=3)
        frameGrid.columnconfigure(1, weight=3)
        frameGrid.columnconfigure(2, weight=3)
        frameGrid.columnconfigure(3, weight=1)
        frameGrid.columnconfigure(4, weight=1)
        frameGrid.rowconfigure(1, weight=1)

        shipperForm.mainloop()
