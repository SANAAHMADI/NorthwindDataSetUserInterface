from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from Models.UserModel import User
from BusinessLogic.UserBusinessLogic import UserBusinessLogic
from UI.MainForm import MainForm
from UI.RegisterForm import RegisterUserForm


def __init__(self, user: User):
    self.User = user
    self.GetData = []
    self.DeleteID = 0
    self.UpdateID = 0

def loginMethod():
    username = txtUserName.get()
    password = txtPassword.get()
    userObject = User(username=username, password=password)
    if username is not None and password is not None:
        userBLLObject = UserBusinessLogic(user=userObject)
        userBLLObject.getUserInfo()
        if userObject.FirstName is not None and userObject.LastName is not None:
            loginForm.destroy()
            mainFormObject = MainForm(userObject)
            mainFormObject.mainFormClass_FormLoad()
        else:
            msg.showinfo('Info','UserName or Password is invalid!!!')

def destroyForm():
    loginForm.destroy()


def userRegisteration_FormLoad():
    registerUserObject = RegisterUserForm(User)
    registerUserObject.registerUser_FormLoad()

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


# Start Create Main Login Form
loginForm = Tk()
loginForm.title('Login Form')
loginForm.geometry('400x160')
loginForm.resizable(0, 0)
loginForm.config(bg="#C5CAE9")
positionRight = int(loginForm.winfo_screenwidth() / 2 - 400 / 2)
positionDown = int(loginForm.winfo_screenheight() / 2 - 340 / 2)
loginForm.geometry("+{}+{}".format(positionRight, positionDown))
# End Create

# Start Create Control
# Start Username Control
lblUserName = ttk.Label(loginForm, text='Username: ')
lblUserName.grid(row=0, column=0, padx=10, pady=10, sticky='w')

txtUserName = StringVar()
txtUserName.trace('w', checkValidation)
entUserName = ttk.Entry(loginForm, textvariable=txtUserName, width=40)
entUserName.focus()
entUserName.grid(row=0, column=1, padx=10, pady=10, sticky='e')
# End Username Control

# Start Password Control
lblPassword = ttk.Label(loginForm, text='Password: ')
lblPassword.grid(row=1, column=0, padx=10, pady=10, sticky='w')

txtPassword = StringVar()
txtPassword.trace('w', checkValidation)
entPassword = ttk.Entry(loginForm, show='*', textvariable=txtPassword, width=40)
entPassword.grid(row=1, column=1, padx=10, pady=10, sticky='e')
# End Password Control

# Start Button Control
btnLogin = ttk.Button(loginForm, text='Login', width=16, command=loginMethod)
btnLogin.grid(row=2, column=1, padx=20, pady=20, sticky='ne')

btnQuit = ttk.Button(loginForm, text='SignIn', width=16, command=userRegisteration_FormLoad)
btnQuit.grid(row=2, column=1, padx=20, pady=20, sticky='nw')
# End Button Control
# End Create Control

loginForm.mainloop()
