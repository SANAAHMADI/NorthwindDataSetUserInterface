import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from Models.UserModel import User
from Models.RegisterModel import *
from BusinessLogic.RegisterBusinessLogic import RegisterUserBusinessLogic

from tkcalendar import DateEntry
from datetime import datetime


class RegisterUserForm:

    def __init__(self, user: User):
        self.User = user
        self.GetData = []
        self.DeleteID = 0
        self.UpdateID=0

    def registerUser_FormLoad(self):
        registerUserForm = Tk()
        registerUserForm.title('User Registeration')
        registerUserForm.geometry('800x520')
        # registerUserForm.config(bg="LightBlue")
        positionRight = int(registerUserForm.winfo_screenwidth() / 2 - 800 / 2)
        positionDown = int(registerUserForm.winfo_screenheight() / 2 - 520 / 2)
        registerUserForm.geometry("+{}+{}".format(positionRight, positionDown))
        # registerBusinessLogic = RegisterUserBusinessLogic()
        # registerBusinessLogic.getEmployee()
        # self.GetData = registerBusinessLogic.AllDataEmployee

        def destroyForm():
            registerUserForm.destroy()

        def clearText():
            # txtIsAdmin.delete(0, END)
            entLastName.delete(0, END)
            entPassword.delete(0, END)
            entFirstName.delete(0, END)
            entUserName.delete(0, END)

        def checkValidation(*args):
            username = txtUserName.get()
            password = txtPassword.get()
            if username is not None and password is not None:
                if len(username) > 20:
                    txtUserName.set(txtUserName.get()[:len(txtUserName.get()) - 1])
                if not username.isalnum():
                    txtUserName.set(txtUserName.get()[:len(txtUserName.get()) - 1])
                if len(password) > 30:
                    txtPassword.set(txtPassword.get()[:len(txtPassword.get()) - 1])
                    
        def registerRegisterUser():
            registerUserObject = RegisterUser(
                 userName=entUserName.get()
                ,password=entPassword.get()
                ,firstName=entFirstName.get()
                ,lastName=entLastName.get()
                ,isAdmin=txtIsAdmin.get() )
            registerUserBLLObject = RegisterUserBusinessLogic(registerUserObject)
            registerUserBLLObject.insertRegisterUserObject()
            showinfo('Success', 'New User Registered successfully.')
            clearText()
            # for i in tree.get_children():
            #     tree.delete(i)
            # employeeBusinessLogic = RegisterUserBusinessLogic()
            # employeeBusinessLogic.getEmployee()
            # self.GetData = employeeBusinessLogic.AllDataEmployee

            # for item in self.GetData:
            #     tree.insert("", 'end', values=item)


        # def updateEmployee():
        #     employeeObject = Employee(
        #         firstName=entFirstName.get())
        #
        #     employeeBusinessLogic = EmployeeBusinessLogic(employeeObject)
        #     employeeBusinessLogic.updateEmployee(self.UpdateID)
        #     showinfo('Success', 'Employee updated successfully.')
        #
        #     for i in tree.get_children():
        #         tree.delete(i)
        #     employeeBusinessLogic = EmployeeBusinessLogic()
        #     employeeBusinessLogic.getEmployee()
        #     self.GetData = employeeBusinessLogic.AllDataEmployee
        #
        #     for item in self.GetData:
        #         tree.insert("", 'end', values=item)
        #
        #     clearText()

        # def deleteEmployee():
        #     employeeObject = EmloyeeIdDelete(
        #         emloyeeID=self.DeleteID)
        #     employeeBusinessLogic = EmployeeBusinessLogic(employeeObject)
        #     employeeBusinessLogic.deleteEmployee(self.DeleteID)
        #     showinfo('Success', 'Employee deleted successfully.')
        #     for i in tree.get_children():
        #         tree.delete(i)
        #     employeeBusinessLogic = EmployeeBusinessLogic()
        #     employeeBusinessLogic.getEmployee()
        #     self.GetData = employeeBusinessLogic.AllDataEmployee
        #
        #     for item in self.GetData:
        #         tree.insert("", 'end', values=item)
        #     clearText()

        # endregion

        frame = LabelFrame(registerUserForm, text="Field...", width=750, height=400, padx=10)
        frameButton = LabelFrame(registerUserForm, text="Opertation ...", width=750, height=200, padx=10)
        # frameGrid = LabelFrame(registerUserForm, text="Data ...", width=750, height=290, padx=10, pady=10)

        frame.grid(row=0, column=0, padx=10)
        frameButton.grid(row=1, column=0, padx=10)
        # frameGrid.grid(row=2, column=0, padx=10)

        lblUserName = ttk.Label(frame, text='Username: ')
        lblUserName.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        txtUserName = StringVar()
        txtUserName.trace('w', checkValidation)
        entUserName = ttk.Entry(frame, textvariable=txtUserName, width=40)
        entUserName.focus()
        entUserName.grid(row=0, column=1, padx=10, pady=10, sticky='e')
        # End Username Control

        # Start Password Control
        lblPassword = ttk.Label(frame, text='Password: ')
        lblPassword.grid(row=0, column=2, padx=10, pady=10, sticky='w')

        txtPassword = StringVar()
        txtPassword.trace('w', checkValidation)
        entPassword = ttk.Entry(frame, show='*', textvariable=txtPassword, width=40)
        entPassword.grid(row=0, column=3, padx=10, pady=10, sticky='e')

        lblFirstName = Label(frame, text='FirstName: ')

        lblFirstName.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        txtFirstName = StringVar()
        entFirstName = ttk.Entry(frame, textvariable=txtFirstName, width=40)
        entFirstName.focus()
        entFirstName.grid(row=1, column=1, padx=10, pady=10, sticky='e')

        lblLastName = Label(frame, text='LastName: ')
        lblLastName.grid(row=1, column=2, padx=10, pady=10, sticky='w')

        txtLastName = StringVar()
        entLastName = ttk.Entry(frame, textvariable=txtLastName, width=40)
        entLastName.focus()
        entLastName.grid(row=1, column=3, padx=10, pady=10, sticky='e')

        lblisAdmin = Label(frame, text='isAdmin: ')
        lblisAdmin.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        txtIsAdmin = StringVar()
        entIsAdmin = ttk.Radiobutton(frame, value="txtIsAdmin", variable=txtIsAdmin, width=40)
        entIsAdmin.focus()
        entIsAdmin.grid(row=2, column=1, padx=10, pady=10, sticky='e')


        btnClearRegisterUser = ttk.Button(frameButton, text='Clear', command=clearText, width=16)
        btnClearRegisterUser.grid(row=3, column=2, padx=10, pady=10, sticky='e')

        btnInsertRegisterUser = ttk.Button(frameButton, text='Insert', command=registerRegisterUser, width=16)
        btnInsertRegisterUser.grid(row=3, column=3, padx=10, pady=10, sticky='e')

        btnBackToMain = ttk.Button(frameButton, text='Close', command=destroyForm, width=14)
        btnBackToMain.grid(row=3, column=4, padx=10, pady=10, sticky='w')

        registerUserForm.mainloop()

        #
        # columns = ("employeeID")
        # tree = ttk.Treeview(frameGrid, columns=columns, show='headings')
        #
        # tree.heading("employeeID", text="EmployeeID", anchor=W)
        # tree.heading("firstName", text="FirstName", anchor=W)
        # tree.heading("lastName", text="lastName", anchor=W)
        # tree.heading("title", text="title", anchor=W)
        # tree.heading("titleOfCourtesy", text="titleOfCourtesy", anchor=W)
        #
        # for item in self.GetData:
        #     tree.insert("", 'end', values=item)
        #
        # def item_selected(event):
        #     for selected_item in tree.selection():
        #         item = tree.item(selected_item)
        #         record = item['values']
        #
        #         entFirstName.delete(0, END)
        #         entFirstName.insert(0, record[1])
        #
        #         entLastName.delete(0, END)
        #         entLastName.insert(0, record[2])
        #
        #         entTitle.delete(0, END)
        #         entTitle.insert(0, record[3])
        #
        #         entTitleOfCourtesy.delete(0, END)
        #         entTitleOfCourtesy.insert(0, record[4])
        #
        #         entBirthDate.delete(0, END)
        #         entBirthDate.insert(0, record[5])
        #
        #         entHireDate.delete(0, END)
        #         entHireDate.insert(0, record[6])
        #
        #
        #         self.DeleteID = record[0]
        #         self.UpdateID = record[0]
        #
        # tree.bind('<<TreeviewSelect>>', item_selected)
        #
        # # tree.grid(row=0, column=0, sticky='nsew')
        #
        # treeXScroll = ttk.Scrollbar(frameGrid, orient=HORIZONTAL)
        # treeXScroll.configure(command=tree.xview)
        # tree.configure(xscrollcommand=treeXScroll.set)
        #
        # frameGrid.grid(column=0, row=3, sticky=(N, S, E, W))
        # tree.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
        # treeXScroll.grid(column=0, row=2, columnspan=3, sticky=W + E)
        #
        # registerUserForm.columnconfigure(0, weight=1)
        # registerUserForm.rowconfigure(0, weight=1)
        # frameGrid.columnconfigure(0, weight=3)
        # frameGrid.columnconfigure(1, weight=3)
        # frameGrid.columnconfigure(2, weight=3)
        # frameGrid.columnconfigure(3, weight=1)
        # frameGrid.columnconfigure(4, weight=1)
        # frameGrid.rowconfigure(1, weight=1)


