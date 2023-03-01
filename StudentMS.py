from tkinter import *
from tkinter import messagebox
from PIL import ImageTk


root = Tk()
root.title("student management system")
root.geometry("1280x700")
root.resizable(False,False)

#connect to database button
connectDatabase = Button(root, text="connect to database")
connectDatabase.grid(row=0,column=1, padx=10, pady=5)

#database image
dbimage = PhotoImage(file="dbimage.png")
dblabel = Label(root, image=dbimage)
dblabel.grid(row=0, column=0, padx=10,pady=5)

#fetched details frame
resultFrame = Frame(root) #highlightbackground="cornflowerblue", highlightthickness=10)
resultFrame.place(x=600,y=20)

#database entry label
resulttitle6 = Label(resultFrame, text="matric-no" , font=("times new roman",15,"bold"))
resulttitle6.grid(row=0,column=0, padx=20)
resulttitle1 = Label(resultFrame, text="firstname", font=("times new roman",15,"bold"))
resulttitle1.grid(row=0,column=1, padx=20)
resulttitle2 = Label(resultFrame, text="lastname", font=("times new roman",15,"bold"))
resulttitle2.grid(row=0,column=2, padx=20)
resulttitle3 = Label(resultFrame, text="gender" , font=("times new roman",15,"bold"))
resulttitle3.grid(row=0,column=3, padx=20)
resulttitle4 = Label(resultFrame, text="faculty" , font=("times new roman",15,"bold"))
resulttitle4.grid(row=0,column=4,padx=20)
resulttitle5 = Label(resultFrame, text="course" , font=("times new roman",15,"bold"))
resulttitle5.grid(row=0,column=5, padx=3)



#action button frame
action = Frame(root) #highlightbackground="cornflowerblue", highlightthickness=10)
action.place(x=100,y=150)

addButton = Button(action, text="search database", font=("times new roman",15,"bold"))
addButton.pack(pady=20,padx=30)
addButton = Button(action, text="add student", font=("times new roman",15,"bold"))
addButton.pack(pady=20,padx=30)
addButton = Button(action, text="update student", font=("times new roman",15,"bold"))
addButton.pack(pady=20,padx=30)
addButton = Button(action, text="remove student", font=("times new roman",15,"bold"))
addButton.pack(pady=20,padx=30)
addButton = Button(action, text="list all students", font=("times new roman",15,"bold"))
addButton.pack(pady=20,padx=30)






root.mainloop()