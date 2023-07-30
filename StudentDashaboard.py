
from tkinter import *
from PIL import ImageTk

dashboard = Tk()

dashboard.geometry("800x600")

dashboard.title("CoDEL student management system")

dashboard.resizable(False , False)


bg = ImageTk.PhotoImage(file="dashboard.JPG")
bg_label = Label(dashboard,image=bg)
bg_label.place(x=0,y=0)





def addStudent():
    dashboard.destroy()
    import StudentMS
    print("add function working")

headerCover = Label(dashboard, text="     ".upper(), font=30 )
headerCover.grid(row=0, column=0, padx=20, pady=60 , rowspan=2)

header = Label(dashboard, text="select desired operation".upper(), font=30 ,background="white",  foreground="black"  )
header.grid(row=2, column=0, padx=20, pady=60)

StudentRecords = Button(dashboard, text="show all records".upper(), font=30, background="green", foreground="black")
StudentRecords.grid(row=3, column=0, pady=20)

StudentAdd = Button(dashboard, text="add student".upper(), font=30, command=addStudent , background="green", foreground="black")
StudentAdd.grid(row=4, column=0, pady=20)

StudentRemove = Button(dashboard, text="remove student".upper(),font=30 , background="green", foreground="black")
StudentRemove.grid(row=5, column=0, pady=20)

StudentEdit = Button(dashboard, text="edit student".upper(), font=30 , background="green", foreground="black")
StudentEdit.grid(row=6, column=0, pady=20)


dashboard.mainloop()