import sqlite3
from tkinter import *

from PIL import ImageTk

root = Tk()
root.title("student management system")
root.geometry("800x600")
root.resizable(False, False)

bg1 = ImageTk.PhotoImage(file="dashboard1.JPG")
bg1_label = Label(root, image=bg1)
bg1_label.place(x=0, y=0)

# connect to database button
db = sqlite3.connect("students.db")

# create cursor
rep1 = db.cursor()

# create table
'''rep1.execute("""CREATE TABLE addresses (
          first_name text,
          last_name text,
          address text,
          city text,
          state text,
          school text,
         department text   )""")
'''
#navigation to dashboard
def backToDashboard():
    root.destroy()
    from StudentDashaboard import window

    import login
    print("dashboard imported")


# database submit function

def submit():
    # connect to database button
    db = sqlite3.connect("students.db")

    # create cursor
    rep1 = db.cursor()

    rep1.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :school, :department)",
                 {
                     'f_name': f_name.get(),
                     'l_name': l_name.get(),
                     'address': address.get(),
                     'city': city.get(),
                     'state': state.get(),
                     'school': school.get(),
                     'department': department.get()
                 }
                 )

    # commit changes
    db.commit()

    # close db connection
    db.close()

    # clear the textboxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    school.delete(0, END)
    department.delete(0, END)


# text box area
notice = Label(root, text="".upper(), font=20)
notice.grid(row=0, column=0, pady=10)

notice = Label(root, text="fill in the student record".upper(), font=40)
notice.grid(row=1, column=1, pady=150)
f_name = Entry(root, width=30, )
f_name.grid(row=2, column=1)
l_name = Entry(root, width=30)
l_name.grid(row=3, column=1, )
address = Entry(root, width=30)
address.grid(row=4, column=1)
city = Entry(root, width=30)
city.grid(row=5, column=1)
state = Entry(root, width=30)
state.grid(row=6, column=1)
school = Entry(root, width=30)
school.grid(row=7, column=1)
department = Entry(root, width=30)
department.grid(row=8, column=1)

# text label area

f_name_label = Label(root, text="First name".upper(), background="green", foreground="white")
f_name_label.grid(row=2, column=0)
l_name_label = Label(root, text="Last name".upper(), background="green", foreground="white")
l_name_label.grid(row=3, column=0)
address_label = Label(root, text="Address".upper(), background="green", foreground="white")
address_label.grid(row=4, column=0)
city_label = Label(root, text="City".upper(), background="green", foreground="white")
city_label.grid(row=5, column=0)
state_label = Label(root, text="State".upper(), background="green", foreground="white")
state_label.grid(row=6, column=0)
school_label = Label(root, text="School".upper(), background="green", foreground="white")
school_label.grid(row=7, column=0)
department_label = Label(root, text="department".upper(), background="green", foreground="white")
department_label.grid(row=8, column=0)

# submit button

submit_button = Button(root, text="submit record".upper(), command=submit,background="green", foreground="white")
submit_button.grid(row=9, column=0, columnspan=1, pady=10, padx=10, ipadx=50)

#back to dashboard

dashboard = Button (root, text="go back to dashboard".upper(),command=backToDashboard,background="green", foreground="white")
dashboard.grid(row=9, column=1, columnspan=1, pady=10, padx=10, ipadx=50)

# commit changes
db.commit()

# close db connection
db.close()

root.mainloop()
