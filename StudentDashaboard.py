from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter
import sqlite3
from PIL import ImageTk
import sqlite3


dashboard = tk.Tk()

dashboard.geometry("1280x700")

dashboard.title("CoDEL student management system")

dashboard.resizable(False, False)

bg = ImageTk.PhotoImage(file="dashboard.JPG")
bg_label = Label(dashboard, image=bg)
bg_label.place(x=0, y=0)




def fetch_data():
    connection = sqlite3.connect('student.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM addresses")
    data = cursor.fetchall()  # Fetch all records

    connection.close()

    students_tree.delete(*students_tree.get_children())  # Clear previous entries

    if data:
        for row in data:
            students_tree.insert('', 'end', values=row)
    else:
        students_tree.insert('', 'end', values=("No data found",))



columns = ("ID", "matric number", "first name", "last name", "address", "city", "state", "school", "department")  # Adjust column names
students_tree = ttk.Treeview(dashboard, columns=columns, show="headings")

for col in columns:
    students_tree.heading(col, text=col)
    students_tree.column(col, width=100)  # Adjust column width

students_tree.grid(row=3, column=1, columnspan=5, rowspan=8)



#A function to add new students
def addStudent():
    dashboard.destroy()
    import StudentMS as st


    print("add function working")


headerCover = Label(dashboard, text="     ".upper(), font=30)
headerCover.grid(row=0, column=0, padx=20, pady=60, rowspan=2)

header = Label(dashboard, text="select desired operation".upper(), font=30, background="white", foreground="black")
header.grid(row=2, column=0, padx=20, pady=60)

StudentRecords = Button(dashboard, text="show all records".upper(), font=30, background="green", foreground="black",command=fetch_data)
StudentRecords.grid(row=3, column=0, pady=20)

StudentAdd = Button(dashboard, text="add student".upper(), font=30, command=addStudent, background="green",
                    foreground="black")
StudentAdd.grid(row=4, column=0, pady=20)

StudentRemove = Button(dashboard, text="remove student".upper(), font=30, background="green", foreground="black")
StudentRemove.grid(row=5, column=0, pady=20)

StudentEdit = Button(dashboard, text="edit student".upper(), font=30, background="green", foreground="black")
StudentEdit.grid(row=6, column=0, pady=20)





dashboard.mainloop()
