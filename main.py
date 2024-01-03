import sys
import time
import mysql.connector as mydb
import pandas

# SCHOOL LIBRARY MANAGEMNET SYSTEM

"""
THEORY
cursors use 
"""

db = mydb.connect(host="localhost",
                  user="root",
                  password="7986994153",
                  database="myLibrary")

def addbook():
    bname = input("Enter book name:")
    bcode = input("Enter book code:")
    bno = input("Total books:")
    bsub = input("Enter subject:")
    # region
    command = "insert into books values(%s,%s,%s,%s)"
    data = (bname, bcode, bno, bsub)
    c = db.cursor()
    c.execute(command, data)
    db.commit()
    # regionend
    print("processing....")
    print("Data Entered Successfully")
    print("-" * 80)
    main()


def issue():
    # issuing a book to a student
    # ISSUE table
    # does not check if books no longer available
    name = input("Enter Name:")
    Class = input("Enter class:")
    bcode = input("Enter book code:")
    date = input("Enter date of issue (yyyymmdd):")
    cd = "insert into issue values(%s,%s,%s,%s)"
    data = (name, Class, bcode, date)
    c = db.cursor()
    c.execute(cd, data)
    db.commit()
    print("processing...")
    print("Book issued to:", name)
    change(bcode, -1)
    print(
        "-" * 80
    )
    main()


def submit():
    name = input("Enter Name:")
    Class = input("Enter class:")
    bcode = input("Enter book code:")
    d = input("Enter date of issue:")
    cd = "insert into submit values(%s,%s,%s,%s)"
    data = (name, Class, bcode, d)
    c = db.cursor()
    c.execute(cd, data)
    db.commit()
    print("processing...", flush=True)
    # remove me
    time.sleep(1)
    print("Book submitted by:", name)
    change(bcode, 1)
    print("-" * 80)
    main()


def change(code, no):
    s = "select bno from books where bcode=%s"
    b = (code, )
    c = db.cursor()
    c.execute(s, b)
    myresult = c.fetchone()
    updated = myresult[0] + no
    update = "update books set bno=%s where bcode=%s"
    t = (updated, code)
    c.execute(update, t)
    db.commit()
    print("-" * 80)
    main()


def dbook():
    n = input("Enter book code")
    v = "delete from books where bcode=%s"
    y = (n, )
    c = db.cursor()
    c.execute(v, y)
    db.commit()
    print("Book with book code", n, "successfully removed")
    print("-" * 80)
    main()


def display():
    display = "select * from books"
    '''result = pandas.read_sql_query(display, db)
    print("\x1b[91m")
    print(result)
    print("\x1b[0m")'''
    c = db.cursor()
    c.execute(display)
    myresult = c.fetchall()
    for i in myresult:
        print("Book Name:", i[0])
        print("Book Code:", i[1])
        print("Total Books:", i[2])
        print("Subject:", i[3])
        print("-" * 80)
    main()


def main():
    print("""Library Manager\n\n1. Add Book\n2.Issue Book\n3.Submit Book\n4.Delete Book\n5.See All Collection\n""")

    print("-" * 80)
    print("What do you want to do?")
    ask = input("Enter Task no.")
    print("-" * 80)
    if ask == "1":
        addbook()
    elif ask == "2":
        issue()
    elif ask == "3":
        submit()
    elif ask == "4":
        dbook()
    elif ask == "5":
        display()
    else:
        print("Wrong Statement")
        main()

def makeTables():
    # issue_desc = "name varchar(40), class varchar(10), bcode, varchar(20), date date"
    """
    issue_desc
        name,
        class,
        bcode,
        date
    """
    # books_desc = "bname varchar(40), bcode varchar(10), bno int(11), bsub varchar(20)"
    """
    books_desc
        bname,
        bcode,
        bno,
        bsub
    """
    # submit_desc = "name varchar(40), class varchar(10), bcode varchar(20), date date"
    """
    submit_desc
        name
        class
        bcode
        date
    """

    # commands to create needed tables if they dont already exist
    commands = [
        "CREATE TABLE IF NOT EXISTS issue "
        "(name varchar(40), class varchar(10), bcode varchar(20), date date);",
        "CREATE TABLE IF NOT EXISTS books "
        "(bname varchar(40), bcode varchar(10), bno int(11), bsub varchar(20));",
        "CREATE TABLE IF NOT EXISTS submit "
        "(name varchar(40), class varchar(10), bcode varchar(20), date date);"
    ]

    # creating all the tables if they dont exist
    for table_name, command in zip(["issue", "books", "submit"], commands):
        c = db.cursor()
        c.execute(command)
        # error handling kind of
        if c.rowcount <= 0:
            # TABLES ALREADY EXIST
            # [NOTE]: calling cursor.fetchone() or cursor.fetchall()
            #         if the row count if zero raises an exception
            #         No result set to fetch from
            pass
        else:
            myresult = c.fetchall()
            for x in myresult:
                print(x)
            print(f"created {table_name}")

        # lol maybe learn error handling in python

        # ERR: No result set to fetch from?
        # myresult = c.fetchall()
        # for x in myresult:
        #     print(x)
    db.commit()

