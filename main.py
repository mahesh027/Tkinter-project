from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Employee Management System")
root.geometry("1920x1080+0+0")
root.config(bg="#2c3e50") #can use color value as red,blue...instead of hexa value
root.state("zoomed")

name = StringVar()
age = StringVar()
doj = StringVar()
gender = StringVar()
email = StringVar()
contact = StringVar()

#Entries Frame
entries_frame=Frame(root,bg="#535c68")
entries_frame.pack(side=TOP,fill=X)
title=Label(entries_frame,text="Employee Management System",font=("Calibri",18,"bold"),bg="#535c68",fg="white")
title.grid(row=0,columnspan=2,padx=10,pady=20)

lblName=Label(entries_frame,text="Name",font=("Calibri",16),bg="#535c68",fg="white")
lblName.grid(row=1,column=0,padx=10,pady=10,sticky="w")
txtName=Entry(entries_frame,textvariable=name,font=("Calibri",16),width=30)
txtName.grid(row=1,column=1,padx=10,pady=10,sticky="w")

lblAge=Label(entries_frame,text="Age",font=("Calibri",16),bg="#535c68",fg="white")
lblAge.grid(row=1,column=2,padx=10,pady=10,sticky="w")
txtAge=Entry(entries_frame,textvariable=age,font=("Calibri",16),width=30)
txtAge.grid(row=1,column=3,padx=10,pady=10,sticky="w")

lblDoj=Label(entries_frame,text="D.O.J",font=("Calibri",16),bg="#535c68",fg="white")
lblDoj.grid(row=2,column=0,padx=10,pady=10,sticky="w")
txtDoj=Entry(entries_frame,textvariable=doj,font=("Calibri",16),width=30)
txtDoj.grid(row=2,column=1,padx=10,pady=10,sticky="w")

lblEmail=Label(entries_frame,text="Email",font=("Calibri",16),bg="#535c68",fg="white")
lblEmail.grid(row=2,column=2,padx=10,pady=10,sticky="w")
txtEmail=Entry(entries_frame,textvariable=email,font=("Calibri",16),width=30)
txtEmail.grid(row=2,column=3,padx=10,pady=10,sticky="w")

lblGender=Label(entries_frame,text="Gender",font=("Calibri",16),bg="#535c68",fg="white")
lblGender.grid(row=3,column=0,padx=10,pady=10,sticky="w")
comboGender=ttk.Combobox(entries_frame,font=("Calibri",16),width=20,state="readonly")
comboGender['values']=("Male","Female")
comboGender.grid(row=3,column=1,padx=10,pady=10,sticky="w")

lblContact = Label(entries_frame, text="Contact No", font=("Calibri", 16), bg="#535c68", fg="white")
lblContact.grid(row=3, column=2, padx=10, pady=10, sticky="w")
txtContact = Entry(entries_frame, textvariable=contact, font=("Calibri", 16), width=30)
txtContact.grid(row=3, column=3, padx=10, sticky="w")

lblAddress = Label(entries_frame, text="Address", font=("Calibri", 16), bg="#535c68", fg="white")
lblAddress.grid(row=4, column=0, padx=10, pady=10, sticky="w")

txtAddress=Text(entries_frame,width=85,height=5,font=("Calibri",16))
txtAddress.grid(row=5,column=0,columnspan=4,padx=10,sticky="w")

def add_employee():
    pass
def update_employee():
    pass
def delete_employee():
    pass
def clearAll():
    pass
btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnAdd = Button(btn_frame, command=add_employee, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#16a085", bd=0).grid(row=0, column=0)
btnEdit = Button(btn_frame, command=update_employee, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="#2980b9",
                 bd=0).grid(row=0, column=1, padx=10)
btnDelete = Button(btn_frame, command=delete_employee, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#c0392b",
                   bd=0).grid(row=0, column=2, padx=10)
btnClear = Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                  bg="#f39c12",
                  bd=0).grid(row=0, column=3, padx=10)


root.mainloop()
