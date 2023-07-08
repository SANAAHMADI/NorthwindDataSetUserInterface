import tkinter
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.messagebox import showinfo
# from PIL import Image, ImageTk
from Models.UserModel import User
from Models.CategoryModel import *
from BusinessLogic.CategoryBusinessLogic import CategoryBusinessLogic
from DataAccess.CategoryDataAccess import CategoryDataAccess
from tkcalendar import DateEntry
from datetime import datetime

picture_path = ""
class CategoryForm:

    def __init__(self, user: User):
        self.User = user
        self.GetData = []
        self.DeleteID = 0
        self.UpdateID=0
        self.Filename_Pic = ''



    def category_FormLoad(self):
        categoryForm = Tk()
        categoryForm.title('Category Register')
        categoryForm.geometry('800x460')

        # categoryForm.config(bg="LightBlue")
        positionRight = int(categoryForm.winfo_screenwidth() / 2 - 800 / 2)
        positionDown = int(categoryForm.winfo_screenheight() / 2 - 460 / 2)
        categoryForm.geometry("+{}+{}".format(positionRight, positionDown))
        categoryBusinessLogic = CategoryBusinessLogic()
        categoryBusinessLogic.getCategory()
        self.GetData = categoryBusinessLogic.AllDataCategory

        def checkValidation(*args):
            categoryName = entCategoryName.get()
            if categoryName is not None:
                if len(categoryName) > 15:
                    entCategoryName.delete(0, END)
                    showinfo('Error', 'Category name cannot except 15 characters.')
                elif not categoryName.isalpha():
                    entCategoryName.delete(0, END)
                    showinfo('Error', 'Category name can only contain letters.')


        def destroyForm():
            categoryForm.destroy()

        def clearText():
            entDescription.delete(0, END)
            entCategoryName.delete(0, END)
            # btnUploadPhoto.delete(0, END)

        def validate15(value):
            return len(value) <= 15

        def registerCategory():
            categoryName = entCategoryName.get()
            if not categoryName.isalpha():
                showinfo('Error', 'Category name can only contain letters.')
            else:
                categoryObject = Category(
                    categoryName=categoryName,
                    description=entDescription.get(),
                    picture=self.Filename_Pic
                )
                categoryBLLObject = CategoryBusinessLogic(categoryObject)
                categoryBLLObject.insertCategory()
                showinfo('Success', 'Category registered successfully.')
                for i in tree.get_children():
                    tree.delete(i)
                categoryBusinessLogic = CategoryBusinessLogic()
                categoryBusinessLogic.getCategory()
                self.GetData = categoryBusinessLogic.AllDataCategory

                for item in self.GetData:
                    tree.insert("", 'end', values=item)
                clearText()

                # ... existing code ...

        def updateCategory():
            categoryName = entCategoryName.get()
            if not categoryName.isalpha():
                showinfo('Error', 'Category name can only contain letters.')
            else:
                # with open(picture_path, 'rb') as f:
                #     picture_data = f.read()

                categoryObject = Category(
                    categoryName=categoryName,
                    description=entDescription.get(),
                    picture=self.Filename_Pic
                )
                categoryBLLObject = CategoryBusinessLogic(categoryObject)
                categoryBLLObject.updateCategory(self.UpdateID)
                showinfo('Success', 'Category updated successfully.')
                for i in tree.get_children():
                    tree.delete(i)
                categoryBusinessLogic = CategoryBusinessLogic()
                categoryBusinessLogic.getCategory()
                self.GetData = categoryBusinessLogic.AllDataCategory

                for item in self.GetData:
                    tree.insert("", 'end', values=item)
                clearText()
        # def registerCategory():
        #     categoryObject = Category(
        #         categoryName=entCategoryName.get()
        #         , description=entDescription.get()
        #         , picture=self.Filename_Pic
        #     )
        #     categoryBLLObject = CategoryBusinessLogic(categoryObject)
        #     categoryBLLObject.insertCategory()
        #     showinfo('Success', 'Category Registered successfully.')
        #
        #     for i in tree.get_children():
        #         tree.delete(i)
        #     categoryBusinessLogic = CategoryBusinessLogic()
        #     categoryBusinessLogic.getCategory()
        #     self.GetData = categoryBusinessLogic.AllDataCategory
        #
        #     for item in self.GetData:
        #         tree.insert("", 'end', values=item)
        #     clearText()
        #
        # def updateCategory():
        #     with open(picture_path, 'rb') as f:
        #         picture_data = f.read()
        #
        #     categoryObject = Category(
        #         # categoryID=self.UpdateID,
        #         categoryName=entCategoryName.get(),
        #         description=entDescription.get(),
        #         picture=picture_data
        #     )
        #     categoryBLLObject = CategoryBusinessLogic(categoryObject)
        #     categoryBLLObject.updateCategory(self.UpdateID)
        #     showinfo('Success', 'Category updated successfully.')
        #     for i in tree.get_children():
        #         tree.delete(i)
        #     categoryBusinessLogic = CategoryBusinessLogic()
        #     categoryBusinessLogic.getCategory()
        #     self.GetData = categoryBusinessLogic.AllDataCategory
        #
        #     for item in self.GetData:
        #         tree.insert("", 'end', values=item)
        #     clearText()

        def deleteCategory():
            categoryObject = CategoryIdDelete(
                categoryID=self.DeleteID
            )
            categoryBLLObject = CategoryBusinessLogic(categoryObject)
            categoryBLLObject.deleteCategory(self.DeleteID)
            showinfo('Success', 'Category deleted successfully.')
            for i in tree.get_children():
                tree.delete(i)
            categoryBusinessLogic = CategoryBusinessLogic()
            categoryBusinessLogic.getCategory()
            self.GetData = categoryBusinessLogic.AllDataCategory

            for item in self.GetData:
                tree.insert("", 'end', values=item)
            clearText()

        def upload_photo():
            global img
            f_types = [('Jpg Files', '*.jpg')]
            filename = filedialog.askopenfilename(filetypes=f_types)
            self.Filename_Pic = filename

        # endregion
        frame = LabelFrame(categoryForm, text="Field...", width=750, height=400, padx=10)
        frameButton = LabelFrame(categoryForm, text="Opertation ...", width=750, height=200, padx=10)
        frameGrid = LabelFrame(categoryForm, text="Data ...", width=750, height=290, padx=10, pady=10)

        frame.grid(row=0, column=0, padx=10)
        frameButton.grid(row=1, column=0, padx=10)
        frameGrid.grid(row=2, column=0, padx=10)

        lblCategoryName = Label(frame, text='Category Name: ')
        lblCategoryName.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        txtCategoryName = StringVar()
        txtCategoryName.trace('w', checkValidation)
        entCategoryName = ttk.Entry(frame, textvariable=txtCategoryName, width=40)
        entCategoryName.focus()
        entCategoryName.config(validate="key", validatecommand=(entCategoryName.register(validate15), "%P"))
        entCategoryName.grid(row=0, column=1, padx=10, pady=10, sticky='e')

        lblDescription = Label(frame, text='Description: ')
        lblDescription.grid(row=0, column=2, padx=10, pady=10, sticky='w')

        txtDescription = StringVar()
        entDescription = ttk.Entry(frame, textvariable=txtDescription, width=40)
        entDescription.grid(row=0, column=3, padx=10, pady=10, sticky='e')

        lblPicture = Label(frame, text='Picture: ')
        lblPicture.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        btnUploadPhoto = ttk.Button(frame, text='Upload Photo', command=upload_photo)
        btnUploadPhoto.grid(row=1, column=1, padx=10, pady=10, sticky='e')
        # txtPicture = StringVar()
        # entPicture = PhotoImage(frame, textvariable=txtPicture, width=40)
        # entPicture.grid(row=1, column=1, padx=10, pady=10, sticky='e')

        btnClearCategory = ttk.Button(frameButton, text='Clear', command=clearText, width=16)
        btnClearCategory.grid(row=0, column=0, padx=10, pady=10, sticky='e')

        btnInsertCategory = ttk.Button(frameButton, text='Insert',
                                       command=registerCategory, width=16)
        btnInsertCategory.grid(row=0, column=1, padx=10, pady=10, sticky='e')

        btnUpdateCategory = ttk.Button(frameButton, text='Update',
                                       command=updateCategory, width=16)
        btnUpdateCategory.grid(row=0, column=2, padx=10, pady=10, sticky='e')

        btnDeleteCategory = ttk.Button(frameButton, text='Delete', command=deleteCategory, width=16)
        btnDeleteCategory.grid(row=0, column=3, padx=10, pady=10, sticky='e')

        btnBackToMain = ttk.Button(frameButton, text='Close', command=destroyForm, width=14)
        btnBackToMain.grid(row=0, column=4, padx=10, pady=10, sticky='w')

        columns = ("categoryID", "categoryName", "description", "picture")
        tree = ttk.Treeview(frameGrid, columns=columns, show='headings')

        tree.heading("categoryID", text="CategoryID", anchor=W)
        tree.heading("categoryName", text="CategoryName", anchor=W)
        tree.heading("description", text="Description", anchor=W)
        tree.heading("picture", text="Picture", anchor=W)

        for item in self.GetData:
            tree.insert("", 'end', values=item)

        def item_selected(event):
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                record = item['values']

                entCategoryName.delete(0, END)
                entCategoryName.insert(0, record[1])

                entDescription.delete(0, END)
                entDescription.insert(0, record[2])

                # btnUploadPhoto.delete(0, END)
                # btnUploadPhoto.insert(0, record[3])

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

        categoryForm.columnconfigure(0, weight=1)
        categoryForm.rowconfigure(0, weight=1)
        frameGrid.columnconfigure(0, weight=3)
        frameGrid.columnconfigure(1, weight=3)
        frameGrid.columnconfigure(2, weight=3)
        frameGrid.columnconfigure(3, weight=1)
        frameGrid.columnconfigure(4, weight=1)
        frameGrid.rowconfigure(1, weight=1)

        categoryForm.mainloop()