def password():
    pswd = input("Enter the security key")
    if pswd == "pass":
        main()
    else:
        print("Wrong Password")
        print("Try Again")
        password()

if __name__ == "__main__":
    if "debug" in sys.argv:
        get_books = "select * from books"
        print("processing...", flush=True)
        # using pandas to get sql query results in table form
        results = pandas.read_sql_query(get_books, db)
        print(results)
    else:
        makeTables()
        password()


'''main.pyimport time
import mysql.connector as mydb
db = mydb.connect(host="localhost",
                  user="root",
                  password="7986994153",
                  database="library")

# from replit import db

def addbook():
    bname = input("Enter book name:")
    bcode = input("Enter book code:")
    bno = input("Total books:")
    bsub = input("Enter subject:")
    # region
    command = "insert into books values(%s,%s,%s,%s)"
    data = (bname, bcode, bno, bsub)
    c = db.cursor()
    c.execute(command, data)
    db.commit()
    # regionend
    print("processing....")
    print("Data Entered Successfully")
    print("-" * 80)
    main()


def issue():
    name = input("Enter Name:")
    Class = input("Enter class:")
    bcode = input("Enter book code:")
    date = input("Enter date of issue (yyyymmdd):")
    cd = "insert into issue values(%s,%s,%s,%s)"
    data = (name, Class, bcode, date)
    c = db.cursor()
    c.execute(cd, data)
    db.commit()
    print("processing...")
    print("Book issued to:", name)
    change(bcode, -1)
    print(
        "-" * 80
    )
    main()


def submit():
    name = input("Enter Name:")
    Class = input("Enter class:")
    bcode = input("Enter book code:")
    d = input("Enter date of issue:")
    cd = "insert into submit values(%s,%s,%s,%s)"
    data = (name, Class, bcode, d)
    c = db.cursor()
    c.execute(cd, data)
    db.commit()
    print("processing...", flush=True)
    time.sleep(1)
    print("Book submitted by:", name)
    change(bcode, 1)
    print("-" * 80)
    main()


def change(code, no):
    s = "select bno from books where bcode=%s"
    b = (code, )
    c = db.cursor()
    c.execute(s, b)
    myresult = c.fetchone()
    updated = myresult[0] + no
    update = "update books set bno=%s where bcode=%s"
    t = (updated, code)
    c.execute(update, t)
    db.commit()
    print("-" * 80)
    main()


def dbook():
    n = input("Enter book code")
    v = "delete from books where bcode=%s"
    y = (n, )
    c = db.cursor()
    c.execute(v, y)
    db.commit()
    print("Book with book code", n, "successfully removed")
    print("-" * 80)
    main()


def display():
    display = "select * from books"
    c = db.cursor()
    c.execute(display)
    myresult = c.fetchall()
    for i in myresult:
        print("Book Name:", i[0])
        print("Book Code:", i[1])
        print("Total Books:", i[2])
        print("Subject:", i[3])
        print("-" * 80)
    main()


def main():
    print(
        """
                        Library Manager

        1. Add Book
        2.Issue Book
        3.Submit Book
        4.Delete Book
        5.See All Collection
        """
    )

    print("-" * 80)
    print("What do you want to do?")
    ask = input("Enter Task no.")
    print("-" * 80)
    if ask == "1":
        addbook()
    elif ask == "2":
        issue()
    elif ask == "3":
        submit()
    elif ask == "4":
        dbook()
    elif ask == "5":
        display()
    else:
        print("Wrong Statement")
        main()


def password():
    pswd = input("Enter the security key")
    if pswd == "hello world":
        main()
    else:
        print("Wrong Password")
        print("Try Again")
        password()

password()'''
# idea:
# grep -rn

# gui based on books ulimately


