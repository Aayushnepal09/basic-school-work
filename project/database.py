import sqlite3
from tkinter import *

root = Tk()
root.title('database address book')

# database

# creating a database or connect to one
conn = sqlite3.connect('addresses_book.db')

# creating cursor
'''cursor is an instance using which you can invoke methods that
execute SQLITE statement, fetch data from the result sets of the quarries'''
c = conn.cursor()
# c.execute("""CREATE TABLE ADDRESSES(
#             first_name text ,
#             last_name text,
#             address text,
#             city text
#             state text
#             zipcode integer
# )
# """)
# print("Table created successfully")

# commit change
conn.commit()
conn.close()
root.mainloop()
