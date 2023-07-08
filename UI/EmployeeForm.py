import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from Models.UserModel import User
from Models.EmployeeModel import *
from BusinessLogic.EmployeeBusinessLogic import EmployeeBusinessLogic
from DataAccess.EmployeeDataAccess import EmployeeDataAccess
from tkcalendar import DateEntry
from datetime import datetime


class EmployeeForm:

    def __init__(self, user: User):
        self.User = user
        self.GetData = []
        self.DeleteID = 0
        self.UpdateID=0

    def employee_FormLoad(self):
        employeeForm = Tk()
        employeeForm.title('Employee Register')
        employeeForm.geometry('800x720')
        employeeForm.config(bg="LightBlue")
        positionRight = int(employeeForm.winfo_screenwidth() / 2 - 800 / 2)
        positionDown = int(employeeForm.winfo_screenheight() / 2 - 720 / 2)
        employeeForm.geometry("+{}+{}".format(positionRight, positionDown))
        employeeBusinessLogic = EmployeeBusinessLogic()
        employeeBusinessLogic.getEmployee()
        self.GetData = employeeBusinessLogic.AllDataEmployee

        def destroyForm():
            employeeForm.destroy()

        def clearText():
            entCity.delete(0, END)
            entFirstName.delete(0, END)
            entCity.delete(0, END)
            entTitle.delete(0, END)
            entNotes.delete(0, END)
            entRegion.delete(0, END)
            entAddress.delete(0, END)
            entBirthDate.delete(0, END)
            entCountry.delete(0, END)
            entExtension.delete(0, END)
            entHireDate.delete(0, END)
            entHomePhone.delete(0, END)
            entLastName.delete(0, END)
            entPostalCode.delete(0, END)
            # entReportsTo.delete(0, END)
            entTitleOfCourtesy.delete(0, END)

        def registerEmployee():
            firstName = entFirstName.get()
            lastName = entLastName.get()
            title = entTitle.get()
            titleOfCourtesy = entTitleOfCourtesy.get()
            birthDate = entBirthDate.get()
            hireDate = entHireDate.get()
            address = entAddress.get()
            city = entCity.get()
            region = entRegion.get()
            postalCode = entPostalCode.get()
            country = entCountry.get()
            homePhone = entHomePhone.get()
            extension = entExtension.get()
            notes = entNotes.get()
            if len(firstName) > 10 or not firstName.isalpha():
                showinfo('Error', 'First Name cannot exceed 10 characters and can only contain letters.')
                return False
            if len(lastName) > 20 or not lastName.isalpha():
                showinfo('Error', 'last Name cannot exceed 20 characters and can only contain letters.')
                return False
            if len(title) > 30 or not title.isalpha():
                showinfo('Error', 'title cannot exceed 30 characters and can only contain letters.')
                return False
            if len(titleOfCourtesy) > 25 or not titleOfCourtesy.isalpha():
                showinfo('Error', 'Category name cannot exceed 25 characters and can only contain letters.')
                return False
            if len(address) > 60 or not address.isalpha():
                showinfo('Error', 'address cannot exceed 60 characters and can only contain letters.')
                return False
            if len(city) > 15 or not city.isalpha():
                showinfo('Error', 'city cannot exceed 15 characters and can only contain letters.')
                return False
            if len(region) > 15 or not region.isalpha():
                showinfo('Error', 'region cannot exceed 15 characters and can only contain letters.')
                return False
            if len(postalCode) > 10 or not postalCode.isalpha():
                showinfo('Error', 'postal Code cannot exceed 10 and can only contain letters.')
                return False
            if len(country) > 15 or not country.isalpha():
                showinfo('Error', 'country cannot exceed 15 characters and can only contain letters.')
                return False
            if len(homePhone) > 24 or not homePhone.isalnum():
                showinfo('Error', 'Home Phone cannot exceed 24 characters can only contain numbers.')
                return False
            if len(extension) > 4 or not extension.isalpha():
                showinfo('Error', 'extension cannot exceed 4 characters and can only contain letters.')
                return False
            else:

                employeeObject = Employee(
                    firstName=entFirstName.get(),
                    lastName=entLastName.get(),
                    title=entTitle.get(),
                    titleOfCourtesy=entTitleOfCourtesy.get(),
                    birthDate=entBirthDate.get(),
                    hireDate=entHireDate.get(),
                    address=entAddress.get(),
                    city=entCity.get(),
                    region=entRegion.get(),
                    postalCode=entPostalCode.get(),
                    country=entCountry.get(),
                    homePhone=entHomePhone.get(),
                    extension=entExtension.get(),
                    notes=entNotes.get())
                employeeBLLObject = EmployeeBusinessLogic(employeeObject)
                employeeBLLObject.insertEmployee()
                showinfo('Success', 'Employee Registered successfully.')
                for i in tree.get_children():
                    tree.delete(i)
                employeeBusinessLogic = EmployeeBusinessLogic()
                employeeBusinessLogic.getEmployee()
                self.GetData = employeeBusinessLogic.AllDataEmployee

            for item in self.GetData:
                tree.insert("", 'end', values=item)
            clearText()

        def updateEmployee():
            firstName = entFirstName.get()
            lastName = entLastName.get()
            title = entTitle.get()
            titleOfCourtesy = entTitleOfCourtesy.get()
            birthDate = entBirthDate.get()
            hireDate = entHireDate.get()
            address = entAddress.get()
            city = entCity.get()
            region = entRegion.get()
            postalCode = entPostalCode.get()
            country = entCountry.get()
            homePhone = entHomePhone.get()
            extension = entExtension.get()
            notes = entNotes.get()
            if len(firstName) > 10 or not firstName.isalpha():
                showinfo('Error', 'First Name cannot exceed 10 characters and can only contain letters.')
                return False
            if len(lastName) > 20 or not lastName.isalpha():
                showinfo('Error', 'last Name cannot exceed 20 characters and can only contain letters.')
                return False
            if len(title) > 30 or not title.isalpha():
                showinfo('Error', 'title cannot exceed 30 characters and can only contain letters.')
                return False
            if len(titleOfCourtesy) > 25 or not titleOfCourtesy.isalpha():
                showinfo('Error', 'Category name cannot exceed 25 characters and can only contain letters.')
                return False
            if len(address) > 60 or not address.isalpha():
                showinfo('Error', 'address cannot exceed 60 characters and can only contain letters.')
                return False
            if len(city) > 15 or not city.isalpha():
                showinfo('Error', 'city cannot exceed 15 characters and can only contain letters.')
                return False
            if len(region) > 15 or not region.isalpha():
                showinfo('Error', 'region cannot exceed 15 characters and can only contain letters.')
                return False
            if len(postalCode) > 10 or not postalCode.isalnum():
                showinfo('Error', 'postal Code cannot exceed 10 and can only contain numbers.')
                return False
            if len(country) > 15 or not country.isalpha():
                showinfo('Error', 'country cannot exceed 15 characters and can only contain letters.')
                return False
            if len(homePhone) > 24 or not homePhone.isalnum():
                showinfo('Error', 'Home Phone cannot exceed 24 characters can only contain numbers.')
                return False
            if len(extension) > 4 or not extension.isalpha():
                showinfo('Error', 'extension cannot exceed 4 characters and can only contain letters.')
                return False

            else:
                employeeObject = Employee(
                    firstName=entFirstName.get(),
                    lastName=entLastName.get(),
                    title=entTitle.get(),
                    titleOfCourtesy=entTitleOfCourtesy.get(),
                    birthDate=entBirthDate.get(),
                    hireDate=entHireDate.get(),
                    address=entAddress.get(),
                    city=entCity.get(),
                    region=entRegion.get(),
                    postalCode=entPostalCode.get(),
                    country=entCountry.get(),
                    homePhone=entHomePhone.get(),
                    extension=entExtension.get(),
                    notes=entNotes.get())
                    # reportsTo=txtReportsTo.get()
                employeeBusinessLogic = EmployeeBusinessLogic(employeeObject)
                employeeBusinessLogic.updateEmployee(self.UpdateID)
                showinfo('Success', 'Employee updated successfully.')

                for i in tree.get_children():
                    tree.delete(i)
                employeeBusinessLogic = EmployeeBusinessLogic()
                employeeBusinessLogic.getEmployee()
                self.GetData = employeeBusinessLogic.AllDataEmployee

                for item in self.GetData:
                    tree.insert("", 'end', values=item)

                clearText()

        def deleteEmployee():
            employeeObject = EmloyeeIdDelete(
                emloyeeID=self.DeleteID)
            employeeBusinessLogic = EmployeeBusinessLogic(employeeObject)
            employeeBusinessLogic.deleteEmployee(self.DeleteID)
            showinfo('Success', 'Employee deleted successfully.')
            for i in tree.get_children():
                tree.delete(i)
            employeeBusinessLogic = EmployeeBusinessLogic()
            employeeBusinessLogic.getEmployee()
            self.GetData = employeeBusinessLogic.AllDataEmployee

            for item in self.GetData:
                tree.insert("", 'end', values=item)
            clearText()

        # endregion

        frame = LabelFrame(employeeForm, text="Field...", width=750, height=400, padx=10)
        frameButton = LabelFrame(employeeForm, text="Opertation ...", width=750, height=200, padx=10)
        frameGrid = LabelFrame(employeeForm, text="Data ...", width=750, height=290, padx=10, pady=10)

        frame.grid(row=0, column=0, padx=10)
        frameButton.grid(row=1, column=0, padx=10)
        frameGrid.grid(row=2, column=0, padx=10)

        lblLastName = Label(frame, text='Last Name: ')
        lblLastName.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        txtLastName = StringVar()
        entLastName = ttk.Entry(frame, textvariable=txtLastName, width=40)
        entLastName.grid(row=0, column=1, padx=10, pady=10, sticky='e')

        lblFirstName = Label(frame, text='First Name: ')
        lblFirstName.grid(row=0, column=2, padx=10, pady=10, sticky='w')

        txtFirstName = StringVar()
        entFirstName = ttk.Entry(frame, textvariable=txtFirstName, width=40)
        entFirstName.grid(row=0, column=3, padx=10, pady=10, sticky='e')

        lblTitle = Label(frame, text='Title: ')
        lblTitle.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        txtTitle = StringVar()
        entTitle = ttk.Entry(frame, textvariable=txtTitle, width=40)
        entTitle.grid(row=1, column=1, padx=10, pady=10, sticky='e')

        lblTitleOfCourtesy = Label(frame, text='Title of Courtesy: ')
        lblTitleOfCourtesy.grid(row=1, column=2, padx=10, pady=10, sticky='w')

        txtTitleOfCourtesy = StringVar()
        entTitleOfCourtesy = ttk.Entry(frame, textvariable=txtTitleOfCourtesy, width=40)
        entTitleOfCourtesy.grid(row=1, column=3, padx=10, pady=10, sticky='e')

        lblBirthDate = Label(frame, text='Birth Date: ')
        lblBirthDate.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        txtBirthDate = StringVar()
        entBirthDate = DateEntry(frame, textvariable=txtBirthDate, width=30)
        entBirthDate.grid(row=2, column=1, padx=10, pady=10, sticky='e')

        lblHireDate = Label(frame, text='Hire Date: ')
        lblHireDate.grid(row=2, column=2, padx=10, pady=10, sticky='w')

        txtHireDate = StringVar()
        entHireDate = DateEntry(frame, textvariable=txtHireDate, width=30)
        entHireDate.grid(row=2, column=3, padx=10, pady=10, sticky='e')

        lblAddress = Label(frame, text='Address: ')
        lblAddress.grid(row=3, column=0, padx=10, pady=10, sticky='w')

        txtAddress = StringVar()
        entAddress = ttk.Entry(frame, textvariable=txtAddress, width=40)
        entAddress.grid(row=3, column=1, padx=10, pady=10, sticky='e')

        lblCity = Label(frame, text='City: ')
        lblCity.grid(row=3, column=2, padx=10, pady=10, sticky='w')

        txtCity = StringVar()
        entCity = ttk.Entry(frame, textvariable=txtCity, width=40)
        entCity.grid(row=3, column=3, padx=10, pady=10, sticky='e')

        lblRegion = Label(frame, text='Region: ')
        lblRegion.grid(row=4, column=0, padx=10, pady=10, sticky='w')

        txtRegion = StringVar()
        entRegion = ttk.Entry(frame, textvariable=txtRegion, width=40)
        entRegion.grid(row=4, column=1, padx=10, pady=10, sticky='e')

        lblPostalCode = Label(frame, text='Postal Code: ')
        lblPostalCode.grid(row=4, column=2, padx=10, pady=10, sticky='w')

        txtPostalCode = StringVar()
        entPostalCode = ttk.Entry(frame, textvariable=txtPostalCode, width=40)
        entPostalCode.grid(row=4, column=3, padx=10, pady=10, sticky='e')

        lblCountry = Label(frame, text='Country: ')
        lblCountry.grid(row=5, column=0, padx=10, pady=10, sticky='w')

        txtCountry = StringVar()
        entCountry = ttk.Entry(frame, textvariable=txtCountry, width=40)
        entCountry.grid(row=5, column=1, padx=10, pady=10, sticky='e')

        lblHomePhone = Label(frame, text='Home Phone: ')
        lblHomePhone.grid(row=5, column=2, padx=10, pady=10, sticky='w')

        txtHomePhone = StringVar()
        entHomePhone = ttk.Entry(frame, textvariable=txtHomePhone, width=40)
        entHomePhone.grid(row=5, column=3, padx=10, pady=10, sticky='e')

        lblExtension = Label(frame, text='Extension: ')
        lblExtension.grid(row=6, column=0, padx=10, pady=10, sticky='w')

        txtExtension = StringVar()
        entExtension = ttk.Entry(frame, textvariable=txtExtension, width=40)
        entExtension.grid(row=6, column=1, padx=10, pady=10, sticky='e')

        lblNotes = Label(frame, text='Notes: ')
        lblNotes.grid(row=6, column=2, padx=10, pady=10, sticky='w')

        txtNotes = StringVar()
        entNotes = ttk.Entry(frame, textvariable=txtNotes, width=40)
        entNotes.grid(row=6, column=3, padx=10, pady=10, sticky='e')

        # lblReportsTo = Label(frame, text='Reports To: ')
        # lblReportsTo.grid(row=7, column=0, padx=10, pady=10, sticky='w')
        #
        # txtReportsTo = StringVar()
        # entReportsTo = ttk.Entry(frame, textvariable=txtReportsTo, width=40)
        # entReportsTo.grid(row=7, column=1, padx=10, pady=10, sticky='e')

        btnClearEmployee = ttk.Button(frameButton, text='Clear', command=clearText, width=16)
        btnClearEmployee.grid(row=8, column=0, padx=10, pady=10, sticky='e')

        btnInsertEmployee = ttk.Button(frameButton, text='Insert', command=registerEmployee, width=16)
        btnInsertEmployee.grid(row=8, column=1, padx=10, pady=10, sticky='e')

        btnUpdateEmployee = ttk.Button(frameButton, text='Update', command=updateEmployee , width=16)
        btnUpdateEmployee.grid(row=8, column=2, padx=10, pady=10, sticky='e')

        btnDeleteEmployee = ttk.Button(frameButton, text='Delete', command=deleteEmployee , width=16)
        btnDeleteEmployee.grid(row=8, column=3, padx=10, pady=10, sticky='e')

        btnBackToMain = ttk.Button(frameButton, text='Close', command=destroyForm, width=14)
        btnBackToMain.grid(row=8, column=4, padx=10, pady=10, sticky='w')

        columns = ("employeeID",
                   "firstName",
                   "lastName",
                   "title",
                   "titleOfCourtesy",
                   "birthDate",
                   "hireDate",
                   "address",
                   "city",
                   "region",
                   "postalCode",
                   "country",
                   "homePhone",
                   "extension",
                   "notes",
                   "reportsTo")
        tree = ttk.Treeview(frameGrid, columns=columns, show='headings')

        tree.heading("employeeID", text="EmployeeID", anchor=W)
        tree.heading("firstName", text="FirstName", anchor=W)
        tree.heading("lastName", text="lastName", anchor=W)
        tree.heading("title", text="title", anchor=W)
        tree.heading("titleOfCourtesy", text="titleOfCourtesy", anchor=W)
        tree.heading("birthDate", text="birthDate", anchor=W)
        tree.heading("hireDate", text="hireDate", anchor=W)
        tree.heading("address", text="address", anchor=W)
        tree.heading("city", text="city", anchor=W)
        tree.heading("region", text="region", anchor=W)
        tree.heading("postalCode", text="postalCode", anchor=W)
        tree.heading("postalCode", text="postalCode", anchor=W)
        tree.heading("homePhone", text="homePhone", anchor=W)
        tree.heading("extension", text="extension", anchor=W)
        tree.heading("notes", text="notes", anchor=W)
        tree.heading("reportsTo", text="reportsTo", anchor=W)

        for item in self.GetData:
            tree.insert("", 'end', values=item)

        def item_selected(event):
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                record = item['values']

                entFirstName.delete(0, END)
                entFirstName.insert(0, record[1])

                entLastName.delete(0, END)
                entLastName.insert(0, record[2])

                entTitle.delete(0, END)
                entTitle.insert(0, record[3])

                entTitleOfCourtesy.delete(0, END)
                entTitleOfCourtesy.insert(0, record[4])

                entBirthDate.delete(0, END)
                entBirthDate.insert(0, record[5])

                entHireDate.delete(0, END)
                entHireDate.insert(0, record[6])

                entAddress.delete(0, END)
                entAddress.insert(0, record[7])

                entCity.delete(0, END)
                entCity.insert(0, record[8])

                entRegion.delete(0, END)
                entRegion.insert(0, record[9])

                entPostalCode.delete(0, END)
                entPostalCode.insert(0, record[10])

                entCountry.delete(0, END)
                entCountry.insert(0, record[11])

                entHomePhone.delete(0, END)
                entHomePhone.insert(0, record[12])

                entExtension.delete(0, END)
                entExtension.insert(0, record[13])

                entNotes.delete(0, END)
                entNotes.insert(0, record[14])


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

        employeeForm.columnconfigure(0, weight=1)
        employeeForm.rowconfigure(0, weight=1)
        frameGrid.columnconfigure(0, weight=3)
        frameGrid.columnconfigure(1, weight=3)
        frameGrid.columnconfigure(2, weight=3)
        frameGrid.columnconfigure(3, weight=1)
        frameGrid.columnconfigure(4, weight=1)
        frameGrid.rowconfigure(1, weight=1)

        employeeForm.mainloop()
