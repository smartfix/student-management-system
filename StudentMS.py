import sqlite3
from tkinter import *
from tkinter import messagebox


from PIL import ImageTk

import StudentDashaboard

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

rep1.execute("""CREATE TABLE IF NOT EXISTS addresses (
          matric_number text,
          first_name text,
          last_name text,
          address text,
          city text,
          state text,
          school text,
         department text   )""")
#navigation to dashboard
def backToDashboard():
    root.destroy()
    print("dashboard imported")


# database submit function

def submit():
    # connect to database button
    db = sqlite3.connect("students.db")

    # create cursor
    rep1 = db.cursor()

    rep1.execute("INSERT INTO addresses VALUES (:m_number,:f_name, :l_name, :address, :city, :state, :school, :department)",
                 {
                     'm_number': m_number.get(),
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
    m_number.delete(0, END)
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    school.delete(0, END)
    department.delete(0, END)

    #notification of record submition
    messagebox.showinfo("Student record ".upper(), "student record added to the database")



# text box area
notice = Label(root, text="".upper(), font=10)
notice.grid(row=0, column=0, pady=10)

notice = Label(root, text="fill in the student record".upper(), font=30)
notice.grid(row=1, column=1, pady=100)
m_number = Entry(root, width=30)
m_number.grid(row=2, column=1)
f_name = Entry(root, width=30, )
f_name.grid(row=3, column=1)
l_name = Entry(root, width=30)
l_name.grid(row=4, column=1, )
address = Entry(root, width=30)
address.grid(row=5, column=1)
city = Entry(root, width=30)
city.grid(row=6, column=1)
state = Entry(root, width=30)
state.grid(row=7, column=1)
school = Entry(root, width=30)
school.grid(row=8, column=1)
department = Entry(root, width=30)
department.grid(row=9, column=1)

# text label area
m_number_label = Label(root, text="matric number".upper(), background="green", foreground="white",font=15 )
m_number_label.grid(row=2, column=0)
f_name_label = Label(root, text="First name".upper(), background="green", foreground="white",font=15)
f_name_label.grid(row=3, column=0)
l_name_label = Label(root, text="Last name".upper(), background="green", foreground="white",font=15)
l_name_label.grid(row=4, column=0)
address_label = Label(root, text="Address".upper(), background="green", foreground="white",font=15)
address_label.grid(row=5, column=0)
city_label = Label(root, text="City".upper(), background="green", foreground="white",font=15)
city_label.grid(row=6, column=0)
state_label = Label(root, text="State".upper(), background="green", foreground="white",font=15)
state_label.grid(row=7, column=0)
school_label = Label(root, text="School".upper(), background="green", foreground="white",font=15)
school_label.grid(row=8, column=0)
department_label = Label(root, text="department".upper(), background="green", foreground="white",font=15)
department_label.grid(row=9, column=0)

# submit button

submit_button = Button(root, text="submit record".upper(), command=submit,background="green", foreground="white", font=30)
submit_button.grid(row=10, column=0, columnspan=2, rowspan=2, pady=10, padx=10, ipadx=50 )



# commit changes
db.commit()

# close db connection
db.close()

root.mainloop()
