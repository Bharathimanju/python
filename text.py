import tkinter as tk
import sqlite3
from tkinter import ttk, messagebox




root = tk.Tk()
root.title("management")

connection = sqlite3.connect("management.db")

TABLE_NAME = "Management_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"

connection.execute("CREATE TABLE IF NOT EXISTS " + TABLE_NAME +
                   "(" + STUDENT_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   STUDENT_NAME + " TEXT, " + STUDENT_COLLEGE + " TEXT, " +
                   STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " INTEGER);")

label = tk.Label(root, text="student management system", fg="red", font=("sylfaen", 18, "bold"))
label.place(x=500, y=5)


class student:
    student_name = ""
    college_name = ""
    phone_number = 0
    address = ""

    def _init_(self, student_name, college_name, phone_number, address):
        self.student_name = student_name
        self.college_name = college_name
        self.phone_number = phone_number
        self.address = address


namelabel = tk.Label(root, text="Enter Your Name", font=("cabrian", 20))
namelabel.place(x=300, y=80)
collegelabel = tk.Label(root, text="Enter Your college", font=("cabrian", 20))
collegelabel.place(x=300, y=140)
phonelabel = tk.Label(root, text="Enter Your phone", font=("cabrian", 20))
phonelabel.place(x=300, y=200)
addresslabel = tk.Label(root, text="Enter Your address", font=("cabrian", 20))
addresslabel.place(x=300, y=260)

nameEntry = tk.Entry(root, width=30)
nameEntry.place(x=700, y=80)
collegeEntry = tk.Entry(root, width=30)
collegeEntry.place(x=700, y=140)
phoneEntry = tk.Entry(root, width=30)
phoneEntry.place(x=700, y=200)
addressEntry = tk.Entry(root, width=30)
addressEntry.place(x=700, y=260)


def takeNameInput():
    global nameEntry, collegeEntry, phoneEntry, addressEntry
    global TABLE_NAME, STUDENT_NAME, STUDENT_COLLEGE, STUDENT_ADDRESS, STUDENT_PHONE
    username = nameEntry.get()
    nameEntry.delete(0, tk.END)
    collegename = collegeEntry.get()
    collegeEntry.delete(0, tk.END)
    phone = int(phoneEntry.get())
    phoneEntry.delete(0, tk.END)
    address = addressEntry.get()
    addressEntry.delete(0, tk.END)

    connection.execute("INSERT INTO " + TABLE_NAME + "(" + STUDENT_NAME + "," + STUDENT_COLLEGE + "," +
                       STUDENT_ADDRESS + "," + STUDENT_PHONE + ") VALUES ('" + username + "','" + collegename +
                       "','" + address + "','" + str(phone) + "');")
    connection.commit()
    messagebox.showinfo("success", "data saved successfully")


def destroyRootWindow():
    secondWindow = tk.Tk()
    secondWindow.title("Display result")
    label = tk.Label(secondWindow, text="student management system", font=("sylfaen", 30))
    label.pack()
    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("one", "two", "three", "four")
    tree.heading("one", text="student name")
    tree.heading("two", text="college name")
    tree.heading("three", text="address")
    tree.heading("four", text="phone number")
    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + ";")
    i = 0
    for row in cursor:
        tree.insert("", i, text="student" + str(row[0]),
                    values=(row[1], row[2], row[3], row[4]))
        i = i + 1
    tree.pack()
    secondWindow.mainloop()


button = tk.Button(root, text="Take input", command=lambda: takeNameInput())
button.place(x=400, y=400 )

displaybutton = tk.Button(root, text="Display result", command=lambda: destroyRootWindow())
displaybutton.place(x=670, y=400)

root.mainloop()
