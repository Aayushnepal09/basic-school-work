import sqlite3
from tkinter import*
root=Tk()
root.title('database address book')


#database

#creaing a database or connect to one
conn=sqlite3.connect(('aaddress_book.db'))

#creating cursor
'''curser is an instance using which you can invoke methords that
execute SQLITE statement, ferch data from the result sets of the querirs'''
c= conn.cursor()
c.execute("""CREATE TABLE ADDRESSES(
            first_name text,
            last_name text,
            address text,
            city text
            state text
            zipcode integer
)
""")
print("Table created successfully")

#commit change
conn.commit()
conn.close()
root.mainloop()