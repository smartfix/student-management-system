
from tkinter import *

from PIL import ImageTk
from tkinter import messagebox
from customtkinter import *



def login():
    if usernameEntry.get() == "" or passwordEntry.get() == "":
        messagebox.showerror("invalid password", "fields can not be empty.")

    elif usernameEntry.get() == "admin" and passwordEntry.get() =="12345":
        messagebox.showinfo("login", "your login is sucessfull")

        window.destroy()
        import StudentMS

    else:
        messagebox.showerror("Error", "please enter correct credencials")



window = Tk()

window.geometry("1280x700")

window.title("CoDEL student management system")

window.resizable(False , False)

bg = ImageTk.PhotoImage(file="double.JPG")
bg_label = Label(window,image=bg)
bg_label.place(x=0,y=0)

loginframe = Frame(window,bg="")
loginframe.place(x=400,y=200)

logoImage = ImageTk.PhotoImage(file="single.JPG")
bg_label = Label(loginframe, image=logoImage)
bg_label.grid(row=0,column=0, columnspan=2,pady=10)

usernameImage = PhotoImage(file="user.png")
usernameLabel = Label(loginframe, image=usernameImage, text="username",compound=LEFT,
                      font=("times new roman",15,"bold"))
usernameLabel.grid(row=1,column=0,pady=10,padx=5)

usernameEntry = Entry(loginframe, font=("times new roman",10,"bold"))
usernameEntry.grid(row=1,column=1,pady=10,padx=5)


passwordImage = PhotoImage(file="password.png")
passwordLabel = Label(loginframe, image=passwordImage, text="password" , compound=LEFT,font=("times new roman",15,"bold"))
passwordLabel.grid(row=2,column=0)


passwordEntry = Entry(loginframe, font=("times new roman",10,"bold"))
passwordEntry.grid(row=2,column=1)

loginButton = Button(loginframe , text="login" , font=("times new roman",12,"italic"), width=10, fg="white", bg="cornflowerblue" , cursor="hand2", command=login)
loginButton.grid(row=3,column=1, pady=10,)

#registerButton = Button(loginframe, text="register" ) font=("times new roman",10,"italic"))
#registerButton.grid(row=3,column=0)


window.mainloop()

