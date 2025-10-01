import os
import sqlite3
from tabulate import tabulate
from datetime import datetime

home_dir = os.path.dirname(os.path.abspath(__file__))
db = os.path.join(home_dir, "data.db")

cnxn = sqlite3.connect(db)
gamo = cnxn.cursor()

gamo.execute("""CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,   -- unique ID
    title TEXT NOT NULL,                    -- description of expense
    amount REAL NOT NULL,                   -- expense amount
    expense_date TEXT NOT NULL,             -- actual date of expense
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")
cnxn.commit()

headers = ["ID", "Title", "Amount", "Expense Date", "Recorded At"]

def record():
    try:
        a = input("Description of the payment: ")
        b = int(input("Enter amount: "))
        while True:
            asdasd = input("Enter date (YYYY-MM-DD): ")
            try:
                c = datetime.strptime(asdasd, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Invalid format entered.")
        gamo.execute("insert into expenses (title, amount, expense_date) values (?,?,?)", (a,b,c))
        cnxn.commit()
        print("Entry recorded successfuly.")
        mm()
    except Exception as e:
        print("Error Occured: ", e)
        mm()

def view():
    try:
        gamo.execute("select * from expenses")
        u = gamo.fetchall()
        print(tabulate(u, headers=headers, tablefmt="fancy_grid"))
        mm()
    except Exception as e:
        print("Error Occured: ", e)
        mm()

def delete():
    try:
        x = int(input("Enter Transaction ID to delete: "))
        gamo.execute("select * from expenses where id = ?", (x,))
        u = gamo.fetchall()
        if u is None:
            print("Invalid ID.")
            mm()
        else:
            gamo.execute("delete from expenses where id = ?", (x,))
            cnxn.commit()
            print("Data deleted successfuly.")
            mm()
    except Exception as e:
        print("Error Occured: ", e)
        mm()

def update():
    try:
        x = int(input("Enter Transaction ID to update: "))
        gamo.execute("Select * from expenses where id = ?", (x,))
        u = gamo.fetchall()
        if u is None:
            print("Invalid ID.")
            mm()
        else:
            a = input("Enter new titile: ")
            b = int(input("Enter new amount: "))
            gamo.execute("update expenses set title = ?, amount = ? where id = ?", (a,b,x))
            cnxn.commit()
            print("Data updated successfuly.")
            mm()
    except Exception as e:
        print("Error Occured: ", e)
        mm()

def mm():
    try:
        print("""Choose your option: 
[1] Add Expense
[2] View Expenses
[3] Delete Expense
[4] Update Expense""")
        x = int(input("Enter your choice: "))
        if x == 1:
            record()
        elif x == 2:
            view()
        elif x == 3:
            delete()
        elif x == 4:
            update()
        else:
            print("Invalid choice. Try Again.")
    except Exception as e:
        print("Error Occured: ", e)
        mm()

mm()