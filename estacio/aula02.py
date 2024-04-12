import sqlite3  
import tkinter as tk
from datetime import datetime

conn = sqlite3.connect('lab_keys.db')
cursor  = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS lab_keys(name TEXT, registration TEXT, key TEXT, date_time TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS returned_keys(name TEXT, key TEXT, return_time TEXT)''')






root.mainloop()